// Slide 11: Autoregression Animation Controller

let autoregressStep = 0;
const maxSteps = 6; // Updated to match actual HTML structure (4 steps + 2 states)

function nextAutoregressStep() {
    // Prevent triggering during slide transitions
    if (currentSlide !== 10) return; // Slide 11 is index 10
    
    autoregressStep = (autoregressStep + 1) % maxSteps;
    
    // Reset all elements
    const elements = [
        'prediction1', 'arrow1', 'step2', 'prediction2', 'arrow2', 'step3', 
        'prediction3', 'arrow3', 'step4'
    ];
    elements.forEach(id => {
        const el = document.getElementById(id);
        if (el) el.style.opacity = '0';
    });
    
    // Get container for scrolling
    const container = document.getElementById('stepsContainer');
    const autoContainer = container.parentElement;
    
    // Show elements based on current step and auto-scroll
    switch(autoregressStep) {
        case 1: // Show "while" prediction
            document.getElementById('prediction1').style.opacity = '1';
            break;
            
        case 2: // Show arrow and step 2
            document.getElementById('prediction1').style.opacity = '1';
            document.getElementById('arrow1').style.opacity = '1';
            document.getElementById('step2').style.opacity = '1';
            scrollToStep('step2', container);
            break;
            
        case 3: // Show "ensuring" prediction
            document.getElementById('prediction1').style.opacity = '1';
            document.getElementById('arrow1').style.opacity = '1';
            document.getElementById('step2').style.opacity = '1';
            document.getElementById('prediction2').style.opacity = '1';
            break;
            
        case 4: // Show arrow and step 3
            document.getElementById('prediction1').style.opacity = '1';
            document.getElementById('arrow1').style.opacity = '1';
            document.getElementById('step2').style.opacity = '1';
            document.getElementById('prediction2').style.opacity = '1';
            document.getElementById('arrow2').style.opacity = '1';
            document.getElementById('step3').style.opacity = '1';
            scrollToStep('step3', container);
            break;
            
        case 5: // Show "it" prediction
            document.getElementById('prediction1').style.opacity = '1';
            document.getElementById('arrow1').style.opacity = '1';
            document.getElementById('step2').style.opacity = '1';
            document.getElementById('prediction2').style.opacity = '1';
            document.getElementById('arrow2').style.opacity = '1';
            document.getElementById('step3').style.opacity = '1';
            document.getElementById('prediction3').style.opacity = '1';
            break;
            
        case 0: // Reset state - back to beginning
            container.scrollTop = 0;
            autoContainer.classList.remove('has-scroll');
            break;
    }
}

function scrollToStep(stepId, container) {
    const step = document.getElementById(stepId);
    if (step && container) {
        setTimeout(() => {
            const stepTop = step.offsetTop - container.offsetTop;
            const containerHeight = container.clientHeight;
            const stepHeight = step.clientHeight;
            
            // Calculate scroll position to center the step
            const scrollTo = stepTop - (containerHeight / 2) + (stepHeight / 2);
            
            container.scrollTo({
                top: Math.max(0, scrollTo),
                behavior: 'smooth'
            });
            
            // Show fade overlays after scrolling
            setTimeout(() => {
                updateFadeOverlays(container, container.parentElement);
            }, 300);
        }, 100);
    }
}

function updateFadeOverlays(container, autoContainer) {
    if (container.scrollHeight > container.clientHeight) {
        autoContainer.classList.add('has-scroll');
    } else {
        autoContainer.classList.remove('has-scroll');
    }
}

function resetAutoregressSlide() {
    autoregressStep = 0;
    const elements = [
        'prediction1', 'arrow1', 'step2', 'prediction2', 'arrow2', 'step3',
        'prediction3', 'arrow3', 'step4', 'prediction4', 'arrow4', 'step5',
        'prediction5', 'arrow5', 'step6'
    ];
    elements.forEach(id => {
        const el = document.getElementById(id);
        if (el) el.style.opacity = '0';
    });
    
    // Reset scroll and fades
    const container = document.getElementById('stepsContainer');
    if (container) {
        container.scrollTop = 0;
        container.parentElement.classList.remove('has-scroll');
    }
}

// Register slide 11 reset function with navigation system
if (typeof registerSlideResetter === 'function') {
    registerSlideResetter(10, resetAutoregressSlide); // Slide 11 is index 10
}

// Make nextAutoregressStep globally available for onclick handlers
if (typeof window !== 'undefined') {
    window.nextAutoregressStep = nextAutoregressStep;
}