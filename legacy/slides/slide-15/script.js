// Slide 15: Progressive RAG Demo Animation

// Progressive demo state for slide-15 (exposed to window for navigation.js)
window.ragAnimationStep = 0;
window.maxRagSteps = 4;

// Progressive Demo Controller for Slide 15 (exposed to window for navigation.js)
window.triggerNextRagAnimation = function() {
    // Only handle if we're on slide 15
    const currentSlideElement = document.querySelector('.slide-15.active');
    if (!currentSlideElement) return false;

    if (window.ragAnimationStep < window.maxRagSteps) {
        window.ragAnimationStep++;
        showProgressiveStep(window.ragAnimationStep);
        return true; // Handled, don't advance slide
    }

    // All steps completed - reset and allow advance
    window.ragAnimationStep = 0;
    return false; // Not handled, allow slide advance
};

function showProgressiveStep(step) {
    const element = document.getElementById(`demo-step-${step}`);
    if (element) {
        element.classList.add('show');

        // Smooth scroll to keep the new element in view
        setTimeout(() => {
            element.scrollIntoView({
                behavior: 'smooth',
                block: 'center',
                inline: 'nearest'
            });
        }, 200);
    }

    // Special handling for step 3: trigger RAG content expansion
    if (step === 3) {
        setTimeout(() => {
            const ragContent = document.getElementById('rag-content-1');
            const systemCard = document.querySelector('.slide-15 .system-message');

            if (ragContent && systemCard) {
                // Start by showing the separator
                ragContent.classList.add('show');

                // Set card to final height immediately to accommodate all content
                setTimeout(() => {
                    const finalHeight = systemCard.scrollHeight;
                    systemCard.style.height = finalHeight + 'px';
                }, 100);

                // Sequential pulsing of documents (just visual effect, card already sized)
                const chunks = ragContent.querySelectorAll('.chunk-item');

                chunks.forEach((chunk, index) => {
                    setTimeout(() => {
                        chunk.classList.add('pulse');
                    }, 600 + (index * 800)); // Progressive text appearance
                });
            }
        }, 500);
    }
}

function resetProgressiveDemo() {
    for (let i = 1; i <= 4; i++) {
        const element = document.getElementById(`demo-step-${i}`);
        if (element) {
            // Immediately remove show class and reset state
            element.classList.remove('show');
            // Force immediate reset without transition
            element.style.transition = 'none';
            element.style.opacity = '0';
            element.style.transform = 'translateY(30px)';
            // Re-enable transition after a brief moment
            setTimeout(() => {
                if (element) {
                    element.style.transition = 'all 0.6s ease-out';
                }
            }, 50);
        }
    }

    // Reset RAG content
    const ragContent = document.getElementById('rag-content-1');
    const systemCard = document.querySelector('.slide-15 .system-message');

    if (ragContent) {
        ragContent.classList.remove('show');
        ragContent.style.opacity = '0';
        ragContent.style.height = '0';
        ragContent.style.overflow = 'hidden';

        // Reset chunk animations
        const chunks = ragContent.querySelectorAll('.chunk-item');
        chunks.forEach(chunk => {
            chunk.classList.remove('pulse');
        });
    }

    // Reset system card height
    if (systemCard) {
        systemCard.style.height = 'auto';
    }

    // Clean up scroll detection
    const slide15 = document.querySelector('.slide-15');
    if (slide15 && slide15.scrollCleanup) {
        slide15.scrollCleanup();
    }
}

// No click handler needed - animations are triggered by keyboard navigation
// (Space, Arrow keys) which is handled by the main navigation system

// Add slide resetters registry if not exists
if (typeof window.slideResetters === 'undefined') {
    window.slideResetters = {};
}

// Register the reset function for this slide
window.slideResetters['slide-15'] = function() {
    window.ragAnimationStep = 0;
    resetProgressiveDemo();
};

// Scroll detection for slide-15 fade effects
function setupScrollDetection() {
    const slide15 = document.querySelector('.slide-15');
    if (!slide15) return;

    function checkScroll() {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        const windowHeight = window.innerHeight;
        const documentHeight = document.documentElement.scrollHeight;

        // Check if we're scrolled and content extends beyond viewport
        if (scrollTop > 50 || documentHeight > windowHeight + 100) {
            slide15.classList.add('scrolled');
        } else {
            slide15.classList.remove('scrolled');
        }
    }

    // Check scroll on load and scroll events
    window.addEventListener('scroll', checkScroll);
    checkScroll(); // Initial check

    // Clean up listener when leaving slide
    slide15.scrollCleanup = () => {
        window.removeEventListener('scroll', checkScroll);
        slide15.classList.remove('scrolled');
    };
}

// Set up scroll detection when slide becomes active
const slide15Observer = new MutationObserver(function(mutations) {
    mutations.forEach(function(mutation) {
        if (mutation.attributeName === 'class') {
            const slide15 = document.querySelector('.slide-15');
            if (slide15 && slide15.classList.contains('active')) {
                setTimeout(() => {
                    setupScrollDetection();
                }, 100);
            }
        }
    });
});

// Start observing when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    const slide15 = document.querySelector('.slide-15');
    if (slide15) {
        slide15Observer.observe(slide15, { attributes: true });
    }
});
