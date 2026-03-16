/**
 * student_detail.js — Teacher's view of a single student's progress.
 * Shows student dashboard with class comparison overlays.
 */

var COLORS = {
    primary: "#00c385",
    primaryLight: "#4dd9a8",
    success: "#00c385",
    warning: "#c4a800",
    danger: "#ef4444",
    purple: "#344b47",
    cyan: "#96b1ac",
    classAvg: "#96b1ac",
};

// Wait for auth, then load
if (typeof authReady !== "undefined") {
    authReady.then(loadStudentDetail);
} else {
    loadStudentDetail();
}

async function loadStudentDetail() {
    if (!currentUser || currentUser.role !== "teacher") {
        document.getElementById("loading-state").textContent = "Access denied. Teachers only.";
        return;
    }

    var classId = currentUser.class_id;
    if (!classId) {
        document.getElementById("loading-state").textContent = "No classroom found.";
        return;
    }

    try {
        var resp = await fetch(
            "/api/classroom/class/" + classId + "/student/" + encodeURIComponent(STUDENT_LEARNER_ID)
        );
        var data = await resp.json();

        if (data.error) {
            document.getElementById("loading-state").textContent = data.error;
            return;
        }

        renderStudentDetail(data);
    } catch (err) {
        console.error("Failed to load student data:", err);
        document.getElementById("loading-state").textContent = "Failed to load data. Please refresh.";
    }
}

function renderStudentDetail(data) {
    document.getElementById("loading-state").style.display = "none";
    document.getElementById("student-content").style.display = "";

    var profile = data.profile || {};
    var sessions = data.sessions || [];
    var classAvg = data.class_averages || {};
    var mc = data.metric_cards || {};

    // Header
    document.getElementById("student-name").textContent = profile.display_name || STUDENT_LEARNER_ID;
    var metaParts = [];
    metaParts.push("Level: " + (profile.level || "A1"));
    metaParts.push(sessions.length + " recordings");
    if (data.class_rank && data.class_size) {
        metaParts.push("Rank: #" + data.class_rank + " of " + data.class_size);
    }
    document.getElementById("student-meta").textContent = metaParts.join("  |  ");

    // Comparison cards
    renderCompareCards(mc, classAvg, data.class_rank, data.class_size);

    // Skill bars
    renderSkillBars(data.skill_bars);

    // Insights
    renderInsights(data.insights);

    // Charts
    if (sessions.length > 0) {
        renderRadar(mc, classAvg, sessions);
        renderScoreTrend(sessions);
    }

    renderPhonemeChart(data.phoneme_errors || []);
    renderVocabGrid(data.vocabulary || []);
    renderSessionsTable(sessions);
}

// ── Comparison Cards ──────────────────────────────────────────────────

function renderCompareCards(mc, classAvg, rank, classSize) {
    var container = document.getElementById("compare-cards");
    var metrics = [
        { label: "Avg Score", student: mc.avg_total, classVal: classAvg.total },
        { label: "Accuracy", student: mc.avg_accuracy, classVal: classAvg.accuracy },
        { label: "Fluency", student: mc.avg_fluency, classVal: classAvg.fluency },
        { label: "Prosody", student: mc.avg_prosody, classVal: classAvg.prosody },
        { label: "Completeness", student: mc.avg_completeness, classVal: classAvg.completeness },
    ];

    // Add rank card
    var rankPct = (rank && classSize) ? Math.round((rank / classSize) * 100) : null;
    var rankClass = rankPct != null ? (rankPct <= 33 ? "rank-top" : rankPct <= 66 ? "rank-mid" : "rank-low") : "";

    var html = "";
    if (rank && classSize) {
        html += '<div class="compare-card">' +
            '<span class="cc-label">Class Rank</span>' +
            '<span class="rank-badge ' + rankClass + '">#' + rank + ' of ' + classSize + '</span>' +
            '</div>';
    }

    for (var i = 0; i < metrics.length; i++) {
        var m = metrics[i];
        var sVal = m.student != null ? m.student : 0;
        var cVal = m.classVal != null ? m.classVal : 0;
        var diff = sVal - cVal;
        var diffClass = diff > 2 ? "above" : diff < -2 ? "below" : "same";
        var diffText = diff > 0 ? "+" + Math.round(diff) + " above class" :
                       diff < 0 ? Math.round(diff) + " below class" : "= class average";
        var sColor = sVal >= 70 ? "#00c385" : sVal >= 40 ? "#c4a800" : "#ef4444";

        html += '<div class="compare-card">' +
            '<span class="cc-label">' + m.label + '</span>' +
            '<span class="cc-student" style="color:' + sColor + '">' + Math.round(sVal) + '</span>' +
            '<span class="cc-class">Class avg: ' + Math.round(cVal) + '</span>' +
            '<span class="cc-diff ' + diffClass + '">' + diffText + '</span>' +
            '</div>';
    }
    container.innerHTML = html;
}

