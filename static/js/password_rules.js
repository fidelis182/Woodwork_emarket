document.addEventListener("DOMContentLoaded", () => {
    const passwordInput = document.getElementById('id_password1');
    if (!passwordInput) return;

    const rules = {
        length: document.getElementById('rule-length'),
        number: document.getElementById('rule-number'),
        uppercase: document.getElementById('rule-uppercase'),
        lowercase: document.getElementById('rule-lowercase'),
        special: document.getElementById('rule-special')
    };

    passwordInput.addEventListener('input', () => {
        const value = passwordInput.value;

        rules.length.classList.toggle('text-success', value.length >= 8);
        rules.length.classList.toggle('text-danger', value.length < 8);
        rules.length.textContent = (value.length >= 8 ? '✅' : '❌') + ' At least 8 characters';

        rules.number.classList.toggle('text-success', /\d/.test(value));
        rules.number.classList.toggle('text-danger', !/\d/.test(value));
        rules.number.textContent = (/\d/.test(value) ? '✅' : '❌') + ' At least one number';

        rules.uppercase.classList.toggle('text-success', /[A-Z]/.test(value));
        rules.uppercase.classList.toggle('text-danger', !/[A-Z]/.test(value));
        rules.uppercase.textContent = (/[A-Z]/.test(value) ? '✅' : '❌') + ' At least one uppercase letter';

        rules.lowercase.classList.toggle('text-success', /[a-z]/.test(value));
        rules.lowercase.classList.toggle('text-danger', !/[a-z]/.test(value));
        rules.lowercase.textContent = (/[a-z]/.test(value) ? '✅' : '❌') + ' At least one lowercase letter';

        rules.special.classList.toggle('text-success', /[!@#$%^&*]/.test(value));
        rules.special.classList.toggle('text-danger', !/[!@#$%^&*]/.test(value));
        rules.special.textContent = (/[!@#$%^&*]/.test(value) ? '✅' : '❌') + ' At least one special character (!@#$%^&*)';
    });
});

    passwordInput.addEventListener('input', () => {
        checkRules(passwordInput.value);

        if (confirmInput && confirmInput.value.length > 0) {
            if (passwordInput.value === confirmInput.value) {
                confirmInput.classList.add('is-valid');
                confirmInput.classList.remove('is-invalid');
            } else {
                confirmInput.classList.add('is-invalid');
                confirmInput.classList.remove('is-valid');
            }
        }
    });

    if (confirmInput) {
        confirmInput.addEventListener('input', () => {
            if (passwordInput.value === confirmInput.value) {
                confirmInput.classList.add('is-valid');
                confirmInput.classList.remove('is-invalid');
            } else {
                confirmInput.classList.add('is-invalid');
                confirmInput.classList.remove('is-valid');
            }
        });
    }
});
