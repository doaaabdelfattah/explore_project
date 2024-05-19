$(document).ready(function () {
    $('#signUpForm').on('submit', function (event) {
        // const phoneNumber = $('#phone');
        // if (typeof phoneNumber !== Number) {
        //     event.preventDefault();
        //     $('#phoneNumber').addClass('error');
        //     $('#phoneNumber').after('<span class="error-message">Phone must be number.</span>');

        // }


        const password = $('#password').val();
        const confirmPassword = $('#confirmPassword').val();

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


