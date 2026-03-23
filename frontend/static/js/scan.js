/**
 * scan.js v3 — AR Scan & Learn interface.
 *
 * Flow:
 *   1. Camera opens fullscreen, YOLO model loads
 *   2. User taps "Detect" → runs one detection pass, shows results
 *   3. User taps "Generate" → fetches sentence for detected objects
 *   4. User taps "Record" → records speech, submits for analysis
 *   5. Results slide up from bottom
 */

var CONF_THRESHOLD = 0.35;
var IOU_THRESHOLD = 0.45;
var MODEL_INPUT_SIZE = 640;

var CLASS_NAMES = [
    "person","bicycle","car","motorcycle","airplane","bus","train","truck","boat",
    "traffic light","fire hydrant","stop sign","parking meter","bench","bird","cat",
    "dog","horse","sheep","cow","elephant","bear","zebra","giraffe","backpack",
    "umbrella","handbag","tie","suitcase","frisbee","skis","snowboard","sports ball",
    "kite","baseball bat","baseball glove","skateboard","surfboard","tennis racket",
    "bottle","wine glass","cup","fork","knife","spoon","bowl","banana","apple",
    "sandwich","orange","broccoli","carrot","hot dog","pizza","donut","cake",
    "chair","couch","potted plant","bed","dining table","toilet","tv","laptop",
    "mouse","keyboard","cell phone","microwave","oven","toaster","sink",
    "refrigerator","book","clock","vase","scissors","teddy bear","hair drier",
    "toothbrush"
];

// ── DOM Elements ────────────────────────────────────────────────────────────

var videoEl = document.getElementById("camera");
var overlayEl = document.getElementById("overlay");
var loadingMsg = document.getElementById("loading-msg");
var drawCtx = overlayEl ? overlayEl.getContext("2d") : null;

var detectBtn = document.getElementById("ar-detect-btn");
var generateBtn = document.getElementById("ar-generate-btn");
var listenBtn = document.getElementById("ar-listen-btn");
var recordBtn = document.getElementById("ar-record-btn");
var nextBtn = document.getElementById("ar-next-btn");

var detectedLabel = document.getElementById("ar-detected-label");
var sentenceEl = document.getElementById("ar-sentence");
var statusEl = document.getElementById("ar-status");
var topStatus = document.getElementById("ar-topbar-status");

var resultsPanel = document.getElementById("ar-results");
var resultsClose = document.getElementById("ar-results-close");

// ── State ───────────────────────────────────────────────────────────────────

var yoloSession = null;
var currentDetections = [];     // latest detection results
var currentObjects = [];        // unique object labels
var currentSentence = "";
var currentObjectName = "";
var sentenceLoading = false;

// Recording
var manualRecording = false;
var mediaRecorder = null;
var audioChunks = [];
var ttsAudio = null;

// ── Camera ──────────────────────────────────────────────────────────────────

async function startCamera() {
    try {
        var stream = await navigator.mediaDevices.getUserMedia({
            video: { facingMode: "environment", width: { ideal: 1280 }, height: { ideal: 720 } },
            audio: false,
        });
        videoEl.srcObject = stream;
        await new Promise(function (r) { videoEl.onloadedmetadata = r; });
        overlayEl.width = videoEl.videoWidth;
        overlayEl.height = videoEl.videoHeight;
    } catch (err) {
        console.error("Camera access denied:", err);
        loadingMsg.textContent = "Camera access denied. Please allow camera permissions.";
    }
}

// ── YOLO Model ──────────────────────────────────────────────────────────────

async function loadModel() {
    try {
        ort.env.wasm.wasmPaths = "https://cdn.jsdelivr.net/npm/onnxruntime-web@1.22.0/dist/";
        yoloSession = await ort.InferenceSession.create("/static/models/yolo11s.onnx", {
            executionProviders: ["wasm"],
        });
        loadingMsg.style.display = "none";
        topStatus.textContent = "Ready";
        console.log("YOLO11s model loaded.");
    } catch (err) {
        console.error("Failed to load model:", err);
        loadingMsg.textContent = "Failed to load detection model.";
    }
}


// ── Preprocessing ───────────────────────────────────────────────────────────

