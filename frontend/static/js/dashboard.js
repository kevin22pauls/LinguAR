/**
 * dashboard.js — Full learner dashboard (Spec 3.7).
 *
 * Charts (all Chart.js):
 *  1. Four-dimension radar (accuracy, fluency, prosody, completeness)
 *  2. Pronunciation score trend (line)
 *  3. Sounds to practice (horizontal bar, bottom 10 phonemes)
 *  4. Fluency & prosody trend (dual-line)
 *  5. Reading speed / WPM trend (line)
 *  6. Vocabulary mastery heatmap (tile grid)
 *  7. L1 predictions vs actuals (grouped bar)
 *  8. Sessions table + metric cards + badges
 */

const COLORS = {
    primary: "#00c385",
    primaryLight: "#4dd9a8",
    success: "#00c385",
    warning: "#c4a800",
    danger: "#ef4444",
    purple: "#344b47",
    cyan: "#96b1ac",
};

// ── Main ────────────────────────────────────────────────────────────────

async function loadDashboard() {
    let data;
    try {
        const learnerId = typeof getLearnerId === "function" ? getLearnerId() : "default";
        const resp = await fetch("/api/learner/" + encodeURIComponent(learnerId) + "/dashboard");
        if (!resp.ok) return;
        data = await resp.json();
    } catch (err) {
        console.log("Dashboard data not available yet.");
        return;
    }

    const sessions = data.sessions || [];
    if (sessions.length === 0) return;

    const mc = data.metric_cards || {};
    const classAvg = data.class_averages || null;

    // Comparison cards (student vs class)
    renderCompareCards(mc, classAvg, data.class_rank, data.class_size);

    // Insights
    renderDashboardInsights(data.insights);

    // Skill bars with improvement tracking
    renderDashboardSkillBars(data.skill_bars);

    // Spaced repetition (async, non-blocking)
    fetchSpacedRepetition(data.learner_id || (typeof getLearnerId === "function" ? getLearnerId() : "default"));

    // Charts
    renderRadarChart(mc, sessions, classAvg);
    renderScoreTrend(sessions);
    renderPhonemeChart(data.phoneme_errors || []);
    renderFluencyProsodyTrend(sessions);
    renderWpmTrend(data.wpm_trend || sessions);
    renderVocabularyGrid(data.vocabulary || []);
    renderL1Chart(data.l1_predictions || []);
    renderSessionsTable(sessions);
}

// ── Comparison Cards ────────────────────────────────────────────────────

