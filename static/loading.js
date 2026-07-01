/**
 * Resume Vision - Loader Interface Manager
 * Handles the async progress messaging for the ATS evaluation process.
 */
document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    const loadingScreen = document.getElementById("loadingScreen");
    const loadingText = document.getElementById("loadingText");

    if (!form || !loadingScreen || !loadingText) return;

    const messages = [
        "PARSING RESUME STRUCTURE",
        "EXTRACTING TARGET SKILLSETS",
        "MATCHING REQUIREMENTS MATRIX",
        "GENERATING ATS SCORES",
        "COMPILING RECRUITER VERDICT"
    ];

    form.addEventListener("submit", (e) => {
        // Trigger fade-in layout
        loadingScreen.style.display = "flex";
        loadingScreen.style.opacity = "0";
        
        // Force reflow
        void loadingScreen.offsetHeight;
        
        // Transition opacity
        loadingScreen.style.transition = "opacity 0.4s cubic-bezier(0.16, 1, 0.3, 1)";
        loadingScreen.style.opacity = "1";

        let index = 0;
        loadingText.textContent = messages[0];

        const interval = setInterval(() => {
            index++;
            if (index < messages.length) {
                loadingText.textContent = messages[index];
            } else {
                clearInterval(interval);
            }
        }, 1500);
    });
});