function preprocess(video) {
    var canvas = document.createElement("canvas");
    canvas.width = MODEL_INPUT_SIZE;
    canvas.height = MODEL_INPUT_SIZE;
    var c = canvas.getContext("2d");

    var scale = Math.min(MODEL_INPUT_SIZE / video.videoWidth, MODEL_INPUT_SIZE / video.videoHeight);
    var nw = Math.round(video.videoWidth * scale);
    var nh = Math.round(video.videoHeight * scale);
    var dx = (MODEL_INPUT_SIZE - nw) / 2;
    var dy = (MODEL_INPUT_SIZE - nh) / 2;

    c.fillStyle = "#808080";
    c.fillRect(0, 0, MODEL_INPUT_SIZE, MODEL_INPUT_SIZE);
    c.drawImage(video, dx, dy, nw, nh);

    var imageData = c.getImageData(0, 0, MODEL_INPUT_SIZE, MODEL_INPUT_SIZE);
    var pixels = imageData.data;
    var float32 = new Float32Array(3 * MODEL_INPUT_SIZE * MODEL_INPUT_SIZE);
    var area = MODEL_INPUT_SIZE * MODEL_INPUT_SIZE;

    for (var i = 0; i < area; i++) {
        float32[i] = pixels[i * 4] / 255;
        float32[area + i] = pixels[i * 4 + 1] / 255;
        float32[area * 2 + i] = pixels[i * 4 + 2] / 255;
    }

    return { tensor: new ort.Tensor("float32", float32, [1, 3, MODEL_INPUT_SIZE, MODEL_INPUT_SIZE]), scale: scale, dx: dx, dy: dy };
}

// ── Postprocessing (NMS) ────────────────────────────────────────────────────

function postprocess(output, scale, dx, dy) {
    var data = output.data;
    var numDetections = 8400;
    var numClasses = CLASS_NAMES.length;
    var boxes = [];

    for (var i = 0; i < numDetections; i++) {
        var maxScore = 0;
        var classId = 0;
        for (var c = 0; c < numClasses; c++) {
            var score = data[(4 + c) * numDetections + i];
            if (score > maxScore) { maxScore = score; classId = c; }
        }
        if (maxScore < CONF_THRESHOLD) continue;

        var cx = data[0 * numDetections + i];
        var cy = data[1 * numDetections + i];
        var w  = data[2 * numDetections + i];
        var h  = data[3 * numDetections + i];

        boxes.push({
            x1: (cx - w/2 - dx) / scale, y1: (cy - h/2 - dy) / scale,
            x2: (cx + w/2 - dx) / scale, y2: (cy + h/2 - dy) / scale,
            score: maxScore, classId: classId, label: CLASS_NAMES[classId]
        });
    }

    boxes.sort(function (a, b) { return b.score - a.score; });
    var kept = [];
    var suppressed = {};

    for (var i = 0; i < boxes.length; i++) {
        if (suppressed[i]) continue;
        kept.push(boxes[i]);
        for (var j = i + 1; j < boxes.length; j++) {
            if (suppressed[j]) continue;
            if (boxes[i].classId === boxes[j].classId && iou(boxes[i], boxes[j]) > IOU_THRESHOLD) {
                suppressed[j] = true;
            }
        }
    }
    return kept;
}

function iou(a, b) {
    var x1 = Math.max(a.x1, b.x1), y1 = Math.max(a.y1, b.y1);
    var x2 = Math.min(a.x2, b.x2), y2 = Math.min(a.y2, b.y2);
    var inter = Math.max(0, x2 - x1) * Math.max(0, y2 - y1);
    var aArea = (a.x2 - a.x1) * (a.y2 - a.y1);
    var bArea = (b.x2 - b.x1) * (b.y2 - b.y1);
    return inter / (aArea + bArea - inter);
}

// ── Drawing ─────────────────────────────────────────────────────────────────

function drawDetections(detections) {
    drawCtx.clearRect(0, 0, overlayEl.width, overlayEl.height);

    for (var d = 0; d < detections.length; d++) {
        var det = detections[d];
        var x = Math.max(0, det.x1);
        var y = Math.max(0, det.y1);
        var w = Math.min(overlayEl.width, det.x2) - x;
        var h = Math.min(overlayEl.height, det.y2) - y;

        drawCtx.strokeStyle = "#4f46e5";
        drawCtx.lineWidth = 3;
        drawCtx.strokeRect(x, y, w, h);

        var text = det.label + " " + Math.round(det.score * 100) + "%";
        drawCtx.font = "bold 16px sans-serif";
        var tw = drawCtx.measureText(text).width;
        drawCtx.fillStyle = "rgba(79,70,229,0.85)";
        drawCtx.fillRect(x, y - 24, tw + 10, 24);
        drawCtx.fillStyle = "#fff";
        drawCtx.fillText(text, x + 5, y - 6);
    }
}

