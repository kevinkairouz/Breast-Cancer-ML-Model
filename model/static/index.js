
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('cancerForm');
    const clearBtn = document.getElementById('clearBtn');
    const resultDiv = document.getElementById('result');
    const resultText = document.getElementById('resultText');


    clearBtn.addEventListener('click', function() {
        if (confirm('Are you sure you want to clear all fields?')) {
            form.reset();
            resultDiv.style.display = 'none';
            
    
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        }
    });

 
    form.addEventListener('submit', function(e) {
        const inputs = form.querySelectorAll('input[type="number"]');
        let isValid = true;

        inputs.forEach(input => {
            if (input.value === '' || isNaN(input.value)) {
                isValid = false;
                input.style.borderColor = '#f56565';
            } else {
                input.style.borderColor = '#e2e8f0';
            }
        });

        if (!isValid) {
            e.preventDefault();
            alert('Please fill in all fields with valid numbers');
            return false;
        }

        const submitBtn = form.querySelector('input[type="submit"]');
        const originalValue = submitBtn.value;
        submitBtn.value = 'Processing...';
        submitBtn.disabled = true;

        e.preventDefault();
        handleAjaxSubmission();
    });

    function saveFormData() {
        const formData = {};
        const inputs = form.querySelectorAll('input[type="number"]');
        
        inputs.forEach(input => {
            formData[input.name] = input.value;
        });
        
        localStorage.setItem('breastCancerFormData', JSON.stringify(formData));
    }

    function loadFormData() {
        const savedData = localStorage.getItem('breastCancerFormData');
        
        if (savedData) {
            const formData = JSON.parse(savedData);
            
            Object.keys(formData).forEach(key => {
                const input = form.querySelector(`[name="${key}"]`);
                if (input) {
                    input.value = formData[key];
                }
            });
        }
    }

    function debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }


    function handleAjaxSubmission() {
        const formData = new FormData(form);
        const data = {};
        
        formData.forEach((value, key) => {
            data[key] = parseFloat(value);
        });

        fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            // Display result
            resultText.textContent = data.prediction || data.result;
            resultDiv.style.display = 'block';
            
            // Scroll to result
            resultDiv.scrollIntoView({ behavior: 'smooth' });
            
            // Reset submit button
            const submitBtn = form.querySelector('input[type="submit"]');
            submitBtn.value = 'Get Prediction';
            submitBtn.disabled = false;
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred. Please try again.');
            
            const submitBtn = form.querySelector('input[type="submit"]');
            submitBtn.value = 'Get Prediction';
            submitBtn.disabled = false;
        });
    }

    const sectionHeaders = document.querySelectorAll('.section h2');
    sectionHeaders.forEach(header => {
        header.style.cursor = 'pointer';
        header.addEventListener('click', function() {
            this.parentElement.scrollIntoView({ behavior: 'smooth' });
        });
    });

    const numberInputs = form.querySelectorAll('input[type="number"]');
    numberInputs.forEach(input => {
        input.addEventListener('blur', function() {
            if (this.value === '') {
                this.style.borderColor = '#f56565';
            } else {
                this.style.borderColor = '#48bb78';
            }
        });
    });
});

function loadSampleData() {
    const sampleData = {
        radius_mean: 17.99,
        texture_mean: 10.38,
        perimeter_mean: 122.8,
        area_mean: 1001,
        smoothness_mean: 0.1184,
        compactness_mean: 0.2776,
        concavity_mean: 0.3001,
        concave_points_mean: 0.1471,
        symmetry_mean: 0.2419,
        fractal_dimension_mean: 0.07871,
        radius_se: 1.095,
        texture_se: 0.9053,
        perimeter_se: 8.589,
        area_se: 153.4,
        smoothness_se: 0.006399,
        compactness_se: 0.04904,
        concavity_se: 0.05373,
        concave_points_se: 0.01587,
        symmetry_se: 0.03003,
        fractal_dimension_se: 0.006193,
        radius_worst: 25.38,
        texture_worst: 17.33,
        perimeter_worst: 184.6,
        area_worst: 2019,
        smoothness_worst: 0.1622,
        compactness_worst: 0.6656,
        concavity_worst: 0.7119,
        concave_points_worst: 0.2654,
        symmetry_worst: 0.4601,
        fractal_dimension_worst: 0.1189
    };

    Object.keys(sampleData).forEach(key => {
        const input = document.querySelector(`[name="${key}"]`);
        if (input) {
            input.value = sampleData[key];
        }
    });
}

console.log('To load sample data, run: loadSampleData()');