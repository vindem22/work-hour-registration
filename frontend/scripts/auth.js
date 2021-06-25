const CLIENT_ID = 'QS1lmDYxbmIeVSbZFW22HPweyL2lFzX9qCrBfRMW'
const CLIENT_SECRET = 'TpI1AE4e8SJusMmTKojgl8cPDMivbBZCLUcmiTWun76mV2gzW39ucXxMcsHwek4Ar55Ydzsqs3DiV5ZmHY3oABdd9PSbgqjYynq8hsXTmLy2argiM0QXPXGiVLVWqWX6'

const submit_btn = document.querySelector('button');

function authentication() {
    const emailInput = document.getElementById('email').value;
    const passwordInput = document.getElementById('password').value;

    const reqBody = {
        client_id: CLIENT_ID,
        client_secret: CLIENT_SECRET,
        grant_type: "password",
        username: emailInput,
        password: passwordInput
    }
    console.log('password', passwordInput, 'email', emailInput)
    fetch('http://localhost:8000/auth/login/', { 
        method: "POST", 
        headers: {
            'Content-Type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify(reqBody)}
    ).then(response => response.json()).then(data => {
        if(data.error) {
            console.log(data.error);
        } else {
            saveCookie(data);
        }
    }).catch(error => console.log(error))
    console.log('success')
}

function saveCookie(data) {
    if(localStorage.getItem('auth-token') === null) {
        localStorage.setItem('auth-token', data.access_token)
    }
}


submit_btn.addEventListener('click', e => {
    e.preventDefault();
    authentication();
})