function clearDetections() {
    drawCtx.clearRect(0, 0, overlayEl.width, overlayEl.height);
}

// ── Detect Button (one-shot detection) ──────────────────────────────────────

detectBtn.addEventListener("click", async function () {
    if (!yoloSession) {
        statusEl.textContent = "Model not loaded yet.";
        return;
    }

    detectBtn.textContent = "Detecting...";
    detectBtn.classList.add("detecting");
    statusEl.textContent = "Scanning for objects...";

    try {
        var prep = preprocess(videoEl);
        var feeds = {};
        feeds[yoloSession.inputNames[0]] = prep.tensor;
        var results = await yoloSession.run(feeds);
        var output = results[yoloSession.outputNames[0]];
        currentDetections = postprocess(output, prep.scale, prep.dx, prep.dy);
        drawDetections(currentDetections);

        // Extract unique labels
        var seen = {};
        currentObjects = [];
        for (var i = 0; i < currentDetections.length; i++) {
            if (!seen[currentDetections[i].label]) {
                seen[currentDetections[i].label] = true;
                currentObjects.push(currentDetections[i].label);
            }
        }

        if (currentObjects.length > 0) {
            detectedLabel.textContent = "Detected: " + currentObjects.join(", ");
            currentObjectName = currentObjects[0];
            generateBtn.disabled = false;
            statusEl.textContent = currentObjects.length + " object(s) found. Tap Generate for a sentence.";
        } else {
            detectedLabel.textContent = "No objects detected";
            generateBtn.disabled = true;
            statusEl.textContent = "Try pointing at a common object and tap Detect again.";
        }
    } catch (err) {
        console.error("Detection error:", err);
        statusEl.textContent = "Detection failed. Try again.";
    }

    detectBtn.textContent = "Detect";
    detectBtn.classList.remove("detecting");
});

// ── Generate Button ─────────────────────────────────────────────────────────

generateBtn.addEventListener("click", async function () {
    if (currentObjects.length === 0) return;
    if (sentenceLoading) return;

    sentenceLoading = true;
    generateBtn.disabled = true;
    sentenceEl.textContent = "Generating sentence...";
    statusEl.textContent = "";

    try {
        if (currentObjects.length >= 2) {
            var detList = currentObjects.map(function (o) { return { label: o, confidence: 0.9 }; });
            var resp = await fetch("/api/scene-describe", {
                method: "POST",
                headers: { "Content-Type": "application/x-www-form-urlencoded" },
                body: "detections=" + encodeURIComponent(JSON.stringify(detList)) + "&difficulty=A2",
            });
            var data = await resp.json();
            currentSentence = data.sentence || data.description || ("I can see a " + currentObjects.join(" and a ") + ".");
        } else {
            var resp = await fetch("/api/generate", {
                method: "POST",
                headers: { "Content-Type": "application/x-www-form-urlencoded" },
                body: "object_name=" + encodeURIComponent(currentObjects[0]) + "&difficulty=A2",
            });
            var data = await resp.json();
            currentSentence = data.sentence || ("I can see a " + currentObjects[0] + ".");
        }
    } catch (e) {
        currentSentence = "I can see a " + currentObjects[0] + ".";
    }

    sentenceEl.textContent = currentSentence;
    sentenceLoading = false;
    generateBtn.disabled = false;

    // Enable practice buttons
    listenBtn.disabled = false;
    recordBtn.disabled = false;
    nextBtn.disabled = false;

    statusEl.textContent = "Read the sentence aloud. Tap Record when ready.";
});

// ── Recording ───────────────────────────────────────────────────────────────

recordBtn.addEventListener("click", function () {
    if (!currentSentence) return;
    toggleManualRecording();
});

