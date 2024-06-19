// Navigation Bar at Header 

function shownav(){
    
    let nav_list = document.querySelector('.sidebar');
    
    if(nav_list.style.display == "block"){
      nav_list.style.display = 'none';
    }
    else{
      nav_list.style.display = 'block';
    }

  }

