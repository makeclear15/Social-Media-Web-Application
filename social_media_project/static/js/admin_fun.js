//Start to sort User List
function sort_user() {
    var selectElement = document.getElementById('user_sort');
    var selectedOption = selectElement.value;
//    console.log('Selected option:', selectedOption);
    var sortbutton = document.getElementById('sort_btn');
    sortbutton.href = '12_'+selectedOption;
    sortbutton.click();
}
function search_user() {
    var selectElement = document.getElementById('search_bar');
    var selectedOption = selectElement.value;
//    console.log('Selected option:', selectedOption);
    var searchbtn = document.getElementById('search_btn');
    searchbtn.href = '13_'+selectedOption;
    searchbtn.click();
}

function sort_profile() {
    var selectElement = document.getElementById('user_prof');
    var selectedOption = selectElement.value;
//    console.log('Selected option:', selectedOption);
    var sortbutton = document.getElementById('sort_btn1');
    sortbutton.href = '12_'+selectedOption;
    sortbutton.click();
}

function search_profile() {
    var selectElement = document.getElementById('search_bar');
    var selectedOption = selectElement.value;
//    console.log('Selected option:', selectedOption);
    var searchbtn = document.getElementById('search_btn');
    searchbtn.href = '13_'+selectedOption;
    searchbtn.click();
}
//document.addEventListener("DOMContentLoaded", function() {
function show_user_form(){
    // Your code here
    var showFormButton = document.getElementById("add_user");
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

function search_profile_user() {
    var selectElement = document.getElementById('search_bar_user');
    var selectedOption = selectElement.value;
//    console.log('Selected option:', selectedOption);
    var searchbtn = document.getElementById('search_btn_user');
    searchbtn.href = '/admin_search_user/13_'+selectedOption;
    searchbtn.click();
}
