let videoWidth, videoHeight;

// whether streaming video from the camera.
let streaming = false;

let video = document.getElementById('video');
let ret_img = document.getElementById('returned-image');
// let canvasOutput = document.getElementById('canvasOutput');
// let canvasOutputCtx = canvasOutput.getContext('2d');
let stream = null;


let src = null;
let dstC1 = null;
let dstC3 = null;
let dstC4 = null;


function startCamera() {
  if (streaming) return;
  navigator.mediaDevices.getUserMedia({video: true, audio: false})
    .then(function(s) {
    stream = s;
    video.srcObject = s;
    video.play();
    setInterval(function() {
      startVideoProcessing()
    }, 500);
  })
    .catch(function(err) {
    console.log("An error occured! " + err);
  });

  video.addEventListener("canplay", function(ev){
    if (!streaming) {
      videoWidth = video.videoWidth;
      videoHeight = video.videoHeight;
      video.setAttribute("width", videoWidth);
      video.setAttribute("height", videoHeight);
      // canvasOutput.width = videoWidth;
      // canvasOutput.height = videoHeight;
      streaming = true;
    }
    startVideoProcessing();
  }, false);
}

function startVideoProcessing() {
  if (!streaming) { console.warn("Please startup your webcam"); return; }
  // stopVideoProcessing();
  canvasInput = document.createElement('canvas');
  canvasInput.width = videoWidth;
  canvasInput.height = videoHeight;
  canvasInputCtx = canvasInput.getContext('2d');
  
  // canvasBuffer = document.createElement('canvas');
  // canvasBuffer.width = videoWidth;
  // canvasBuffer.height = videoHeight;
  // canvasBufferCtx = canvasBuffer.getContext('2d');

  canvasInputCtx.drawImage(video,0,0);
  let dataURL = canvasInput.toDataURL('image/jpeg');
  var xhr = new XMLHttpRequest();
  xhr.open("POST", "/video", true);
  xhr.responseType = "text";
  xhr.onload = response;
  xhr.send(dataURL);
}

function response(e) {
  var imageUrl = 'data:image/bmp;base64,'+this.response
  ret_img.src = imageUrl;
}

function stopVideoProcessing() {
  if (src != null && !src.isDeleted()) src.delete();
  if (dstC1 != null && !dstC1.isDeleted()) dstC1.delete();
  if (dstC3 != null && !dstC3.isDeleted()) dstC3.delete();
  if (dstC4 != null && !dstC4.isDeleted()) dstC4.delete();
}



function opencvIsReady() {
    console.log('OpenCV.js is ready');
    startCamera();
    
  }