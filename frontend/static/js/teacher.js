/**
 * teacher.js — Teacher dashboard with rich analytics.
 */

var currentClassId = null;

// Wait for auth.js to populate currentUser
(function waitForAuth() {
    var attempts = 0;
    var timer = setInterval(function () {
        attempts++;
        if (currentUser && currentUser.role === "teacher") {
            clearInterval(timer);
            initTeacher();
        } else if (currentUser && currentUser.role !== "teacher") {
            clearInterval(timer);
            document.getElementById("loading-state").textContent =
                "Access denied. This page is for teachers only.";
        } else if (attempts > 30) {
            clearInterval(timer);
            document.getElementById("loading-state").textContent =
                "Could not load user session. Please log in again.";
        }
    }, 100);
})();

async function initTeacher() {
    var classId = currentUser.class_id;
    if (!classId) {
        document.getElementById("loading-state").textContent =
            "No classroom found. Please log in again.";
        return;
    }

    currentClassId = classId;

    try {
        var results = await Promise.all([
            fetch("/api/classroom/class/" + classId).then(function (r) { return r.json(); }),
            fetch("/api/classroom/class/" + classId + "/analytics").then(function (r) { return r.json(); }),
            fetch("/api/classroom/class/" + classId + "/assignments").then(function (r) { return r.json(); }),
        ]);

        var classData = results[0];
        var analytics = results[1];
        var assignments = results[2];

        if (classData.error) {
            document.getElementById("loading-state").textContent = classData.error;
            return;
        }

        renderDashboard(classData, analytics, assignments);
    } catch (err) {
        console.error("Failed to load teacher dashboard:", err);
        document.getElementById("loading-state").textContent =
            "Failed to load data. Please refresh.";
    }
}

function renderDashboard(classData, analytics, assignments) {
    document.getElementById("loading-state").style.display = "none";
    document.getElementById("teacher-content").style.display = "";

    // Header
    document.getElementById("class-title").textContent =
        "Class: " + classData.class_name + " — " + (currentUser.display_name || "Teacher");
    document.getElementById("class-meta").textContent =
        "Class code: " + classData.class_id + "  |  Share this code with students to join.";

    // Stats
    var learners = analytics.learners || [];
    var totalRecordings = 0;
    var activeThisWeek = 0;
    var now = Date.now();
    var weekAgo = now - 7 * 24 * 60 * 60 * 1000;

    for (var i = 0; i < learners.length; i++) {
        totalRecordings += learners[i].total_recordings || 0;
        if (learners[i].last_active) {
            var lastDate = new Date(learners[i].last_active).getTime();
            if (lastDate > weekAgo) activeThisWeek++;
        }
    }

    document.getElementById("st-students").textContent = analytics.member_count || 0;
    document.getElementById("st-active").textContent = activeThisWeek;
    document.getElementById("st-avg").textContent =
        analytics.class_avg_score != null ? analytics.class_avg_score : "—";
    document.getElementById("st-recordings").textContent = totalRecordings;

    var dims = analytics.class_dim_averages || {};
    document.getElementById("st-acc").textContent = dims.accuracy != null ? dims.accuracy : "—";
    document.getElementById("st-flu").textContent = dims.fluency != null ? dims.fluency : "—";

    // Class insights
    renderClassInsights(analytics.insights || []);

    // Charts
    renderProgressChart(analytics.progress_trend || []);
    renderDimensionRadar(dims);

    // Leaderboard
    renderLeaderboard(analytics.leaderboard || []);

    // Score distribution
    renderScoreDistribution(analytics.score_distribution || {});

    // Problem sounds
    renderProblemSounds(analytics.common_problem_phonemes || []);

    // Struggling words
    renderStrugglingWords(analytics.struggling_words || []);

    // Student table (expanded)
    renderStudentTable(learners);

    // Assignments
    renderAssignments(assignments);
}

/* ── Class Insights ─────────────────────────────────────────────────── */

function renderClassInsights(insights) {
    var card = document.getElementById("class-insights-card");
    var list = document.getElementById("class-insights-list");
    if (!card || !list) return;
    if (!insights || insights.length === 0) {
        card.style.display = "none";
        return;
    }
    card.style.display = "block";
    list.innerHTML = insights.map(function (item) {
        return '<div class="insight-item insight-' + item.type + '">'
            + '<span class="insight-text">' + item.text + '</span>'
            + '</div>';
    }).join("");
}

/* ── Progress Chart (line) ──────────────────────────────────────────── */