function toggleManualRecording() {
    if (manualRecording) {
        // Stop recording
        if (mediaRecorder && mediaRecorder.state !== "inactive") mediaRecorder.stop();
        manualRecording = false;
        recordBtn.classList.remove("ar-recording");
        recordBtn.textContent = "Record";
        statusEl.textContent = "Processing...";
    } else {
        // Start recording
        navigator.mediaDevices.getUserMedia({ audio: true }).then(function (stream) {
            mediaRecorder = new MediaRecorder(stream);
            audioChunks = [];
            mediaRecorder.ondataavailable = function (e) { if (e.data.size > 0) audioChunks.push(e.data); };
            mediaRecorder.onstop = function () {
                var blob = new Blob(audioChunks, { type: "audio/webm" });
                stream.getTracks().forEach(function (t) { t.stop(); });
                submitRecording(blob);
            };
            mediaRecorder.start();
            manualRecording = true;
            recordBtn.classList.add("ar-recording");
            recordBtn.textContent = "Stop";
            statusEl.textContent = "Recording... Tap Stop when done.";
        }).catch(function () {
            statusEl.textContent = "Microphone access denied.";
        });
    }
}

// ── TTS ─────────────────────────────────────────────────────────────────────

listenBtn.addEventListener("click", async function () {
    if (!currentSentence) return;
    if (ttsAudio) { ttsAudio.pause(); ttsAudio.currentTime = 0; }
    listenBtn.textContent = "...";

    // Try server TTS first, fall back to browser speechSynthesis
    try {
        var resp = await fetch("/api/tts?text=" + encodeURIComponent(currentSentence));
        if (resp.ok) {
            var blob = await resp.blob();
            var url = URL.createObjectURL(blob);
            ttsAudio = new Audio(url);
            ttsAudio.onended = function () { listenBtn.textContent = "Listen"; URL.revokeObjectURL(url); };
            ttsAudio.onerror = function () { listenBtn.textContent = "Listen"; speakBrowser(currentSentence); };
            await ttsAudio.play();
            listenBtn.textContent = "Playing";
            return;
        }
    } catch (e) { /* fall through to browser TTS */ }

    speakBrowser(currentSentence);
});

function speakBrowser(text) {
    if (!window.speechSynthesis) {
        listenBtn.textContent = "Listen";
        statusEl.textContent = "TTS not available on this device.";
        return;
    }
    var utter = new SpeechSynthesisUtterance(text);
    utter.lang = "en-US";
    utter.rate = 0.9;
    utter.onstart = function () { listenBtn.textContent = "Playing"; };
    utter.onend = function () { listenBtn.textContent = "Listen"; };
    utter.onerror = function () { listenBtn.textContent = "Listen"; };
    speechSynthesis.speak(utter);
}

// ── Next Sentence ───────────────────────────────────────────────────────────

nextBtn.addEventListener("click", function () {
    resultsPanel.classList.remove("visible");
    if (currentObjects.length > 0) {
        sentenceLoading = false;
        generateBtn.click();
    }
});

// ── Submit Recording ────────────────────────────────────────────────────────

async function submitRecording(audioBlob) {
    statusEl.textContent = "Analyzing...";
    recordBtn.disabled = true;

    // Wait for auth to resolve so we get the real learner_id
    if (typeof authReady !== "undefined") {
        await authReady;
    }
    var learnerId = typeof getLearnerId === "function" ? getLearnerId() : "default";
    var formData = new FormData();
    formData.append("audio", audioBlob, "recording.wav");
    formData.append("reference_text", currentSentence);
    formData.append("object_name", currentObjectName);
    formData.append("learner_id", learnerId);

    try {
        var resp = await fetch("/api/record", { method: "POST", body: formData });
        var data = await resp.json();

        // Server mode: poll for results via job_id
        if (data.status === "queued" && data.job_id) {
            data = await pollForResults(data.job_id);
        }

        showResults(data);
    } catch (err) {
        statusEl.textContent = "Upload failed. Try again.";
    }

    recordBtn.disabled = false;
}

async function pollForResults(jobId) {
    var maxAttempts = 120;  // 2 minutes at 1s intervals
    for (var i = 0; i < maxAttempts; i++) {
        await new Promise(function (r) { setTimeout(r, 1000); });
        try {
            var resp = await fetch("/api/recording/" + jobId);
            var data = await resp.json();
            if (data.status === "complete") return data.result || data;
            if (data.status === "error") return { status: "error", message: data.message || "Analysis failed" };
            statusEl.textContent = data.message || "Analyzing...";
        } catch (err) {
            // Network error, keep trying
        }
    }
    return { status: "error", message: "Analysis timed out" };
}

// ── Show Results ────────────────────────────────────────────────────────────