function renderCompareCards(mc, classAvg, rank, classSize) {
    var container = document.getElementById("compare-cards");
    if (!container) return;

    // If no class data, show simple metric cards instead
    if (!classAvg) {
        var metrics = [
            { label: "Avg Score", value: mc.avg_total },
            { label: "Accuracy", value: mc.avg_accuracy },
            { label: "Fluency", value: mc.avg_fluency },
            { label: "Prosody", value: mc.avg_prosody },
            { label: "Completeness", value: mc.avg_completeness },
            { label: "XP", value: mc.xp, isXp: true },
        ];
        container.innerHTML = metrics.map(function (m) {
            var val = m.value != null ? Math.round(m.value) : "—";
            var sColor = m.isXp ? "var(--primary)" : (val >= 70 ? "#00c385" : val >= 40 ? "#c4a800" : "#ef4444");
            var extra = "";
            if (m.isXp && mc.streak > 0) {
                extra = '<span class="cc-class" style="color:var(--primary);">' + mc.streak + ' day streak</span>';
            }
            return '<div class="compare-card">' +
                '<span class="cc-label">' + m.label + '</span>' +
                '<span class="cc-student" style="color:' + (typeof val === "number" ? sColor : "var(--text-muted)") + '">' + val + '</span>' +
                extra +
                '</div>';
        }).join("");
        return;
    }

    var metrics = [
        { label: "Avg Score", student: mc.avg_total, classVal: classAvg.total },
        { label: "Accuracy", student: mc.avg_accuracy, classVal: classAvg.accuracy },
        { label: "Fluency", student: mc.avg_fluency, classVal: classAvg.fluency },
        { label: "Prosody", student: mc.avg_prosody, classVal: classAvg.prosody },
        { label: "Completeness", student: mc.avg_completeness, classVal: classAvg.completeness },
    ];

    var rankPct = (rank && classSize) ? Math.round((rank / classSize) * 100) : null;
    var rankClass = rankPct != null ? (rankPct <= 33 ? "rank-top" : rankPct <= 66 ? "rank-mid" : "rank-low") : "";

    var html = "";
    if (rank && classSize) {
        html += '<div class="compare-card">' +
            '<span class="cc-label">Class Rank</span>' +
            '<span class="rank-badge ' + rankClass + '">#' + rank + ' of ' + classSize + '</span>' +
            '</div>';
    }
    // XP + streak card
    if (mc.xp) {
        html += '<div class="compare-card">' +
            '<span class="cc-label">XP</span>' +
            '<span class="cc-student" style="color:var(--primary);">' + mc.xp + '</span>' +
            (mc.streak > 0 ? '<span class="cc-class" style="color:var(--primary);">' + mc.streak + ' day streak</span>' : '') +
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
        var sColor = sVal >= 70 ? "#009b6a" : sVal >= 40 ? "#c4a800" : "#ef4444";

        html += '<div class="compare-card">' +
            '<span class="cc-label">' + m.label + '</span>' +
            '<span class="cc-student" style="color:' + sColor + '">' + Math.round(sVal) + '</span>' +
            '<span class="cc-class">Class avg: ' + Math.round(cVal) + '</span>' +
            '<span class="cc-diff ' + diffClass + '">' + diffText + '</span>' +
            '</div>';
    }
    container.innerHTML = html;
}

// ── 1. Radar Chart ──────────────────────────────────────────────────────

function renderRadarChart(mc, sessions, classAvg) {
    const ctx = document.getElementById("radar-chart");
    if (!ctx) return;

    const latest = sessions[sessions.length - 1] || {};

    var datasets = [
        {
            label: "Latest",
            data: [latest.accuracy || 0, latest.fluency || 0, latest.prosody || 0, latest.completeness || 0],
            borderColor: COLORS.primary,
            backgroundColor: "rgba(0,195,133,0.15)",
            borderWidth: 2,
            pointRadius: 4,
        },
        {
            label: "Your Average",
            data: [mc.avg_accuracy || 0, mc.avg_fluency || 0, mc.avg_prosody || 0, mc.avg_completeness || 0],
            borderColor: COLORS.primaryLight,
            backgroundColor: "rgba(77,217,168,0.08)",
            borderWidth: 2,
            borderDash: [4, 4],
            pointRadius: 3,
        },
    ];

    if (classAvg) {
        datasets.push({
            label: "Class Average",
            data: [classAvg.accuracy || 0, classAvg.fluency || 0, classAvg.prosody || 0, classAvg.completeness || 0],
            borderColor: "#96b1ac",
            backgroundColor: "rgba(150,177,172,0.08)",
            borderWidth: 2,
            borderDash: [6, 3],
            pointRadius: 3,
        });
    }

    new Chart(ctx, {
        type: "radar",
        data: {
            labels: ["Accuracy", "Fluency", "Prosody", "Completeness"],
            datasets: datasets,
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                r: { min: 0, max: 100, ticks: { stepSize: 25, font: { size: 10 } } },
            },
            plugins: { legend: { position: "bottom", labels: { font: { size: 11 } } } },
        },
    });
}

// ── 2. Score Trend ──────────────────────────────────────────────────────

