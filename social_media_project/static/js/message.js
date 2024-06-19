function AddUser(){
    var input = ['Dinesh','Vivek','Stephen','Arun','Mukesh','Mohan','Zain','Sameer','Rin']
    console.log(input)

    for (var value of input)
    {
    var element = document.createElement('div')
    element.setAttribute('class','ind-user')
    element.setAttribute('onclick',`LoadMsg('${value}')`)
    element.innerHTML = `
    <h4 class="${value}")">${value}</h4>
    <p>Hello! This is ${value}</p>`
    
    var addElement = document.getElementById('users')
    addElement.append(element)
    }
}
function LoadMsg(event){
    // var user_name = document.getElementsByClassName("user_name").textContent
    var user_name = event
    var Username = document.getElementById("Username")
    Username.innerHTML=`${user_name}`
    console.log(user_name)
}