function showResults(data) {
    if (data.status === "error") {
        statusEl.textContent = "Error: " + (data.message || "Unknown");
        return;
    }
    statusEl.textContent = "Done! Tap Record to try again.";

    // XP earned
    var xpBanner = document.getElementById("ar-xp-banner");
    var xpText = document.getElementById("ar-xp-text");
    if (xpBanner && xpText && data.xp_earned) {
        xpBanner.style.display = "block";
        xpText.textContent = "+" + data.xp_earned + " XP" + (data.streak > 1 ? "  |  " + data.streak + " day streak!" : "");
    }

    // Verdict
    var total = data.total != null ? data.total : "--";
    setEl("ar-verdict-score", total);
    var banner = document.getElementById("ar-verdict-banner");
    if (banner && typeof total === "number") {
        banner.className = "verdict-banner " + (total >= 70 ? "verdict-good" : total >= 40 ? "verdict-ok" : "verdict-low");
    }
    var vLabel = document.getElementById("ar-verdict-label");
    if (vLabel && data.classification) {
        vLabel.textContent = data.classification === "CORRECT" ? "Excellent!" : data.classification === "PARTIAL" ? "Good effort" : "Try again";
    }

    // 4D scores
    setScoreEl("ar-s-accuracy", data.accuracy);
    setScoreEl("ar-s-fluency", data.fluency);
    setScoreEl("ar-s-prosody", data.prosody);
    setScoreEl("ar-s-completeness", data.completeness);

    // Word feedback
    var wf = document.getElementById("ar-word-feedback");
    if (data.words && wf) {
        wf.innerHTML = data.words.map(function (w) {
            return '<span class="word-' + w.status + '">' + w.word + ' </span>';
        }).join("");
    }

    // Transcript
    var tEl = document.getElementById("ar-transcript");
    if (data.transcript && tEl) {
        tEl.style.display = "block";
        tEl.textContent = 'You said: "' + data.transcript + '"';
    }

    // Skill bars
    renderArSkillBars(data.skill_bars);

    // Phoneme analysis
    renderPhonemeAnalysis(data);

    // Details grid
    var dg = document.getElementById("ar-details-grid");
    if (dg) {
        dg.innerHTML = [
            detailItem("WPM", fmtN(data.words_per_minute, 0)),
            detailItem("Art. Rate", fmtN(data.articulation_rate, 1) + " syll/s"),
            detailItem("Run Length", fmtN(data.mean_length_of_run, 1)),
            detailItem("Longest", (data.longest_fluent_phrase || 0) + " words"),
            detailItem("Fillers", data.filler_count != null ? data.filler_count : "--"),
            detailItem("Reps", data.repetition_count != null ? data.repetition_count : "--"),
            detailItem("Stress", fmtPct(data.stress_accuracy)),
            detailItem("Intonation", fmtPct(data.intonation_accuracy)),
            detailItem("Rhythm", fmtN(data.rhythm_npvi_v, 1)),
            detailItem("Pitch", fmtN(data.pitch_range_st, 1) + " ST"),
            detailItem("WER", data.wer != null ? fmtN(data.wer * 100, 1) + "%" : "--"),
            detailItem("Duration", data.duration_sec != null ? data.duration_sec + "s" : "--"),
        ].join("");
    }

    // Slide panel up
    resultsPanel.classList.add("visible");
}

// ── Skill Bars ─────────────────────────────────────────────────────────────

function renderArSkillBars(bars) {
    var card = document.getElementById("ar-skill-bars-card");
    if (!bars || bars.length === 0) {
        if (card) card.style.display = "none";
        return;
    }
    if (card) card.style.display = "block";

    for (var i = 0; i < bars.length; i++) {
        var bar = bars[i];
        var fill = document.getElementById("ar-bar-" + bar.name);
        var starsEl = document.getElementById("ar-stars-" + bar.name);
        if (!fill) continue;

        var pct = Math.max(0, Math.min(100, bar.value));
        fill.style.width = pct + "%";
        fill.className = "skill-fill " + (pct >= 70 ? "fill-high" : pct >= 40 ? "fill-mid" : "fill-low");

        if (starsEl) {
            var stars = bar.stars || 1;
            var starStr = "";
            for (var s = 0; s < 5; s++) {
                starStr += s < stars ? "\u2B50" : "\u2606";
            }
            var delta = bar.delta || 0;
            var deltaHtml = "";
            if (delta > 0) {
                deltaHtml = '<span class="skill-delta up">+' + delta + ' \u2191</span>';
            } else if (delta < 0) {
                deltaHtml = '<span class="skill-delta down">' + delta + ' \u2193</span>';
            } else if (bar.prev_stars != null) {
                deltaHtml = '<span class="skill-delta same">=</span>';
            }
            starsEl.innerHTML = starStr + deltaHtml;
        }
    }
}

