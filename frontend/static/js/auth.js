/**
 * auth.js — shared auth utilities.
 * Loaded on every page via base.html.
 * Redirects to /login if no session. Exposes currentUser globally.
 *
 * Uses sessionStorage to ensure login is required every time a new
 * tab/window is opened (sessionStorage is per-tab and cleared on close).
 *
 * Other scripts should call: authReady.then(function() { ... })
 * to wait for auth to finish before using currentUser / getLearnerId().
 */

var currentUser = null;

var _authResolve;
var authReady = new Promise(function (resolve) { _authResolve = resolve; });

(async function checkAuth() {
    // Login page should not redirect
    if (window.location.pathname === "/login") {
        _authResolve();
        return;
    }

    // If this tab hasn't logged in yet, force login
    if (!sessionStorage.getItem("linguar_authed")) {
        try { await fetch("/api/auth/logout", { method: "POST" }); } catch (e) {}
        window.location.href = "/login";
        return;
    }

    try {
        var resp = await fetch("/api/auth/me");
        var data = await resp.json();

        if (!data.logged_in) {
            sessionStorage.removeItem("linguar_authed");
            window.location.href = "/login";
            return;
        }

        currentUser = data;

        // Update nav with user info
        var navInner = document.querySelector(".nav-inner");
        if (navInner) {
            // Teacher role: replace student nav with teacher nav
            if (data.role === "teacher") {
                var navLinks = navInner.querySelector(".nav-links");
                if (navLinks) {
                    navLinks.innerHTML =
                        '<a href="/teacher"' + (window.location.pathname === "/teacher" ? ' class="active"' : '') + '>Teacher Dashboard</a>';
                }
            }

            var userEl = document.createElement("div");
            userEl.className = "nav-user";
            userEl.innerHTML =
                '<span class="nav-user-name">' + data.display_name + '</span>' +
                '<span class="nav-user-room">' + data.classroom + '</span>' +
                '<a href="#" class="nav-logout" onclick="logout()">Logout</a>';
            navInner.appendChild(userEl);
        }
    } catch (e) {
        // Server not reachable — don't redirect, let page work offline
    }

    _authResolve();
})();

async function logout() {
    try {
        await fetch("/api/auth/logout", { method: "POST" });
    } catch (e) {}
    currentUser = null;
    sessionStorage.removeItem("linguar_authed");
    window.location.href = "/login";
}

function getLearnerId() {
    if (currentUser) return currentUser.learner_id;
    return "default";
}