// ── Skill Bars ───────────────────────────────────────────────────────

function renderSkillBars(bars) {
    var card = document.getElementById("sd-skill-bars-card");
    if (!card || !bars || bars.length === 0) return;
    card.style.display = "block";

    for (var i = 0; i < bars.length; i++) {
        var bar = bars[i];
        var fill = document.getElementById("sd-bar-" + bar.name);
        var starsEl = document.getElementById("sd-stars-" + bar.name);
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

// ── Insights ─────────────────────────────────────────────────────────

function renderInsights(insights) {
    var card = document.getElementById("sd-insights-card");
    if (!card || !insights) return;

    var studentItems = (insights.student || []);
    var teacherItems = (insights.teacher || []);

    if (studentItems.length === 0 && teacherItems.length === 0) return;
    card.style.display = "block";

    var icons = {
        success: "&#9989;", encouragement: "&#128170;",
        pronunciation: "&#128264;", accent: "&#127758;",
        fluency: "&#9200;", prosody: "&#127925;",
        tip: "&#128161;", words: "&#128214;",
        completeness: "&#128203;", diagnostic: "&#128269;",
        progress: "&#128200;", l1_transfer: "&#127758;",
    };

    function renderItems(items, containerId) {
        var el = document.getElementById(containerId);
        if (!el) return;
        el.innerHTML = items.map(function (item) {
            var icon = icons[item.type] || "&#128172;";
            return '<div class="insight-item insight-' + item.type + '">' +
                '<span class="insight-icon">' + icon + '</span>' +
                '<span class="insight-text">' + item.text + '</span>' +
                '</div>';
        }).join("");
    }

    renderItems(studentItems, "sd-insights-student");
    renderItems(teacherItems, "sd-insights-teacher");
}

// ── Radar Chart (student vs class avg) ───────────────────────────────

function renderRadar(mc, classAvg, sessions) {
    var ctx = document.getElementById("sd-radar-chart");
    if (!ctx) return;

    var latest = sessions[sessions.length - 1] || {};

    new Chart(ctx, {
        type: "radar",
        data: {
            labels: ["Accuracy", "Fluency", "Prosody", "Completeness"],
            datasets: [
                {
                    label: "Student (Latest)",
                    data: [latest.accuracy || 0, latest.fluency || 0, latest.prosody || 0, latest.completeness || 0],
                    borderColor: COLORS.primary,
                    backgroundColor: "rgba(0,195,133,0.15)",
                    borderWidth: 2,
                    pointRadius: 4,
                },
                {
                    label: "Student (Average)",
                    data: [mc.avg_accuracy || 0, mc.avg_fluency || 0, mc.avg_prosody || 0, mc.avg_completeness || 0],
                    borderColor: COLORS.primaryLight,
                    backgroundColor: "rgba(77,217,168,0.08)",
                    borderWidth: 2,
                    borderDash: [4, 4],
                    pointRadius: 3,
                },
                {
                    label: "Class Average",
                    data: [classAvg.accuracy || 0, classAvg.fluency || 0, classAvg.prosody || 0, classAvg.completeness || 0],
                    borderColor: COLORS.classAvg,
                    backgroundColor: "rgba(150,177,172,0.08)",
                    borderWidth: 2,
                    borderDash: [6, 3],
                    pointRadius: 3,
                },
            ],
        },
        options: {
            responsive: true, maintainAspectRatio: false,
            scales: { r: { min: 0, max: 100, ticks: { stepSize: 25, font: { size: 10 } } } },
            plugins: { legend: { position: "bottom", labels: { font: { size: 11 } } } },
        },
    });
}

// ── Score Trend ──────────────────────────────────────────────────────

function renderScoreTrend(sessions) {
    var ctx = document.getElementById("sd-score-trend");
    if (!ctx || sessions.length === 0) return;

    new Chart(ctx, {
        type: "line",
        data: {
            labels: sessions.map(function (s) { return s.date; }),
            datasets: [
                { label: "Accuracy", data: sessions.map(function (s) { return s.accuracy; }), borderColor: COLORS.primary, tension: 0.3, borderWidth: 2, pointRadius: 2 },
                { label: "Fluency", data: sessions.map(function (s) { return s.fluency; }), borderColor: COLORS.success, tension: 0.3, borderWidth: 2, pointRadius: 2 },
                { label: "Prosody", data: sessions.map(function (s) { return s.prosody; }), borderColor: COLORS.warning, tension: 0.3, borderWidth: 2, pointRadius: 2 },
                { label: "Total", data: sessions.map(function (s) { return s.total; }), borderColor: COLORS.purple, tension: 0.3, borderWidth: 2.5, pointRadius: 2 },
            ],
        },
        options: {
            responsive: true, maintainAspectRatio: false,
            scales: { y: { min: 0, max: 100 }, x: { ticks: { maxTicksLimit: 8, font: { size: 10 } } } },
            plugins: { legend: { position: "bottom", labels: { font: { size: 11 }, boxWidth: 12 } } },
        },
    });
}

// ── Phoneme Chart ────────────────────────────────────────────────────

function renderPhonemeChart(phonemeErrors) {
    var ctx = document.getElementById("sd-phoneme-chart");
    if (!ctx || phonemeErrors.length === 0) return;

    var bottom10 = phonemeErrors.slice(0, 10);
    var labels = bottom10.map(function (p) {
        var label = "/" + p.phoneme + "/";
        if (p.top_sub) label += " \u2192 /" + p.top_sub + "/";
        return label;
    });
    var accs = bottom10.map(function (p) { return p.accuracy; });
    var bgColors = bottom10.map(function (p) {
        if (p.fl != null && p.fl >= 0.5) return COLORS.danger;
        if (p.fl != null && p.fl > 0) return COLORS.warning;
        return p.accuracy < 40 ? COLORS.danger : p.accuracy < 70 ? COLORS.warning : COLORS.success;
    });

    new Chart(ctx, {
        type: "bar",
        data: {
            labels: labels,
            datasets: [{ label: "Accuracy %", data: accs, backgroundColor: bgColors, borderRadius: 4 }],
        },
        options: {
            responsive: true, maintainAspectRatio: false,
            indexAxis: "y",
            scales: { x: { min: 0, max: 100 } },
            plugins: {
                legend: { display: false },
                tooltip: {
                    callbacks: {
                        afterLabel: function (ctx) {
                            var p = bottom10[ctx.dataIndex];
                            var parts = [];
                            if (p.error_count) parts.push(p.error_count + " errors");
                            if (p.fl != null) parts.push("FL: " + p.fl + (p.fl >= 0.5 ? " (high impact)" : " (low impact)"));
                            return parts.join(" | ");
                        }
                    }
                }
            },
        },
    });
}

// ── Vocabulary Grid ──────────────────────────────────────────────────

function renderVocabGrid(vocab) {
    var container = document.getElementById("sd-vocab-grid");
    if (!container || vocab.length === 0) return;

    container.innerHTML = vocab.map(function (v) {
        var cls = "new";
        if (v.avg_score >= 80) cls = "mastered";
        else if (v.avg_score >= 50) cls = "learning";
        else if (v.times_practiced > 0) cls = "struggling";
        return '<span class="vocab-tile ' + cls + '" title="' + v.word + ': ' + v.avg_score + '% (' + v.times_practiced + 'x)">' + v.word + '</span>';
    }).join("");
}

// ── Sessions Table ───────────────────────────────────────────────────

function renderSessionsTable(sessions) {
    var tbody = document.getElementById("sd-sessions-tbody");
    if (!tbody || sessions.length === 0) return;

    var recent = sessions.slice(-20).reverse();

    function scoreClass(val) {
        if (val >= 70) return "score-high";
        if (val >= 40) return "score-mid";
        return "score-low";
    }

    tbody.innerHTML = recent.map(function (s) {
        return '<tr class="session-row" data-id="' + s.id + '" style="cursor:pointer;" title="View details">' +
            "<td>" + s.date + "</td>" +
            "<td>" + (s.object || "Free") + "</td>" +
            '<td class="' + scoreClass(s.accuracy) + '">' + s.accuracy + "</td>" +
            '<td class="' + scoreClass(s.fluency) + '">' + s.fluency + "</td>" +
            '<td class="' + scoreClass(s.prosody) + '">' + s.prosody + "</td>" +
            '<td class="' + scoreClass(s.completeness) + '">' + s.completeness + "</td>" +
            '<td style="font-weight:700;color:var(--primary);">' + s.total + "</td>" +
            "</tr>";
    }).join("");

    tbody.addEventListener("click", function (e) {
        var row = e.target.closest(".session-row");
        if (row && row.dataset.id) {
            window.location.href = "/exercise/" + row.dataset.id;
        }
    });
}
