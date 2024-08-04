const services = [
    "A promising UI/UX design?...",
    "A flexible developed web interface?...",
    "Splendid Quality Assurance?...",
    "A long-term contract or collaboration with a seasoned professional?..."
];

let serviceIndex = 0;
let isAnimating = false;

function changeServiceText() {
            if (!isAnimating) {
                isAnimating = true;
                const text = document.getElementById("service-text");
                const service = services[serviceIndex];
                const length = service.length;
                let currentLength = 0;
                const typingInterval = setInterval(() => {
                        if (currentLength === length) {
                            clearInterval(typingInterval);
                            setTimeout(() => {
                                    isAnimating = false;
                                    deleteText();
                                },
                                2000);
                        } else {
                            text.textContent = service.slice(0, currentLength + 1);
                            currentLength++;
                        }
                    },
                    100);
                serviceIndex = (serviceIndex + 1) % services.length;
            }
        }

        function deleteText() {
            const text = document.getElementById("service-text");
            let length = text.textContent.length;
            const interval = setInterval(() => {
                    if (length === 0) {
                        clearInterval(interval);
                        changeServiceText();
                    } else {
                        text.textContent = text.textContent.slice(0, -1);
                        length--;
                    }
                },
                50);
        }
        changeServiceText();

$(document).ready(function() {
    // Initialize Waypoints and Counter-Up
    var counterTriggered = false; // Add a flag to check if counter has already been triggered

    $('.cta-section').waypoint(function(direction) {
        if (!counterTriggered && direction === 'down') {
            $('.counter').counterUp({
                delay: 10, // the delay time in ms
                time: 3000 // the speed time in ms
            });
            counterTriggered = true; // Set the flag to true
            this.destroy(); // Trigger only once
        }
    }, { offset: '75%' });
});

