function search_profile() {
    var selectElement = document.getElementById('search_bar');
    var selectedOption = selectElement.value;
//    console.log('Selected option:', selectedOption);
    var searchbtn = document.getElementById('search_btn');
    searchbtn.href = '/search_profiles/'+selectedOption;
    searchbtn.click();
}