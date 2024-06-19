

function Load_notify_suggesion(){

createNotification("Vivek", "liked your post");
createNotification("Arun", "commented on your photo");

createFriendSuggestion("Stephen");
createFriendSuggestion("Dinesh");
}

function LoadPost(){

// Set the max attribute for date_of_birth input field
document.getElementById('date_of_birth').setAttribute('max', getCurrentDate());



//    var urls= ['images/\img1.jpg','images/\img3.jpg',
//    'images/\img4.jpg','images/\img5.jpg',]
//    console.log(urls)

//    for(url of urls){
//    var element = document.createElement('div')
//    element.setAttribute('class','post')
//    element.innerHTML =`
//    <div class="user_post_detail">
//          <img class="user_profile"
//          src="${url}">
//          <div><p>Dinesh</p></div>
//        </div>
//    <img class="post-img"
//    src="${url}"
//    alt="Post Image"
//  />
//  <div class="post-info">
//  <div class="interaction">
//  <i class="bi bi-heart">&nbsp;100</i>
//  <i class="bi bi-chat-left-dots">&nbsp;99</i>
//  <i class="bi bi-send">&nbsp;98</i>
//  <a href="${url}" download="POST">
//                <!-- download>hello  -->
//                <i class="bi bi-arrow-down-circle"></i>
//              </a>
//
//</div>
//    <div class="post-text">
//      Instagram is a popular Social media in recent years.
//    </div>`
//    var addElement = document.getElementsByClassName('main_content')[0];
//    addElement.append(element);
//    }



    
//    var post_urls= ['images/\img1.jpg','images/\img3.jpg',
//    'images/\img4.jpg','images/\img5.jpg',]
//
//    for(url of post_urls){
//      var img_element = document.createElement('img')
//      img_element.setAttribute('class','user-post-img')
//      img_element.src = `${url}`
//
//
//    var addElement = document.getElementsByClassName('post-list')[0]
//      addElement.append(img_element)
//      // console.log(img_element)
//    }

    //Load Notification and Follow Suggession


}

//function switchForm(targetCardId) {
//  const post_area = document.getElementById('post-area');
//
//  const add_post = document.getElementById('add-post');
//  const manage_post = document.getElementById('manage-post');
//  const user_profile = document.getElementById('user-profile');
//
//  manage_post.style.display = 'none';
//  post_area.style.display = 'none';
//
//  if (targetCardId === 'user-profile') {
//    user_profile.style.display = 'block';
//  }
//  else{
//    user_profile.style.display = 'none';
//  }
//
//  if (targetCardId === 'display-post') {
//    post_area.style.display = 'block';
//  }
//  else{
//    post_area.style.display = 'none';
//  }
//
//  if (targetCardId === 'manage-post') {
//    manage_post.style.display = 'block';
//  }
//  else{
//    manage_post.style.display = 'none';
//  }
//
//  if (targetCardId === 'add-post') {
//    add_post.style.display = 'block';
//  }
//  else{
//    add_post.style.display = 'none';
//  }
//  //   signupCard.style.display = 'none';
//  // } else {
//  //   loginCard.style.display = 'none';
//  //   signupCard.style.display = 'block';
//  // }
//}

function previewFile() {
  var preview = document.getElementById('filePreview');
  var fileInput = document.getElementById('postFile_url');
  var file = fileInput.files[0];


  if (file) {
      preview.innerHTML = ''; // Clear previous preview

      var fileType = file.type.split('/')[0]; // Get file type (image or video)

      if (fileType === 'image') {
          var img = document.createElement('img');
          img.setAttribute('height', '400px');
          img.setAttribute('width', '100%');
          img.src = URL.createObjectURL(file);
          preview.appendChild(img);
      } else if (fileType === 'video') {
          var video = document.createElement('video');
          video.setAttribute('height', '100');
          video.setAttribute('width', '200');
          video.src = URL.createObjectURL(file);
          video.controls = true;
          preview.appendChild(video);
      }

      preview.style.display = 'block';
  } else {
      preview.style.display = 'none';
  }
}


// date of bith limitation

// Get the current date in the format YYYY-MM-DD
function getCurrentDate() {
  const today = new Date();
  const year = today.getFullYear();
  let month = today.getMonth() + 1;
  let day = today.getDate();

  // Pad month and day with leading zeros if needed
  month = month < 10 ? '0' + month : month;
  day = day < 10 ? '0' + day : day;

  return `${year}-${month}-${day}`;
}

// Start of User-profile hearder Script

function showFollowing() {
  
var followers = document.getElementById("followers-list")
var following = document.getElementById("following-list")
    following.style.display = "block"
    followers.style.display = "none"

  }
  
  function showFollowers() {
    
var followers = document.getElementById("followers-list")
var following = document.getElementById("following-list")
    following.style.display = "none"
    followers.style.display = "block"
  }
// End of User-profile hearder Script

// Start of User Profile details form
function user_details_form(targetCardId){

  let user_details_form = document.getElementById("user_details_form")
  // if(targetCardId == "Show form"){
  // }

  switch (targetCardId){
    case "Show_form":
      user_details_form.style.display = 'block';
      break;
    case "Hide_form":
      user_details_form.style.display = 'none';
      break;
      
  }
  
}


// Start of Notification and follow Suggession 
// Add the following JavaScript code to your script.js file

function createNotification(username, type) {
  var notification = document.createElement("div");
  notification.className = "notification";

  var usernameElement = document.createElement("span");
  usernameElement.className = "username";
  usernameElement.textContent = username;

  var typeElement = document.createElement("span");
  typeElement.className = "type";
  typeElement.textContent = type;

  notification.appendChild(usernameElement);
  notification.appendChild(document.createTextNode(" - "));
  notification.appendChild(typeElement);

  document.getElementById("notificationList").appendChild(notification);
}

function createFriendSuggestion(name) {
  var friendSuggestion = document.createElement("div");
  friendSuggestion.className = "friendSuggestion";

  var friendSuggestionName = document.createElement("div");
  friendSuggestionName.className = "friendSuggestionName";
  friendSuggestionName.textContent = name;

  var friendSuggestionButton = document.createElement("button");
  friendSuggestionButton.className = "friendSuggestionButton";
  friendSuggestionButton.textContent = "follow";

  friendSuggestion.appendChild(friendSuggestionName);
  friendSuggestion.appendChild(friendSuggestionButton);

  document.getElementById("friendSuggestionList").appendChild(friendSuggestion);
}
// End of Notification and follow Suggession


