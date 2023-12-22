$(".input_text").focus(function(){
    $(this).prev('.fa').addclass('glowIcon')
})
$(".input_text").focusout(function(){
    $(this).prev('.fa').removeclass('glowIcon')
})

//login

function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    
    
    // Make a POST request to the server-side API for login
    
    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
    })
    .then(response => response.json())
    .then(data => {
        const resultMessage = document.getElementById('resultMessage');

        if (data.success) {
            alert("Success");
            resultMessage.style.color = 'green';
            window.location.href = data.url;
            //onSuccessfulLogin();
            
        } else {
            alert("Failure");
            resultMessage.style.color = 'red';
        }
        

        resultMessage.textContent = data.message;
    })
    .catch(error => console.error('Error:', error));
}