
  function switchForm(targetID){

    var user_list = document.getElementById('user_list')
    var group_list = document.getElementById('group_list')
    var user_profile_list = document.getElementById('user_profile_list')
    
    user_list.style.display = 'none'
    group_list.style.display = 'none'
    user_profile_list.style.display = 'none'
    switch(targetID){
      case 'display_user':
        user_list.style.display = 'block'
        var display_user= document.getElementById('display_user')
        display_user.setAttribute('href','adminpage/{{1}}')
        console.log(display_user)
        break;
      case 'display_user_profile':
        user_profile_list.style.display = 'block'
        break;
      case 'display_group':
        group_list.style.display = 'block'
        break;

    }

  }