function renderProgressChart(trend) {
    var canvas = document.getElementById("progress-chart");
    if (!canvas || !trend || trend.length === 0) return;

    new Chart(canvas, {
        type: "line",
        data: {
            labels: trend.map(function (t) { return t.date; }),
            datasets: [
                {
                    label: "Overall",
                    data: trend.map(function (t) { return t.avg_total; }),
                    borderColor: "#00c385",
                    backgroundColor: "rgba(0,195,133,0.1)",
                    fill: true,
                    tension: 0.3,
                    borderWidth: 2.5,
                    pointRadius: 3,
                },
                {
                    label: "Accuracy",
                    data: trend.map(function (t) { return t.avg_accuracy; }),
                    borderColor: "#009b6a",
                    borderWidth: 1.5,
                    pointRadius: 2,
                    tension: 0.3,
                    borderDash: [4, 2],
                },
                {
                    label: "Fluency",
                    data: trend.map(function (t) { return t.avg_fluency; }),
                    borderColor: "#96b1ac",
                    borderWidth: 1.5,
                    pointRadius: 2,
                    tension: 0.3,
                    borderDash: [4, 2],
                },
            ],
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: { beginAtZero: true, max: 100, ticks: { font: { size: 11 } } },
                x: { ticks: { font: { size: 11 } } },
            },
            plugins: {
                legend: { position: "bottom", labels: { font: { size: 11 }, boxWidth: 14 } },
                tooltip: {
                    callbacks: {
                        afterLabel: function (ctx) {
                            var t = trend[ctx.dataIndex];
                            return t ? t.recordings + " recordings" : "";
                        },
                    },
                },
            },
        },
    });
}

/* ── Dimension Radar ────────────────────────────────────────────────── */

function renderDimensionRadar(dims) {
    var canvas = document.getElementById("dimension-radar");
    if (!canvas) return;

    var labels = ["Accuracy", "Fluency", "Prosody", "Completeness"];
    var values = [
        dims.accuracy || 0,
        dims.fluency || 0,
        dims.prosody || 0,
        dims.completeness || 0,
    ];

    new Chart(canvas, {
        type: "radar",
        data: {
            labels: labels,
            datasets: [{
                label: "Class Average",
                data: values,
                backgroundColor: "rgba(0,195,133,0.18)",
                borderColor: "#00c385",
                borderWidth: 2.5,
                pointBackgroundColor: "#00c385",
                pointRadius: 4,
            }],
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                r: {
                    beginAtZero: true,
                    max: 100,
                    ticks: { stepSize: 20, font: { size: 10 } },
                    pointLabels: { font: { size: 12, weight: "bold" } },
                },
            },
            plugins: {
                legend: { display: false },
            },
        },
    });
}

/* ── Leaderboard ────────────────────────────────────────────────────── */

function renderLeaderboard(leaderboard) {
    var container = document.getElementById("leaderboard-list");
    if (!container) return;
    if (!leaderboard || leaderboard.length === 0) {
        container.innerHTML = '<p class="empty-state">No scores yet.</p>';
        return;
    }

    var html = "";
    for (var i = 0; i < leaderboard.length; i++) {
        var s = leaderboard[i];
        var rankCls = i === 0 ? "gold" : i === 1 ? "silver" : i === 2 ? "bronze" : "";
        var score = s.avg_score || 0;
        var scoreClass = score >= 70 ? "score-high" : score >= 40 ? "score-mid" : "score-low";

        html +=
            '<div class="lb-row">' +
                '<span class="lb-rank ' + rankCls + '">#' + s.rank + '</span>' +
                '<span class="lb-name">' + (s.display_name || s.learner_id) + '</span>' +
                '<div class="lb-bar-track"><div class="lb-bar-fill" style="width:' + score + '%;"></div></div>' +
                '<span class="lb-score ' + scoreClass + '">' + Math.round(score) + '</span>' +
                '<span class="lb-details">' + (s.total_recordings || 0) + ' rec</span>' +
            '</div>';
    }
    container.innerHTML = html;
}

/* ── Score Distribution ─────────────────────────────────────────────── */

function renderScoreDistribution(dist) {
    var container = document.getElementById("score-dist");
    if (!container) return;

    var buckets = ["0-20", "20-40", "40-60", "60-80", "80-100"];
    var colors = ["#ef4444", "#f97316", "#c4a800", "#4dd9a8", "#00c385"];
    var total = 0;
    for (var i = 0; i < buckets.length; i++) {
        total += dist[buckets[i]] || 0;
    }

    if (total === 0) {
        container.innerHTML = '<p class="empty-state">No score data yet.</p>';
        return;
    }

    var html = "";
    for (var i = 0; i < buckets.length; i++) {
        var count = dist[buckets[i]] || 0;
        var pct = total > 0 ? Math.round(count / total * 100) : 0;
        html +=
            '<div class="dist-row">' +
                '<span class="dist-label">' + buckets[i] + '</span>' +
                '<div class="dist-track">' +
                    '<div class="dist-fill" style="width:' + pct + '%;background:' + colors[i] + ';"></div>' +
                '</div>' +
                '<span class="dist-count">' + count + '</span>' +
            '</div>';
    }
    container.innerHTML = html;
}

