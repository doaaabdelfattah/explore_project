$(document).ready(function () {
    $('#signUpForm').on('submit', function (event) {
        // Prevent form submission to handle validation first
        event.preventDefault();

        // Clear previous error messages
        $('.error-message').remove();
        $('.form-control').removeClass('error');

        // Get form values
        const firstName = $('#f-name').val().trim();
        const lastName = $('#l-name').val().trim();
        const email = $('#email').val().trim();
        const password = $('#password').val();
        const confirmPassword = $('#confirmPassword').val();

        let hasErrors = false;

        // Validate first name
        if (!/^[a-zA-Z]+$/.test(firstName)) {
            $('#f-name').addClass('error');
            $('#f-name').after('<span class="error-message">First name must be a valid text.</span>');
            hasErrors = true;
        }

        // Validate last name
        if (!/^[a-zA-Z]+$/.test(lastName)) {
            $('#l-name').addClass('error');
            $('#l-name').after('<span class="error-message">Last name must be a valid text.</span>');
            hasErrors = true;
        }

        // Validate email
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailPattern.test(email)) {
            $('#email').addClass('error');
            $('#email').after('<span class="error-message">Email must be valid.</span>');
            hasErrors = true;
        }

        // Validate password match
        if (password !== confirmPassword) {
            $('#confirmPassword').addClass('error');
            $('#confirmPassword').after('<span class="error-message">Passwords do not match. Please try again.</span>');
            hasErrors = true;
        }

        // If no errors, submit the form
        if (!hasErrors) {
            alert('Form submitted successfully!');
            // You can proceed with form submission or AJAX call here
            this.submit();
        }
    });

    // Remove error styles and messages when the input fields are changed
    $('#f-name, #l-name, #email, #password, #confirmPassword').on('input', function () {
        $(this).removeClass('error');
        $(this).next('.error-message').remove();
    });

    // =========== Toggle Menu ====================
    // Toggle menu functionality
    $('.toggle-menu').click(function () {
        $('.links-container').toggleClass('open');
    });

    // Optionally close the menu when a link is clicked
    $('.links-container ul li a').click(function () {
        $('.links-container').removeClass('open');
    });
});
