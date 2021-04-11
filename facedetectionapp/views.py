from django.shortcuts import render
from django.http import StreamingHttpResponse, HttpResponse
from facedetectionapp.camera import *
from facedetectionapp.process import *
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
import time
from django.core.files.base import ContentFile
import io

camera = Camera(webopencv())


def index_view(request, *args, **kwargs):
    """Video streaming home page."""
 
    return render(request,'faceDetect.html',{'image':""})


def gen(camera):
    """Video streaming generator function."""

    # app.logger.info("starting to generate frames!")
    print("Starting to generate frames")
    while True:
        frame = camera.get_frame() #pil_image_to_base64(camera.get_frame())
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@csrf_exempt
def video_feed(request, *args, **kwargs):
    if request.method == 'POST':
        # print(request.body)
        _format, _data = str(request.body).split(';base64,')
        file = ContentFile( base64.b64decode(_data))
        img = Image.open(file)
        camera.enqueue_input(img)
        camera_frame = camera.get_frame()
        return HttpResponse(camera_frame)
        