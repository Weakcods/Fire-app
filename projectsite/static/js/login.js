// Show/Hide Password with enhanced accessibility and animations
document.addEventListener('DOMContentLoaded', function() {
    const togglePassword = document.querySelector('.show-password');
    
    togglePassword.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        
        const passwordInput = this.closest('.input-group').querySelector('input');
        const icon = this.querySelector('i');
        
        // Add transition class to password input
        passwordInput.style.transition = 'all 0.3s ease';
        
        if (passwordInput.type === 'password') {
            passwordInput.type = 'text';
            icon.classList.remove('fa-eye');
            icon.classList.add('fa-eye-slash');
            this.setAttribute('data-tooltip', 'Hide Password');
            this.setAttribute('aria-label', 'Hide Password');
        } else {
            passwordInput.type = 'password';
            icon.classList.remove('fa-eye-slash');
            icon.classList.add('fa-eye');
            this.setAttribute('data-tooltip', 'Show Password');
            this.setAttribute('aria-label', 'Show Password');
        }
        
        // Add click feedback animation
        icon.style.transform = 'scale(0.8)';
        setTimeout(() => {
            icon.style.transform = 'scale(1)';
        }, 100);
        
        // Prevent other handlers from executing
        return false;
    });
});

// Form validation
(function() {
    'use strict';
    window.addEventListener('load', function() {
        var forms = document.getElementsByClassName('needs-validation');
        Array.prototype.filter.call(forms, function(form) {
            form.addEventListener('submit', function(event) {
                if (form.checkValidity() === false) {
                    event.preventDefault();
                    event.stopPropagation();
                } else {
                    // Add loading state to button
                    const button = form.querySelector('button[type="submit"]');
                    button.classList.add('loading');
                }
                form.classList.add('was-validated');
            }, false);
        });
    }, false);
})();

// Add floating label effect
const inputs = document.querySelectorAll('.form-control');
inputs.forEach(input => {
    input.addEventListener('focus', () => {
        input.parentElement.classList.add('focused');
    });
    
    input.addEventListener('blur', () => {
        if (!input.value) {
            input.parentElement.classList.remove('focused');
        }
    });
    
    // Check on load
    if (input.value) {
        input.parentElement.classList.add('focused');
    }
});
