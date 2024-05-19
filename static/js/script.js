$(document).ready(function () {
    $('#signUpForm').on('submit', function (event) {
        // Prevent form submission
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



        // Validate first name
        if (!/^[a-zA-Z]+$/.test(firstName)) {
            $('#firstName').addClass('error');
            $('#firstName').after('<span class="error-message">First name must be a valid text.</span>');
        }



        if (password !== confirmPassword) {
            event.preventDefault();
            $('#confirmPassword').addClass('error');
            $('#confirmPassword').after('<span class="error-message">Passwords do not match. Please try again.</span>');
        }
    });

    // Remove error styles and messages when the password fields are changed
    $('#password, #confirmPassword').on('input', function () {
        $('#confirmPassword').removeClass('error');
        $('.error-message').remove();
    });

    // Toggle menu functionality
    $('.toggle-menu').click(function () {
        $('.links-container').toggleClass('open');
    });

    // Optionally close the menu when a link is clicked
    $('.links-container ul li a').click(function () {
        $('.links-container').removeClass('open');
    });





});


