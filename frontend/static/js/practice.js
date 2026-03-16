/**
 * practice.js — Redesigned practice page.
 *
 * Flow:
 *   1. Load available objects into dropdown (or pre-select from assignment URL)
 *   2. User picks object + level, taps "Generate Sentence"
 *   3. Sentence appears — Listen and Record buttons enable
 *   4. Record → manual start/stop → submit to server
 *   5. Results displayed below
 */

// Toggle for teacher details (must be global for onclick)
function toggleTeacherDetails() {
    var body = document.getElementById("teacher-details-body");
    var arrow = document.getElementById("toggle-arrow");
    if (!body) return;
    if (body.style.display === "none") {
        body.style.display = "block";
        if (arrow) arrow.classList.add("open");
    } else {
        body.style.display = "none";
        if (arrow) arrow.classList.remove("open");
    }
}

document.addEventListener("DOMContentLoaded", function () {

// ── DOM refs ────────────────────────────────────────────────────────────────

var objectSelect  = document.getElementById("object-select");
var levelSelect   = document.getElementById("level-select");
var generateBtn   = document.getElementById("generate-btn");
var referenceText = document.getElementById("reference-text");
var listenBtn     = document.getElementById("listen-btn");
var startBtn      = document.getElementById("start-btn");
var stopBtn       = document.getElementById("stop-btn");
var statusText    = document.getElementById("status-text");
var resultsCard   = document.getElementById("results-card");

if (!generateBtn || !startBtn || !stopBtn) return; // page is redirecting

// ── URL params (from assignment or scan page) ──────────────────────────────

var params     = new URLSearchParams(window.location.search);
var assignedObject = params.get("object");

// ── State ───────────────────────────────────────────────────────────────────

var currentSentence = "";
var currentObject   = "";
var mediaRecorder   = null;
var audioChunks     = [];
var mediaStream     = null;
var ttsAudio        = null;

// ── Init: load objects ─────────────────────────────────────────────────────

(async function init() {
    try {
        var resp = await fetch("/api/objects");
        var data = await resp.json();
        var objects = data.objects || [];

        objectSelect.innerHTML = "";
        for (var i = 0; i < objects.length; i++) {
            var opt = document.createElement("option");
            opt.value = objects[i];
            opt.textContent = objects[i].charAt(0).toUpperCase() + objects[i].slice(1);
            objectSelect.appendChild(opt);
        }

        if (assignedObject) {
            objectSelect.value = assignedObject.toLowerCase();
            if (!objectSelect.value) {
                var opt = document.createElement("option");
                opt.value = assignedObject.toLowerCase();
                opt.textContent = assignedObject;
                objectSelect.appendChild(opt);
                objectSelect.value = assignedObject.toLowerCase();
            }
        }

        generateBtn.disabled = false;
    } catch (e) {
        objectSelect.innerHTML = '<option value="bottle">Bottle</option><option value="remote">Remote</option><option value="person">Person</option>';
        generateBtn.disabled = false;
    }

    if (assignedObject) {
        generateSentence();
    }
})();

// ── Generate Sentence ──────────────────────────────────────────────────────

generateBtn.addEventListener("click", generateSentence);

async function generateSentence() {
    var obj   = objectSelect.value;
    var level = levelSelect.value;
    if (!obj) return;

    currentObject = obj;
    generateBtn.disabled = true;
    generateBtn.textContent = "Loading...";
    referenceText.textContent = "Loading sentence...";

    try {
        var resp = await fetch("/api/generate", {
            method: "POST",
            headers: { "Content-Type": "application/x-www-form-urlencoded" },
            body: "object_name=" + encodeURIComponent(obj) + "&difficulty=" + encodeURIComponent(level),
        });
        var data = await resp.json();
        currentSentence = data.sentence || "I can see a " + obj + ".";
        referenceText.textContent = currentSentence;
    } catch (e) {
        currentSentence = "I can see a " + obj + ".";
        referenceText.textContent = currentSentence;
    }

    generateBtn.disabled = false;
    generateBtn.textContent = "Generate Sentence";

    listenBtn.disabled = false;
    startBtn.disabled = false;
    statusText.textContent = "Press Start Recording when ready";

    resultsCard.style.display = "none";
}

// ── Start / Stop Recording ────────────────────────────────────────────────

startBtn.addEventListener("click", async function () {
    if (!currentSentence) return;
    try {
        mediaStream = await navigator.mediaDevices.getUserMedia({ audio: true });
        mediaRecorder = new MediaRecorder(mediaStream);
        audioChunks = [];

        mediaRecorder.ondataavailable = function (e) {
            if (e.data.size > 0) audioChunks.push(e.data);
        };

        mediaRecorder.onstop = function () {
            var audioBlob = new Blob(audioChunks, { type: "audio/webm" });
            mediaStream.getTracks().forEach(function (t) { t.stop(); });
            mediaStream = null;
            submitRecording(audioBlob);
        };

        mediaRecorder.start();
        startBtn.style.display = "none";
        stopBtn.style.display = "";
        statusText.textContent = "Recording... Speak now!";
    } catch (err) {
        console.error("Microphone access denied:", err);
        statusText.textContent = "Microphone access denied.";
    }
});

stopBtn.addEventListener("click", function () {
    if (mediaRecorder && mediaRecorder.state !== "inactive") {
        mediaRecorder.stop();
    }
    stopBtn.style.display = "none";
    startBtn.style.display = "";
    statusText.textContent = "Processing...";
});

// ── Submit to Server ──────────────────────────────────────────────────────

async function submitRecording(audioBlob) {
    if (typeof authReady !== "undefined") {
        await authReady;
    }
    var learnerId = typeof getLearnerId === "function" ? getLearnerId() : "default";

    statusText.textContent = "Analyzing your speech...";
    startBtn.disabled = true;

    var formData = new FormData();
    formData.append("audio", audioBlob, "recording.wav");
    formData.append("reference_text", currentSentence);
    formData.append("object_name", currentObject);
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
        console.error("Upload failed:", err);
        statusText.textContent = "Upload failed. Try again.";
    }

    startBtn.disabled = false;
}

async function pollForResults(jobId) {
    var maxAttempts = 120;
    for (var i = 0; i < maxAttempts; i++) {
        await new Promise(function (r) { setTimeout(r, 1000); });
        try {
            var resp = await fetch("/api/recording/" + jobId);
            var data = await resp.json();
            if (data.status === "complete") return data.result || data;
            if (data.status === "error") return { status: "error", message: data.message || "Analysis failed" };
            statusText.textContent = data.message || "Analyzing...";
        } catch (err) { /* keep trying */ }
    }
    return { status: "error", message: "Analysis timed out" };
}

// ── Display Results ───────────────────────────────────────────────────────

function showResults(data) {
    if (data.status === "error") {
        statusText.textContent = "Analysis failed: " + (data.message || "Unknown error");
        return;
    }

    var xpMsg = "";
    if (data.xp_earned) {
        xpMsg = "  |  +" + data.xp_earned + " XP";
        if (data.streak > 1) xpMsg += "  |  " + data.streak + " day streak!";
    }
    statusText.textContent = "Done! Record again or generate a new sentence." + xpMsg;
    resultsCard.style.display = "block";

    var total = data.total != null ? data.total : "--";
    setVal("verdict-score", total);
    var banner = document.getElementById("verdict-banner");
    if (banner && typeof total === "number") {
        banner.className = "verdict-banner " + verdictClass(total);
    }
    var verdictLabel = document.getElementById("verdict-label");
    if (verdictLabel && data.classification) {
        var cls = data.classification;
        var label = cls === "CORRECT" ? "Excellent!" : cls === "PARTIAL" ? "Good effort" : "Try again";
        verdictLabel.textContent = label;
    }

    // Render insights (student-facing)
    renderInsights(data.insights);

    // Render skill bars (student-friendly)
    renderSkillBars(data.skill_bars);

    // Word-level feedback (FL-weighted coloring)
    var feedbackEl = document.getElementById("word-feedback");
    if (data.words && feedbackEl) {
        feedbackEl.innerHTML = data.words
            .map(function (w) {
                var cls = "word-" + w.status;
                var title = "";
                if (w.status === "fl-high") title = ' title="High impact on understanding (FL ' + (w.fl || "") + ')"';
                else if (w.status === "fl-low") title = ' title="Minor pronunciation difference (FL ' + (w.fl || "") + ')"';
                return '<span class="' + cls + '"' + title + '>' + w.word + ' </span>';
            })
            .join("");
    }

    var transcriptEl = document.getElementById("transcript-line");
    if (data.transcript && transcriptEl) {
        transcriptEl.style.display = "block";
        transcriptEl.textContent = 'You said: "' + data.transcript + '"';
    }

    var badgeEl = document.getElementById("classification-badge");
    if (data.classification && badgeEl) {
        var badgeCls = data.classification === "CORRECT" ? "badge-correct"
            : data.classification === "PARTIAL" ? "badge-partial" : "badge-retry";
        badgeEl.style.display = "inline-block";
        badgeEl.className = "classification-badge " + badgeCls;
        badgeEl.textContent = data.classification.replace("_", " ");
    }

    // Phoneme analysis
    renderPhonemeResults(data);

    // Teacher details (raw numbers — collapsed by default)
    renderTeacherDetails(data);

    var wsCard = document.getElementById("word-scores-card");
    var wsTbody = document.getElementById("word-scores-tbody");
    if (data.word_scores && data.word_scores.length > 0 && wsCard && wsTbody) {
        wsCard.style.display = "block";
        wsTbody.innerHTML = data.word_scores.map(function (ws) {
            var labelCls = ws.label === "C" ? "score-high"
                : ws.label === "S" ? "score-low"
                : ws.label === "R" ? "score-mid"
                : "score-low";
            var labelText = ws.label === "C" ? "Correct"
                : ws.label === "S" ? "Substitution"
                : ws.label === "D" ? "Deletion"
                : ws.label === "I" ? "Insertion"
                : ws.label === "R" ? "Repetition"
                : ws.label;
            return '<tr>'
                + '<td>' + ws.word + '</td>'
                + '<td class="' + scoreColor(ws.accuracy) + '">' + Math.round(ws.accuracy) + '</td>'
                + '<td class="' + labelCls + '">' + labelText + '</td>'
                + '</tr>';
        }).join("");
    }

    resultsCard.scrollIntoView({ behavior: "smooth", block: "start" });
}

// ── Phoneme Analysis ──────────────────────────────────────────────────────

function renderPhonemeResults(data) {
    var card = document.getElementById("phoneme-card");
    var summaryEl = document.getElementById("phoneme-summary");
    var gridEl = document.getElementById("phoneme-grid");

    if (!card || !data.phone_errors || data.phone_errors.length === 0) {
        if (card) card.style.display = "none";
        return;
    }

    card.style.display = "block";

    var counts = data.mdd_counts || { correct: 0, substitution: 0, deletion: 0, insertion: 0 };
    var l1Count = 0;
    data.phone_errors.forEach(function (pe) { if (pe.l1_expected) l1Count++; });
    summaryEl.innerHTML =
        '<span class="ph-stat ph-correct">' + counts.correct + " correct</span>" +
        '<span class="ph-stat ph-sub">' + counts.substitution + " substitution" + (counts.substitution !== 1 ? "s" : "") + "</span>" +
        '<span class="ph-stat ph-del">' + counts.deletion + " deletion" + (counts.deletion !== 1 ? "s" : "") + "</span>" +
        '<span class="ph-stat ph-ins">' + counts.insertion + " insertion" + (counts.insertion !== 1 ? "s" : "") + "</span>" +
        (data.phone_error_rate != null ? '<span class="ph-stat ph-per">PER: ' + data.phone_error_rate + "%</span>" : "") +
        (l1Count > 0 ? '<span class="ph-stat" style="color:#b45309; background:#fef9ee;">' + l1Count + " accent</span>" : "");

    gridEl.innerHTML = data.phone_errors.map(function (pe) {
        var isL1 = pe.l1_expected && pe.error_type === "substitution";
        var cls = "ph-chip " + (isL1 ? "ph-l1-expected" : "ph-" + pe.error_type);
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
        var l1Tag = isL1 ? '<span class="ph-l1-tag">Tamil accent</span>' : '';
        return '<div class="' + cls + '">' +
            '<span class="ph-phone">' + label + "</span>" +
            (detail ? '<span class="ph-detail">' + detail + "</span>" : "") +
            l1Tag + "</div>";
    }).join("");
}

// ── Skill Bars ───────────────────────────────────────────────────────────

function renderSkillBars(bars) {
    if (!bars || bars.length === 0) return;

    for (var i = 0; i < bars.length; i++) {
        var bar = bars[i];
        var fill = document.getElementById("bar-" + bar.name);
        var starsEl = document.getElementById("stars-" + bar.name);
        if (!fill) continue;

        // Set width + color
        var pct = Math.max(0, Math.min(100, bar.value));
        fill.style.width = pct + "%";
        fill.className = "skill-fill " + (pct >= 70 ? "fill-high" : pct >= 40 ? "fill-mid" : "fill-low");

        // Stars + improvement delta
        if (starsEl) {
            var stars = bar.stars || 1;
            var starStr = "";
            for (var s = 0; s < 5; s++) {
                starStr += s < stars ? "\u2B50" : "\u2606";
            }
            // Show delta from previous recording
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

// ── Teacher Details (raw numbers) ────────────────────────────────────────

function renderTeacherDetails(data) {
    var card = document.getElementById("teacher-details-card");
    if (!card) return;
    card.style.display = "block";

    // Raw numbers
    setVal("d-wpm", fmt(data.words_per_minute));
    setVal("d-artrate", fmt(data.articulation_rate, 1) + " syll/s");
    setVal("d-mlr", fmt(data.mean_length_of_run, 1) + " words");
    setVal("d-longest", (data.longest_fluent_phrase || 0) + " words");
    setVal("d-fillers", data.filler_count != null ? data.filler_count : "--");
    setVal("d-reps", data.repetition_count != null ? data.repetition_count : "--");

    setVal("d-stress", fmtPct(data.stress_accuracy));
    setVal("d-intonation", fmtPct(data.intonation_accuracy));
    setVal("d-rhythm", fmt(data.rhythm_npvi_v, 1));
    setVal("d-pitch", fmt(data.pitch_range_st, 1) + " ST");

    setVal("d-pronscore", fmtPct(data.pronunciation_score));
    setVal("d-per", data.phone_error_rate != null ? fmt(data.phone_error_rate, 1) + "%" : "--");
    setVal("d-wer", data.wer != null ? fmt(data.wer * 100, 1) + "%" : "--");
    setVal("d-duration", data.duration_sec != null ? data.duration_sec + "s" : "--");

    setScoreColored("score-accuracy", data.accuracy);
    setScoreColored("score-fluency", data.fluency);
    setScoreColored("score-prosody", data.prosody);
    setScoreColored("score-completeness", data.completeness);

    // Teacher insights
    var tList = document.getElementById("teacher-insights-list");
    if (tList && data.insights && data.insights.teacher && data.insights.teacher.length > 0) {
        tList.innerHTML = data.insights.teacher.map(function (item) {
            return '<div class="insight-item insight-' + item.type + '">'
                + '<span class="insight-text">' + item.text + '</span>'
                + '</div>';
        }).join("");
    }
}

// ── Insights Renderer ─────────────────────────────────────────────────────

function renderInsights(insights) {
    var card = document.getElementById("insights-card");
    var list = document.getElementById("insights-list");
    if (!card || !list) return;

    var items = (insights && insights.student) || [];
    if (items.length === 0) {
        card.style.display = "none";
        return;
    }

    card.style.display = "block";
    var icons = {
        success: "&#9989;",       // green check
        encouragement: "&#128170;", // flexed bicep
        pronunciation: "&#128264;", // speaker
        accent: "&#127758;",       // globe
        fluency: "&#9200;",        // stopwatch
        prosody: "&#127925;",      // musical note
        tip: "&#128161;",          // light bulb
        words: "&#128214;",        // book
        completeness: "&#128203;", // clipboard
    };
    list.innerHTML = items.map(function (item) {
        var icon = icons[item.type] || "&#128172;"; // speech balloon default
        return '<div class="insight-item insight-' + item.type + '">'
            + '<span class="insight-icon">' + icon + '</span>'
            + '<span class="insight-text">' + item.text + '</span>'
            + '</div>';
    }).join("");
}

// ── Helpers ───────────────────────────────────────────────────────────────

function setVal(id, val) {
    var el = document.getElementById(id);
    if (el) el.textContent = val != null ? val : "--";
}

function setScoreColored(id, val) {
    var el = document.getElementById(id);
    if (!el) return;
    el.textContent = val != null ? val : "--";
    el.className = "score-value " + scoreColor(val);
}

function scoreColor(val) {
    if (val == null) return "";
    if (val >= 70) return "score-high";
    if (val >= 40) return "score-mid";
    return "score-low";
}

function verdictClass(val) {
    if (val >= 70) return "verdict-good";
    if (val >= 40) return "verdict-ok";
    return "verdict-low";
}

function fmt(val, decimals) {
    if (val == null) return "--";
    return typeof val === "number" ? val.toFixed(decimals != null ? decimals : 0) : val;
}

function fmtPct(val) {
    if (val == null) return "--";
    return Math.round(val) + "%";
}

// ── TTS Listen Button ─────────────────────────────────────────────────────

listenBtn.addEventListener("click", async function () {
    if (!currentSentence) return;

    if (ttsAudio) {
        ttsAudio.pause();
        ttsAudio.currentTime = 0;
    }

    listenBtn.textContent = "Loading...";
    listenBtn.disabled = true;

    try {
        var resp = await fetch("/api/tts?text=" + encodeURIComponent(currentSentence));
        if (resp.ok) {
            var blob = await resp.blob();
            var blobUrl = URL.createObjectURL(blob);
            ttsAudio = new Audio(blobUrl);
            ttsAudio.onended = function () {
                listenBtn.textContent = "Listen";
                listenBtn.disabled = false;
                URL.revokeObjectURL(blobUrl);
            };
            ttsAudio.onerror = function () {
                listenBtn.textContent = "Listen";
                listenBtn.disabled = false;
                speakBrowser(currentSentence);
            };
            await ttsAudio.play();
            listenBtn.textContent = "Playing...";
            return;
        }
    } catch (e) { /* fall through to browser TTS */ }

    speakBrowser(currentSentence);
});

function speakBrowser(text) {
    listenBtn.disabled = false;
    if (!window.speechSynthesis) {
        listenBtn.textContent = "Listen";
        statusText.textContent = "TTS not available on this browser.";
        return;
    }
    speechSynthesis.cancel();
    var utter = new SpeechSynthesisUtterance(text);
    utter.lang = "en-US";
    utter.rate = 0.9;
    utter.onstart = function () { listenBtn.textContent = "Playing..."; };
    utter.onend = function () { listenBtn.textContent = "Listen"; };
    utter.onerror = function () { listenBtn.textContent = "Listen"; };
    speechSynthesis.speak(utter);
}

// ── Minimal Pair Drill Mode ──────────────────────────────────────────────

var currentMpContrast = "";
var mpGenerateBtn = document.getElementById("mp-generate-btn");
var mpChips = document.querySelectorAll(".mp-chip");

// Make switchMode global
window.switchMode = function (mode) {
    var normalDiv = document.getElementById("mode-normal");
    var minimalDiv = document.getElementById("mode-minimal");
    var tabNormal = document.getElementById("tab-normal");
    var tabMinimal = document.getElementById("tab-minimal");
    if (mode === "minimal") {
        normalDiv.style.display = "none";
        minimalDiv.style.display = "block";
        tabNormal.classList.remove("active");
        tabMinimal.classList.add("active");
    } else {
        normalDiv.style.display = "block";
        minimalDiv.style.display = "none";
        tabNormal.classList.add("active");
        tabMinimal.classList.remove("active");
    }
};

for (var ci = 0; ci < mpChips.length; ci++) {
    mpChips[ci].addEventListener("click", function () {
        for (var j = 0; j < mpChips.length; j++) mpChips[j].classList.remove("selected");
        this.classList.add("selected");
        currentMpContrast = this.dataset.contrast;
        if (mpGenerateBtn) mpGenerateBtn.disabled = false;
    });
}

if (mpGenerateBtn) {
    mpGenerateBtn.addEventListener("click", async function () {
        if (!currentMpContrast) return;
        mpGenerateBtn.disabled = true;
        mpGenerateBtn.textContent = "Loading...";

        try {
            var formData = new FormData();
            formData.append("contrast", currentMpContrast);
            formData.append("difficulty", levelSelect.value === "beginner" ? "A1" : levelSelect.value === "intermediate" ? "B1" : "A2");

            var resp = await fetch("/api/minimal-pairs", { method: "POST", body: formData });
            var data = await resp.json();

            if (data.word_a && data.word_b) {
                // Show pair display
                var pairDisplay = document.getElementById("mp-pair-display");
                if (pairDisplay) pairDisplay.style.display = "flex";
                var parts = currentMpContrast.split("-");
                document.getElementById("mp-word-a").textContent = data.word_a;
                document.getElementById("mp-phone-a").textContent = "/" + (parts[0] || "") + "/";
                document.getElementById("mp-word-b").textContent = data.word_b;
                document.getElementById("mp-phone-b").textContent = "/" + (parts[1] || "") + "/";

                // Pick sentence_a as the practice sentence
                currentSentence = data.sentence_a || "Say: " + data.word_a;
                referenceText.textContent = currentSentence;
                startBtn.disabled = false;
                listenBtn.disabled = false;
                statusText.textContent = "Read the sentence aloud. Focus on the /" + (parts[0] || "") + "/ sound.";
            } else {
                statusText.textContent = "No minimal pairs found for this contrast.";
            }
        } catch (err) {
            statusText.textContent = "Failed to load minimal pair.";
        }

        mpGenerateBtn.disabled = false;
        mpGenerateBtn.textContent = "Get Minimal Pair";
    });
}

}); // end DOMContentLoaded
