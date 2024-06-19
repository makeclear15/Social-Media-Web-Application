// Switching between login and signup 

function switchForm(targetCardId) {
    const loginCard = document.getElementById('loginCard');
    const signupCard = document.getElementById('signupCard');

    if (targetCardId === 'loginCard') {
        loginCard.style.display = 'block';
        signupCard.style.display = 'none';
    } else {
        loginCard.style.display = 'none';
        signupCard.style.display = 'block';
    }
}

function validate(){
    var username = document.getElementById('loginUsername').value
    var password = document.getElementById('loginPassword').value
    

    if(username == 'admin' && password == 'admin@123'){
        var next_page_url = document.querySelector('#loginForm');
        next_page_url.setAttribute('onaction','dashboard.html')
        console.log(next_page_url)

        
        alert("Admin Page")

    }
    else{
        alert("User Page")
    }

}