function show_user_form(){
    // Your code here
    var showFormButton = document.getElementsByClassName("comment-link");
    var modalContainer = document.getElementById("modalContainer");

    showFormButton.onclick = function() {
        modalContainer.style.display = "block";
    }

    document.getElementsByClassName("close")[0].onclick = function() {
        modalContainer.style.display = "none";
    }

    window.onclick = function(event) {
        if (event.target == modalContainer) {
            modalContainer.style.display = "none";
        }
    }
}