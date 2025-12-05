document.addEventListener("DOMContentLoaded", () => {

    const form = document.querySelector("form");
    const durationInput = document.querySelector("input[name='Duration'], input[name='Duration_min']");
    const themeToggle = document.getElementById("themeToggle");

    // 1. Apply saved theme on load
    applySavedTheme();
    updateThemeBtn();

    // 2. Form validation (only if form exists)
    if (form && durationInput) {
        form.addEventListener("submit", (e) => {
            const value = durationInput.value.trim();

            // For index page (Duration_min — number only)
            if (durationInput.name === "Duration_min") {
                if (value === "" || isNaN(value) || Number(value) <= 0) {
                    alert("Enter a valid duration in minutes.");
                    e.preventDefault();
                    return;
                }
            }

            // For time-format version (Duration)
            if (durationInput.name === "Duration") {
                const pattern = /^(\d+h\s?\d*m?$|\d+h$|\d+m$)/i;
                if (!pattern.test(value)) {
                    alert("Duration must be: 2h 30m, 2h, or 30m.");
                    e.preventDefault();
                    return;
                }
            }

            showLoader();
        });

        // Auto-fix spacing (only if this input exists)
        durationInput.addEventListener("blur", () => {
            let v = durationInput.value.trim().toLowerCase();
            v = v.replace(/(\d+h)(\d)/, "$1 $2");
            durationInput.value = v;
        });
    }

    // 3. Theme toggle
    themeToggle.addEventListener("click", () => {
        document.body.classList.toggle("dark");
        localStorage.setItem("theme",
            document.body.classList.contains("dark") ? "dark" : "light"
        );
        updateThemeBtn();
    });

});


// -----------------------
// THEME HELPERS
// -----------------------

function applySavedTheme() {
    if (localStorage.getItem("theme") === "dark") {
        document.body.classList.add("dark");
    }
}

function updateThemeBtn() {
    const btn = document.getElementById("themeToggle");
    if (!btn) return;

    btn.textContent = document.body.classList.contains("dark") ? "☀" : "🌙";
}


// -----------------------
// LOADING OVERLAY
// -----------------------

function showLoader() {
    let box = document.createElement("div");
    box.className = "loader-box";
    box.innerHTML = `<div class="spinner"></div><p>Analyzing...</p>`;
    document.body.appendChild(box);
}