// ── Close Results ───────────────────────────────────────────────────────────

resultsClose.addEventListener("click", function () {
    resultsPanel.classList.remove("visible");
});

// ── Phoneme Analysis Display ────────────────────────────────────────────────

function renderPhonemeAnalysis(data) {
    var card = document.getElementById("ar-phoneme-card");
    var summaryEl = document.getElementById("ar-phoneme-summary");
    var gridEl = document.getElementById("ar-phoneme-grid");

    if (!card || !data.phone_errors || data.phone_errors.length === 0) {
        if (card) card.style.display = "none";
        return;
    }

    card.style.display = "block";

    var counts = data.mdd_counts || { correct: 0, substitution: 0, deletion: 0, insertion: 0 };
    summaryEl.innerHTML =
        '<span class="ph-stat ph-correct">' + counts.correct + ' correct</span>' +
        '<span class="ph-stat ph-sub">' + counts.substitution + ' sub</span>' +
        '<span class="ph-stat ph-del">' + counts.deletion + ' del</span>' +
        '<span class="ph-stat ph-ins">' + counts.insertion + ' ins</span>' +
        (data.phone_error_rate != null ? '<span class="ph-stat">PER: ' + data.phone_error_rate + '%</span>' : '');

    gridEl.innerHTML = data.phone_errors.map(function (pe) {
        var cls = "ph-chip ph-" + pe.error_type;
        var label = "/" + pe.canonical + "/";
        var detail = "";
        if (pe.error_type === "substitution") {
            detail = "heard /" + pe.predicted + "/";
        } else if (pe.error_type === "deletion") {
            detail = "missing";
        } else if (pe.error_type === "insertion") {
            label = "/" + pe.predicted + "/";
            detail = "extra";
        }
        return '<div class="' + cls + '">' +
            '<span class="ph-phone">' + label + '</span>' +
            (detail ? '<span class="ph-detail">' + detail + '</span>' : '') +
            '</div>';
    }).join("");
}

// ── WAV Encoding ────────────────────────────────────────────────────────────

function float32ToWav(float32Array, sampleRate) {
    var numSamples = float32Array.length;
    var buffer = new ArrayBuffer(44 + numSamples * 2);
    var view = new DataView(buffer);

    writeStr(view, 0, "RIFF");
    view.setUint32(4, 36 + numSamples * 2, true);
    writeStr(view, 8, "WAVE");
    writeStr(view, 12, "fmt ");
    view.setUint32(16, 16, true);
    view.setUint16(20, 1, true);
    view.setUint16(22, 1, true);
    view.setUint32(24, sampleRate, true);
    view.setUint32(28, sampleRate * 2, true);
    view.setUint16(32, 2, true);
    view.setUint16(34, 16, true);
    writeStr(view, 36, "data");
    view.setUint32(40, numSamples * 2, true);

    for (var i = 0; i < numSamples; i++) {
        var s = Math.max(-1, Math.min(1, float32Array[i]));
        view.setInt16(44 + i * 2, s < 0 ? s * 0x8000 : s * 0x7FFF, true);
    }
    return new Blob([buffer], { type: "audio/wav" });
}

function writeStr(view, offset, str) {
    for (var i = 0; i < str.length; i++) view.setUint8(offset + i, str.charCodeAt(i));
}

// ── Helpers ─────────────────────────────────────────────────────────────────

function setEl(id, val) {
    var el = document.getElementById(id);
    if (el) el.textContent = val != null ? val : "--";
}

function setScoreEl(id, val) {
    var el = document.getElementById(id);
    if (!el) return;
    el.textContent = val != null ? val : "--";
    el.className = "score-value " + (val >= 70 ? "score-high" : val >= 40 ? "score-mid" : "score-low");
}

function fmtN(val, dec) {
    if (val == null) return "--";
    return typeof val === "number" ? val.toFixed(dec != null ? dec : 0) : val;
}

function fmtPct(val) {
    return val != null ? Math.round(val) + "%" : "--";
}

function detailItem(label, val) {
    return '<div class="detail-item"><span class="detail-val">' + val + '</span><span class="detail-lbl">' + label + '</span></div>';
}

// ── Init ────────────────────────────────────────────────────────────────────

async function init() {
    await startCamera();
    await loadModel();
}

init();
