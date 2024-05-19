$(document).ready(function () {
    // Function to validate a form
    function validateForm(formId) {
        // Clear previous error messages
        $(formId + ' .error-message').remove();
        $(formId + ' .form-control').removeClass('error');

        // Get form values
        const firstName = $(formId + ' #f-name').val().trim();
        const lastName = $(formId + ' #l-name').val().trim();
        const email = $(formId + ' #email').val().trim();
        const phone = $(formId + ' #phone').val().trim();
        const password = $(formId + ' #password').val();
        const confirmPassword = $(formId + ' #confirmPassword').val();

        let hasErrors = false;

        // Validate first name
        if (!/^[a-zA-Z]+$/.test(firstName)) {
            $(formId + ' #f-name').addClass('error');
            $(formId + ' #f-name').after('<span class="error-message">First name must be a valid text.</span>');
            hasErrors = true;
        }

        // Validate last name
        if (!/^[a-zA-Z]+$/.test(lastName)) {
            $(formId + ' #l-name').addClass('error');
            $(formId + ' #l-name').after('<span class="error-message">Last name must be a valid text.</span>');
            hasErrors = true;
        }

        // Validate Phone number
        const phonePattern = /^\d{5,}$/;
        if (!phonePattern.test(phone)) {
            $(formId + ' #phone').addClass('error');
            $(formId + ' #phone').after('<span class="error-message">Phone Number is not valid.</span>');
            hasErrors = true;
        }

        // Validate email
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailPattern.test(email)) {
            $(formId + ' #email').addClass('error');
            $(formId + ' #email').after('<span class="error-message">Email must be valid.</span>');
            hasErrors = true;
        }

        // Validate password match
        if (password !== confirmPassword) {
            $(formId + ' #confirmPassword').addClass('error');
            $(formId + ' #confirmPassword').after('<span class="error-message">Passwords do not match. Please try again.</span>');
            hasErrors = true;
        }

        return !hasErrors;
    }

    $('#signUpForm').on('submit', function (event) {
        event.preventDefault();

        if (validateForm('#signUpForm')) {
            alert('Form submitted successfully!');
            this.submit();
        }
    });

    $('#contactForm').on('submit', function (event) {
        event.preventDefault();

        if (validateForm('#contactForm')) {
            alert('Form submitted successfully!');
            this.submit();
        }
    });

    $('#bookingForm').on('submit', function (event) {
        event.preventDefault();

        if (validateForm('#bookingForm')) {
            alert('Form submitted successfully!');
            this.submit();
        }
    });

    // Remove error styles and messages when the input fields are changed
    $('#f-name, #l-name, #email, #phone, #password, #confirmPassword').on('input', function () {
        $(this).removeClass('error');
        $(this).next('.error-message').remove();
    });

    // Toggle menu functionality using event delegation
    $(document).on('click', '.toggle-menu', function () {
        $('.links-container').toggleClass('open');
    });

    // Optionally close the menu when a link is clicked
    $(document).on('click', '.links-container ul li a', function () {
        $('.links-container').removeClass('open');
    });
});