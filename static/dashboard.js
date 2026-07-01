/**
 * Resume Vision - Results Dashboard Engine
 * Handles radial compliance score animations, color token mapping,
 * and key metric load states.
 */
document.addEventListener("DOMContentLoaded", () => {
    
    // 1. Radial Compliance Circle Gauge
    const gauge = document.querySelector(".gauge-progress");
    const scoreText = document.getElementById("scoreNumber");

    if (gauge && scoreText) {
        const score = parseInt(gauge.dataset.score) || 0;
        
        // Circular math for r=95
        const radius = 95;
        const circumference = 2 * Math.PI * radius; // Approx 596.9

        // Initialize state
        gauge.style.strokeDasharray = `${circumference}`;
        gauge.style.strokeDashoffset = `${circumference}`;

        // Calculate visual fill offset
        const fillOffset = circumference - (score / 100) * circumference;

        // Apply color token mapping based on alignment score
        let strokeColorVar = "var(--error)";
        if (score >= 80) {
            strokeColorVar = "var(--success)";
        } else if (score >= 60) {
            strokeColorVar = "var(--warning)";
        } else if (score >= 40) {
            strokeColorVar = "var(--accent)";
        }

        gauge.style.stroke = strokeColorVar;

        // Trigger transition loop after short paint delay
        setTimeout(() => {
            gauge.style.strokeDashoffset = `${fillOffset}`;
        }, 150);

        // Score numerical counter interpolation
        animateNumber(scoreText, 0, score, 1500);
    }

    /**
     * Smoothly interpolates an integer value inside an HTML node.
     */
    function animateNumber(element, start, end, duration) {
        if (start === end) {
            element.textContent = `${end}%`;
            return;
        }

        const range = end - start;
        let current = start;
        const increment = end > start ? 1 : -1;
        const stepTime = Math.abs(Math.floor(duration / range));
        
        const timer = setInterval(() => {
            current += increment;
            element.textContent = `${current}%`;
            
            if (current === end) {
                clearInterval(timer);
            }
        }, Math.max(stepTime, 12));
    }
});