function renderScoreTrend(sessions) {
    const ctx = document.getElementById("score-trend-chart");
    if (!ctx) return;

    new Chart(ctx, {
        type: "line",
        data: {
            labels: sessions.map((s) => s.date),
            datasets: [
                { label: "Accuracy", data: sessions.map((s) => s.accuracy), borderColor: COLORS.primary, tension: 0.3, borderWidth: 2, pointRadius: 2 },
                { label: "Fluency", data: sessions.map((s) => s.fluency), borderColor: COLORS.success, tension: 0.3, borderWidth: 2, pointRadius: 2 },
                { label: "Prosody", data: sessions.map((s) => s.prosody), borderColor: COLORS.warning, tension: 0.3, borderWidth: 2, pointRadius: 2 },
                { label: "Total", data: sessions.map((s) => s.total), borderColor: COLORS.purple, tension: 0.3, borderWidth: 2.5, pointRadius: 2 },
            ],
        },
        options: lineChartOpts(0, 100, "bottom"),
    });
}

// ── 3. Sounds to Practice ───────────────────────────────────────────────

function renderPhonemeChart(phonemeErrors) {
    const ctx = document.getElementById("phoneme-chart");
    if (!ctx) return;

    if (phonemeErrors.length === 0) {
        const sub = ctx.parentElement.previousElementSibling;
        if (sub) sub.textContent = "No phoneme data yet. Record more sessions.";
        return;
    }

    const bottom10 = phonemeErrors.slice(0, 10);
    // Labels show phoneme + most common substitution if available
    const labels = bottom10.map(function (p) {
        var label = "/" + p.phoneme + "/";
        if (p.top_sub) label += " \u2192 /" + p.top_sub + "/";
        return label;
    });
    const accs = bottom10.map((p) => p.accuracy);
    // Color by FL weight: high FL errors get red, low FL get amber, no FL data uses accuracy
    const bgColors = bottom10.map(function (p) {
        if (p.fl != null && p.fl >= 0.5) return COLORS.danger;
        if (p.fl != null && p.fl > 0) return COLORS.warning;
        return p.accuracy < 40 ? COLORS.danger : p.accuracy < 70 ? COLORS.warning : COLORS.success;
    });

    new Chart(ctx, {
        type: "bar",
        data: {
            labels,
            datasets: [{ label: "Accuracy %", data: accs, backgroundColor: bgColors, borderRadius: 4 }],
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
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

// ── 4. Fluency & Prosody Trend ──────────────────────────────────────────

function renderFluencyProsodyTrend(sessions) {
    const ctx = document.getElementById("fluency-prosody-chart");
    if (!ctx) return;

    new Chart(ctx, {
        type: "line",
        data: {
            labels: sessions.map((s) => s.date),
            datasets: [
                { label: "Fluency", data: sessions.map((s) => s.fluency), borderColor: COLORS.success, tension: 0.3, borderWidth: 2, pointRadius: 2 },
                { label: "Prosody", data: sessions.map((s) => s.prosody), borderColor: COLORS.warning, tension: 0.3, borderWidth: 2, pointRadius: 2 },
            ],
        },
        options: lineChartOpts(0, 100, "bottom"),
    });
}

// ── 5. WPM Trend ────────────────────────────────────────────────────────

function renderWpmTrend(wpmData) {
    const ctx = document.getElementById("wpm-chart");
    if (!ctx) return;

    const filtered = wpmData.filter((d) => d.wpm > 0);
    if (filtered.length === 0) return;

    new Chart(ctx, {
        type: "line",
        data: {
            labels: filtered.map((d) => d.date),
            datasets: [{
                label: "WPM",
                data: filtered.map((d) => d.wpm),
                borderColor: COLORS.cyan,
                tension: 0.3,
                borderWidth: 2,
                pointRadius: 2,
                fill: true,
                backgroundColor: "rgba(6,182,212,0.08)",
            }],
        },
        options: lineChartOpts(0, null, false),
    });
}

// ── 6. Vocabulary Mastery Grid ──────────────────────────────────────────

function renderVocabularyGrid(vocab) {
    const container = document.getElementById("vocab-grid");
    if (!container || vocab.length === 0) return;

    container.innerHTML = vocab.map((v) => {
        let cls = "new";
        if (v.avg_score >= 80) cls = "mastered";
        else if (v.avg_score >= 50) cls = "learning";
        else if (v.times_practiced > 0) cls = "struggling";

        return '<span class="vocab-tile ' + cls + '" title="' + v.word + ": " + v.avg_score + "% (" + v.times_practiced + 'x)">' + v.word + "</span>";
    }).join("");
}

// ── 7. L1 Predictions vs Actuals ────────────────────────────────────────

function renderL1Chart(predictions) {
    if (predictions.length === 0) return;

    const card = document.getElementById("l1-card");
    if (card) card.style.display = "block";

    const ctx = document.getElementById("l1-chart");
    if (!ctx) return;

    const filtered = predictions.filter((p) => p.predicted_difficult);
    if (filtered.length === 0) return;

    const labels = filtered.map((p) => "/" + p.phoneme + "/");

    new Chart(ctx, {
        type: "bar",
        data: {
            labels,
            datasets: [
                {
                    label: "Predicted Difficulty",
                    data: filtered.map(() => 100),
                    backgroundColor: "rgba(168,85,247,0.25)",
                    borderColor: COLORS.purple,
                    borderWidth: 1,
                    borderRadius: 4,
                },
                {
                    label: "Actual Accuracy",
                    data: filtered.map((p) => p.actual_accuracy || 0),
                    backgroundColor: filtered.map((p) =>
                        (p.actual_accuracy || 0) < 60 ? COLORS.danger : COLORS.success
                    ),
                    borderRadius: 4,
                },
            ],
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: { y: { min: 0, max: 100 } },
            plugins: { legend: { position: "bottom", labels: { font: { size: 11 } } } },
        },
    });
}

// ── 8. Sessions Table ───────────────────────────────────────────────────

function renderSessionsTable(sessions) {
    const tbody = document.getElementById("sessions-tbody");
    if (!tbody || sessions.length === 0) return;

    const recent = sessions.slice(-20).reverse();

    tbody.innerHTML = recent.map((s) =>
        '<tr class="session-row" data-id="' + s.id + '" style="cursor:pointer;" title="View details">' +
            "<td>" + s.date + "</td>" +
            "<td>" + (s.object || "Free") + "</td>" +
            '<td class="' + scoreClass(s.accuracy) + '">' + s.accuracy + "</td>" +
            '<td class="' + scoreClass(s.fluency) + '">' + s.fluency + "</td>" +
            '<td class="' + scoreClass(s.prosody) + '">' + s.prosody + "</td>" +
            '<td class="' + scoreClass(s.completeness) + '">' + s.completeness + "</td>" +
            '<td style="font-weight:700;color:var(--primary);">' + s.total + "</td>" +
        "</tr>"
    ).join("");

    // Click handler: navigate to exercise detail page
    tbody.addEventListener("click", function (e) {
        const row = e.target.closest(".session-row");
        if (row && row.dataset.id) {
            window.location.href = "/exercise/" + row.dataset.id;
        }
    });
}

// ── Dashboard Skill Bars ─────────────────────────────────────────────

function renderDashboardSkillBars(bars) {
    var card = document.getElementById("dashboard-skill-bars-card");
    if (!card || !bars || bars.length === 0) return;
    card.style.display = "block";

    for (var i = 0; i < bars.length; i++) {
        var bar = bars[i];
        var fill = document.getElementById("db-bar-" + bar.name);
        var starsEl = document.getElementById("db-stars-" + bar.name);
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

// ── 9. Spaced Repetition ────────────────────────────────────────────────

async function fetchSpacedRepetition(learnerId) {
    try {
        var resp = await fetch("/api/learner/" + encodeURIComponent(learnerId) + "/due-phonemes");
        if (!resp.ok) return;
        var data = await resp.json();
        renderSpacedRepetition(data.due || [], data.all_schedules || []);
    } catch (err) {
        // Silently skip if endpoint not available
    }
}

function renderSpacedRepetition(due, allSchedules) {
    var card = document.getElementById("spaced-rep-card");
    if (!card) return;
    if (due.length === 0 && allSchedules.length === 0) return;

    card.style.display = "block";
    var dueEl = document.getElementById("due-phonemes");
    var scheduleEl = document.getElementById("phoneme-schedule");

    // Due phonemes chips
    if (dueEl) {
        if (due.length === 0) {
            dueEl.innerHTML = '<p style="color:var(--text-muted); font-size:0.9rem;">All caught up! No phonemes due for review.</p>';
        } else {
            dueEl.innerHTML = due.map(function (p) {
                var overdue = p.days_overdue > 0 ? " overdue" : "";
                var meta = p.days_overdue > 0 ? p.days_overdue + "d overdue" : "Due today";
                if (p.last_score != null) meta += " | " + Math.round(p.last_score) + "%";
                return '<div class="due-chip' + overdue + '">' +
                    '<span class="due-phone">/' + p.phoneme + '/</span>' +
                    '<span class="due-meta">' + meta + '</span>' +
                    '</div>';
            }).join("");
        }
    }

    // Schedule overview (top 15)
    if (scheduleEl && allSchedules.length > 0) {
        var top = allSchedules.slice(0, 15);
        scheduleEl.innerHTML = '<h3 style="font-size:0.95rem; font-weight:700; margin-bottom:0.5rem;">Review Schedule</h3>' +
            top.map(function (s) {
                var mastery = s.mastery != null ? Math.max(0, Math.min(100, s.mastery)) : 0;
                var fillColor = mastery >= 70 ? "#00c385" : mastery >= 40 ? "#c4a800" : "#ef4444";
                var statusText = s.status === "overdue" ? "Overdue" : "Next: " + (s.due_date || "—");
                return '<div class="schedule-row">' +
                    '<span class="schedule-phone">/' + s.phoneme + '/</span>' +
                    '<div class="schedule-mastery"><div class="schedule-mastery-fill" style="width:' + mastery + '%; background:' + fillColor + ';"></div></div>' +
                    '<span class="schedule-info">' + statusText + '</span>' +
                    '</div>';
            }).join("");
    }
}

// ── Helpers ─────────────────────────────────────────────────────────────

function renderDashboardInsights(insights) {
    var card = document.getElementById("dashboard-insights-card");
    var list = document.getElementById("dashboard-insights-list");
    if (!card || !list) return;

    var items = (insights && insights.student) || [];
    if (items.length === 0) {
        card.style.display = "none";
        return;
    }

    card.style.display = "block";
    var icons = {
        success: "&#9989;", encouragement: "&#128170;",
        pronunciation: "&#128264;", accent: "&#127758;",
        fluency: "&#9200;", prosody: "&#127925;",
        tip: "&#128161;", words: "&#128214;",
        completeness: "&#128203;",
    };
    list.innerHTML = items.map(function (item) {
        var icon = icons[item.type] || "&#128172;";
        return '<div class="insight-item insight-' + item.type + '">'
            + '<span class="insight-icon">' + icon + '</span>'
            + '<span class="insight-text">' + item.text + '</span>'
            + '</div>';
    }).join("");
}

function scoreClass(val) {
    if (val >= 70) return "score-high";
    if (val >= 40) return "score-mid";
    return "score-low";
}

function lineChartOpts(min, max, legendPos) {
    return {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            y: { min: min, max: max || undefined },
            x: { ticks: { maxTicksLimit: 8, font: { size: 10 } } },
        },
        plugins: {
            legend: legendPos
                ? { position: legendPos, labels: { font: { size: 11 }, boxWidth: 12 } }
                : { display: false },
        },
    };
}

// ── Init ────────────────────────────────────────────────────────────────

// Wait for auth.js to finish resolving currentUser before loading
if (typeof authReady !== "undefined") {
    authReady.then(loadDashboard);
} else {
    loadDashboard();
}
