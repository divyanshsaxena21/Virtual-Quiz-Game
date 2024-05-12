// static/script.js

function validateForm() {
    var username = document.getElementById('username').value;
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    var name = document.getElementById('name').value

    if (username.trim() === '' || email.trim() === '' || password.trim() === '' || name.trim() === '') {
        alert('Please fill in all fields.');
    } else {
        document.getElementById('signupForm').submit();
        alert('SignUp Succesful');
    }
}
