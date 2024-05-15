$(document).ready(function () {
    $('#signUpForm').on('submit', function (event) {
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
});