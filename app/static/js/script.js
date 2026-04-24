/**
 * Iris Species Predictor - Frontend JavaScript
 * Handles form submission, API communication, and UI interactions
 */

// ============================================
// DOM Elements
// ============================================

const predictionForm = document.getElementById('predictionForm');
const loadingSpinner = document.getElementById('loadingSpinner');
const errorContainer = document.getElementById('errorContainer');
const errorList = document.getElementById('errorList');
const resultContainer = document.getElementById('resultContainer');
const resultContent = document.getElementById('resultContent');
const closeResultBtn = document.getElementById('closeResultBtn');
const newPredictionBtn = document.getElementById('newPredictionBtn');
const themeBtn = document.getElementById('themeBtn');

// ============================================
// Theme Management
// ============================================

// Initialize theme from localStorage
function initializeTheme() {
    const savedTheme = localStorage.getItem('theme');
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    
    if (savedTheme === 'dark' || (!savedTheme && prefersDark)) {
        document.body.classList.add('dark-mode');
        updateThemeIcon();
    }
}

// Toggle dark mode
function toggleTheme() {
    document.body.classList.toggle('dark-mode');
    const isDarkMode = document.body.classList.contains('dark-mode');
    localStorage.setItem('theme', isDarkMode ? 'dark' : 'light');
    updateThemeIcon();
}

// Update theme icon
function updateThemeIcon() {
    const icon = themeBtn.querySelector('.theme-icon');
    const isDarkMode = document.body.classList.contains('dark-mode');
    icon.textContent = isDarkMode ? '☀️' : '🌙';
}

// ============================================
// Form Handling
// ============================================

/**
 * Submit prediction form
 */
predictionForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    // Clear previous errors and results
    hideError();
    hideResult();
    
    // Get form data
    const formData = {
        sepal_length: document.getElementById('sepal_length').value,
        sepal_width: document.getElementById('sepal_width').value,
        petal_length: document.getElementById('petal_length').value,
        petal_width: document.getElementById('petal_width').value
    };
    
    // Show loading spinner
    showLoading();
    
    try {
        // Send prediction request
        const response = await fetch('/api/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        });
        
        const data = await response.json();
        
        // Handle response
        if (data.success) {
            displayResult(data);
        } else {
            showError(data.details || ['An error occurred during prediction']);
        }
    } catch (error) {
        console.error('Error:', error);
        showError(['Failed to connect to server. Please check your connection.']);
    } finally {
        hideLoading();
    }
});

/**
 * Reset form
 */
predictionForm.addEventListener('reset', () => {
    hideError();
    hideResult();
});

// ============================================
// UI Display Functions
// ============================================

/**
 * Show loading spinner
 */
function showLoading() {
    loadingSpinner.classList.remove('hidden');
    predictionForm.style.opacity = '0.5';
    predictionForm.style.pointerEvents = 'none';
}

/**
 * Hide loading spinner
 */
function hideLoading() {
    loadingSpinner.classList.add('hidden');
    predictionForm.style.opacity = '1';
    predictionForm.style.pointerEvents = 'auto';
}

/**
 * Show error messages
 */
function showError(errors) {
    errorList.innerHTML = '';
    errors.forEach(error => {
        const li = document.createElement('li');
        li.textContent = error;
        errorList.appendChild(li);
    });
    errorContainer.classList.remove('hidden');
    
    // Scroll to error
    errorContainer.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

/**
 * Hide error messages
 */
function hideError() {
    errorContainer.classList.add('hidden');
    errorList.innerHTML = '';
}

/**
 * Display prediction result
 */
function displayResult(data) {
    const speciesColor = data.color || '#6366f1';
    
    // Determine species emoji
    let emoji = '🌸';
    if (data.species_id === 0) emoji = '🌼';
    else if (data.species_id === 1) emoji = '🌺';
    else if (data.species_id === 2) emoji = '🌻';
    
    // Build confidence badge HTML
    let confidenceHTML = '';
    if (data.confidence !== null) {
        confidenceHTML = `<span class="confidence-badge">Confidence: ${data.confidence}%</span>`;
    }
    
    // Build result content
    resultContent.innerHTML = `
        <div class="species-prediction" style="border-left: 4px solid ${speciesColor}">
            <div class="species-emoji">${emoji}</div>
            <div class="species-name">${data.prediction}</div>
            ${confidenceHTML}
            <p class="species-description">${data.description}</p>
            <div class="species-characteristics">
                <strong>📍 </strong>${data.characteristics}
            </div>
        </div>
    `;
    
    // Update measurement display
    document.getElementById('resultSepalLength').textContent = `${data.input_data.sepal_length} cm`;
    document.getElementById('resultSepalWidth').textContent = `${data.input_data.sepal_width} cm`;
    document.getElementById('resultPetalLength').textContent = `${data.input_data.petal_length} cm`;
    document.getElementById('resultPetalWidth').textContent = `${data.input_data.petal_width} cm`;
    
    // Show result container
    resultContainer.classList.remove('hidden');
    resultContainer.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

/**
 * Hide result container
 */
function hideResult() {
    resultContainer.classList.add('hidden');
    resultContent.innerHTML = '';
}

// ============================================
// Event Listeners
// ============================================

// Close result button
closeResultBtn.addEventListener('click', hideResult);

// New prediction button
newPredictionBtn.addEventListener('click', () => {
    hideResult();
    predictionForm.reset();
    predictionForm.scrollIntoView({ behavior: 'smooth', block: 'center' });
});

// Theme toggle button
themeBtn.addEventListener('click', toggleTheme);

// ============================================
// Input Validation (Real-time)
// ============================================

const inputs = predictionForm.querySelectorAll('input[type="number"]');

inputs.forEach(input => {
    input.addEventListener('blur', (e) => {
        const value = parseFloat(e.target.value);
        const min = parseFloat(e.target.min);
        const max = parseFloat(e.target.max);
        
        // Show hint if outside range
        if (value && (value < min || value > max)) {
            e.target.style.borderColor = '#ef4444';
        } else {
            e.target.style.borderColor = '';
        }
    });
    
    input.addEventListener('focus', (e) => {
        e.target.style.borderColor = '';
    });
});

// ============================================
// Accessibility & Keyboard Navigation
// ============================================

document.addEventListener('keydown', (e) => {
    // Press 'Escape' to close result
    if (e.key === 'Escape' && !resultContainer.classList.contains('hidden')) {
        hideResult();
    }
});

// ============================================
// Initialization
// ============================================

// Initialize theme on page load
document.addEventListener('DOMContentLoaded', () => {
    initializeTheme();
});

// Log app initialization
console.log('🌸 Iris Species Predictor loaded successfully!');
console.log('Ready to make predictions...');