/* ── Problem Sounds ─────────────────────────────────────────────────── */

function renderProblemSounds(phonemes) {
    var container = document.getElementById("problem-sounds");
    if (!phonemes || phonemes.length === 0) {
        container.innerHTML = '<p class="empty-state">No phoneme data yet. Students need to complete more recordings.</p>';
        return;
    }

    var html = "";
    for (var i = 0; i < phonemes.length; i++) {
        var p = phonemes[i];
        var pct = p.avg_score != null ? Math.round(100 - p.avg_score) : 0;
        var cls = pct >= 60 ? "high" : pct >= 40 ? "mid" : "low";
        html +=
            '<div class="sound-bar">' +
                '<span class="sound-label">/' + p.phoneme + '/</span>' +
                '<div class="sound-track">' +
                    '<div class="sound-fill ' + cls + '" style="width:' + pct + '%;"></div>' +
                '</div>' +
                '<span class="sound-pct">' + pct + '% struggling</span>' +
            '</div>';
    }
    container.innerHTML = html;

    if (phonemes.length > 0) {
        var worst = phonemes[0];
        var suggestion = document.getElementById("sound-suggestion");
        var phoneName = getPhonemeCategory(worst.phoneme);
        suggestion.textContent = "Suggestion: Plan a lesson on " + phoneName + " (/" + worst.phoneme + "/)";
        suggestion.style.display = "";
    }
}

function getPhonemeCategory(phoneme) {
    var categories = {
        "TH": "dental fricatives", "DH": "dental fricatives",
        "R": "rhotics", "L": "laterals",
        "V": "labiodental fricatives", "F": "labiodental fricatives",
        "S": "alveolar fricatives", "Z": "alveolar fricatives",
        "SH": "postalveolar fricatives", "ZH": "postalveolar fricatives",
        "CH": "affricates", "JH": "affricates",
        "NG": "velar nasals", "N": "alveolar nasals", "M": "bilabial nasals",
        "W": "approximants", "Y": "approximants",
        "P": "plosives", "B": "plosives", "T": "plosives", "D": "plosives",
        "K": "plosives", "G": "plosives",
        "AE": "front vowels", "EH": "front vowels", "IH": "front vowels",
        "AH": "central vowels", "ER": "r-colored vowels",
        "UW": "back vowels", "OW": "back vowels", "AA": "open vowels",
    };
    return categories[phoneme] || "this sound";
}

/* ── Struggling Words ───────────────────────────────────────────────── */

function renderStrugglingWords(words) {
    var container = document.getElementById("struggling-words");
    if (!container) return;
    if (!words || words.length === 0) {
        container.innerHTML = '<p class="empty-state">No word error data yet.</p>';
        return;
    }

    var html = "";
    for (var i = 0; i < words.length; i++) {
        var w = words[i];
        var pctCls = w.error_rate >= 60 ? "err-high" : w.error_rate >= 35 ? "err-mid" : "err-low";
        html +=
            '<div class="word-chip">' +
                '<strong>' + w.word + '</strong>' +
                '<span class="wc-pct ' + pctCls + '">' + w.error_rate + '% errors</span>' +
                '<span class="wc-students">' + w.student_count + ' student' + (w.student_count !== 1 ? "s" : "") + '</span>' +
            '</div>';
    }
    container.innerHTML = html;
}

/* ── Student Table (expanded with dimensions) ───────────────────────── */

