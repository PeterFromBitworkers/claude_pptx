// Slide 17: Why Now Animation Functions

function startWhyNowAnimation() {
    const steps = document.querySelectorAll('.timeline-step');
    const connectors = document.querySelectorAll('.timeline-connector');
    
    // Make timeline steps visible immediately
    steps.forEach((step, index) => {
        setTimeout(() => {
            step.classList.add('animate-in');
        }, index * 200); // Stagger animation
    });
    
    // Make connectors visible
    connectors.forEach((connector, index) => {
        setTimeout(() => {
            connector.classList.add('animate-in');
        }, (index + 1) * 200 + 300); // After corresponding step
    });
}

function resetWhyNowAnimation() {
    const steps = document.querySelectorAll('.timeline-step');
    const connectors = document.querySelectorAll('.timeline-connector');
    
    // Reset timeline steps
    steps.forEach(step => {
        step.classList.remove('animate-in');
    });
    
    // Reset connectors
    connectors.forEach(connector => {
        connector.classList.remove('animate-in');
    });
}

function initializeSlide16() {
    setTimeout(() => {
        startWhyNowAnimation();
    }, 500);
}

// Register with navigation system
if (typeof registerSlideInitializer === 'function') {
    registerSlideInitializer(16, initializeSlide16); // Slide 17 is index 16
}

if (typeof registerSlideResetter === 'function') {
    registerSlideResetter(16, resetWhyNowAnimation); // Slide 17 is index 16
}