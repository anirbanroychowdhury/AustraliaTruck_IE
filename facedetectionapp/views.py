# Name: Views for face Detect
# Main Job: Used to describe views for face detect
#
# Author: Anirban Roy Chowdhury
# Craated Date: 30 March 2021
# Version: 1.1.0
# ClassID# 1000

# Class Usage
#   1. helps return views for face Detection.
#	2. Gen() creates a stream of images and video_feed displays it

from django.shortcuts import render
from django.http import HttpResponse
from facedetectionapp.camera import *
from facedetectionapp.process import *
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
import json
from django.core.files.base import ContentFile

camera = Camera(webopencv())


def index_view(request, *args, **kwargs):
    """Video streaming home page."""
 
    return render(request,'faceDetect.html',{'image':""})


def gen(camera):
    """Video streaming generator function."""
    while True:
		#Get the next frame from queue
        frame = camera.get_frame()
		#yeild the frame
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

#Converts the gives file into base64 and enques it into the image queue
@csrf_exempt
def video_feed(request, *args, **kwargs):
	#IF request is POST
	if request.method == 'POST':
		_format, _data = str(request.body).split(';base64,')
		#Convert the string into an image
		file = ContentFile( base64.b64decode(_data))
		#Open image
		img = Image.open(file)
		#Enqueue
		camera.enqueue_input(img)
		camera_frame = camera.get_frame()
		data = {'camera_frame':camera_frame[0],'alarm':camera_frame[1]}
		return HttpResponse(json.dumps(data),content_type='application/json')
        