function renderStudentTable(learners) {
    var tbody = document.getElementById("student-tbody");
    if (!learners || learners.length === 0) {
        tbody.innerHTML = '<tr><td colspan="10" class="empty-state">No students yet. Share the class code to invite students.</td></tr>';
        return;
    }

    // Sort by avg_score descending (best first)
    learners.sort(function (a, b) {
        return (b.avg_score || 0) - (a.avg_score || 0);
    });

    var now = Date.now();
    var weekAgo = now - 7 * 24 * 60 * 60 * 1000;

    var html = "";
    for (var i = 0; i < learners.length; i++) {
        var l = learners[i];
        var lastDate = l.last_active ? new Date(l.last_active) : null;
        var isActive = lastDate && lastDate.getTime() > weekAgo;

        html +=
            '<tr class="student-row" data-learner-id="' + l.learner_id + '" style="cursor:pointer;" title="View ' + (l.display_name || l.learner_id) + '\'s progress">' +
                "<td><strong>" + (l.display_name || l.learner_id) + "</strong></td>" +
                "<td>" + (l.level || "A1") + "</td>" +
                '<td class="' + scoreClass(l.avg_score) + '">' + fmtScore(l.avg_score) + "</td>" +
                '<td class="' + scoreClass(l.avg_accuracy) + '">' + fmtScore(l.avg_accuracy) + "</td>" +
                '<td class="' + scoreClass(l.avg_fluency) + '">' + fmtScore(l.avg_fluency) + "</td>" +
                '<td class="' + scoreClass(l.avg_prosody) + '">' + fmtScore(l.avg_prosody) + "</td>" +
                '<td class="' + scoreClass(l.avg_completeness) + '">' + fmtScore(l.avg_completeness) + "</td>" +
                "<td>" + (l.total_recordings || 0) + "</td>" +
                "<td>" + (lastDate ? lastDate.toLocaleDateString() : "—") + "</td>" +
                '<td class="' + (isActive ? "status-on" : "status-off") + '">' +
                    (isActive ? "● Active" : "○ Inactive") +
                "</td>" +
            "</tr>";
    }
    tbody.innerHTML = html;

    tbody.addEventListener("click", function (e) {
        var row = e.target.closest(".student-row");
        if (row && row.dataset.learnerId) {
            window.location.href = "/teacher/student/" + row.dataset.learnerId;
        }
    });
}

function scoreClass(val) {
    if (val == null) return "";
    return val >= 70 ? "score-high" : val >= 40 ? "score-mid" : "score-low";
}

function fmtScore(val) {
    return val != null ? Math.round(val) : "—";
}

/* ── Assignments ────────────────────────────────────────────────────── */

function renderAssignments(assignments) {
    var list = document.getElementById("assignment-list");
    if (!assignments || assignments.length === 0) {
        list.innerHTML = '<p class="empty-state">No assignments yet. Create one below.</p>';
        return;
    }

    var html = "";
    for (var i = 0; i < assignments.length; i++) {
        var a = assignments[i];
        var isOpen = a.is_open !== false;
        var statusCls = isOpen ? "open" : "closed";
        var statusText = isOpen ? "OPEN" : "CLOSED";
        var btnCls = isOpen ? "btn-sm btn-close-assign" : "btn-sm btn-open-assign";
        var btnText = isOpen ? "Close" : "Re-open";
        var btnAction = isOpen ? "closeAssignment" : "openAssignment";

        html +=
            '<div class="assignment-item">' +
                '<div class="assignment-info">' +
                    '<span class="assignment-status ' + statusCls + '">' + statusText + '</span> ' +
                    "<strong>" + a.target_level + "</strong>" +
                    (a.target_objects ? " — " + a.target_objects : "") +
                    ' <span style="color:var(--text-muted);font-size:0.8rem;">(created ' +
                        (a.created_at ? new Date(a.created_at).toLocaleDateString() : "—") +
                    ")</span>" +
                '</div>' +
                '<button class="' + btnCls + '" onclick="' + btnAction + '(' + a.id + ')">' + btnText + '</button>' +
            "</div>";
    }
    list.innerHTML = html;
}

async function closeAssignment(id) {
    try {
        await fetch("/api/classroom/assignment/" + id + "/close", { method: "POST" });
        initTeacher();
    } catch (err) {
        console.error("Failed to close assignment:", err);
    }
}

async function openAssignment(id) {
    try {
        await fetch("/api/classroom/assignment/" + id + "/open", { method: "POST" });
        initTeacher();
    } catch (err) {
        console.error("Failed to open assignment:", err);
    }
}

async function createAssignment() {
    if (!currentClassId) return alert("No class loaded.");

    var objects = document.getElementById("assign-objects").value.trim();
    var level = document.getElementById("assign-level").value;

    var form = new FormData();
    form.append("target_objects", objects);
    form.append("target_level", level);

    try {
        var res = await fetch("/api/classroom/class/" + currentClassId + "/assignment", {
            method: "POST",
            body: form,
        });
        var data = await res.json();
        if (data.assignment_id) {
            document.getElementById("assign-objects").value = "";
            initTeacher();
        }
    } catch (err) {
        console.error("Failed to create assignment:", err);
    }
}
