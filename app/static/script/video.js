document.addEventListener('DOMContentLoaded', function () {
  const video = document.getElementById('myVideo');
  const videoSource = document.getElementById('videoSource');
  const playButton = document.getElementById('playButton');
  const reloadButton = document.getElementById('reloadButton');
  const videoInput = document.getElementById('videoInput');
  const loadButton = document.getElementById('loadButton');
  const loadingIndicator = document.createElement('div');
  loadingIndicator.innerText = 'Loading...';
  loadingIndicator.classList.add('loading-indicator');
  video.parentElement.appendChild(loadingIndicator);

  playButton.addEventListener('click', function () {
      if (video.paused) {
          video.play();
          playButton.textContent = 'Pause';
      } else {
          video.pause();
          playButton.textContent = 'Play';
      }
  });

  reloadButton.addEventListener('click', function () {
      video.load();
      loadingIndicator.style.display = 'block';
  });

  loadButton.addEventListener('click', function () {
      const videoUrl = videoInput.value;
      if (videoUrl) {
          videoSource.src = videoUrl;
          video.load();
          loadingIndicator.style.display = 'block';
      }
  });

  video.addEventListener('canplay', function () {
      loadingIndicator.style.display = 'none';
  });
});