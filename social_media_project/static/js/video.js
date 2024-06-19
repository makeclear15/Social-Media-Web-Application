document.addEventListener('DOMContentLoaded', function () {
    const video = document.getElementById('myVideo');
    const playButton = document.getElementById('playButton');

    playButton.addEventListener('click', function () {
      if (video.paused) {
        video.play();
        playButton.style.display = 'none';
      } else {
        video.pause();
      }
    });

    video.addEventListener('play', function () {
      playButton.style.display = 'none';
    });

    video.addEventListener('pause', function () {
      playButton.style.display = 'block';
    });
  });

