# Name: Views for face Detect
# Main Job: Used to describe views for face detect
#
# Author: Anirban Roy Chowdhury
# Craated Date: 30 March 2021
# Version: 1.1.0
# ClassID# 1000

# Class Usage
#   1. helps return views for face Detection.
#	2. video_feed is a POST API which taken the images from the client side applies the opencv processing and then returns an JSON containing the utf-8 encoded image, and bool value of alarm

from django.shortcuts import render
from django.http import HttpResponse
from facedetectionapp.camera import *
from facedetectionapp.process import *
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
import json
from django.core.files.base import ContentFile

#Get user camera through javascript
# webopencv() function to initialize class from process

# camera = Camera(webopencv())
cameraList = {}

def index_view(request, *args, **kwargs):
	request.session.create()
	sessionID = request.session.session_key
	if sessionID not in cameraList:
		camera = Camera(webopencv(),sessionID)
		cameraList[sessionID] = camera
	return render(request,'faceDetect.html',{})


#Converts the gives file into base64 and enques it into the image queue
@csrf_exempt
def video_feed(request, *args, **kwargs):
	#IF request is POST
	if request.method == 'POST':
		sessionID = request.session.session_key
		if sessionID in cameraList:
			print("Gettting camera from list")
			camera = cameraList[sessionID]
		else:
			print("creating camera and appending to dict from video_feed")
			camera = Camera(webopencv(),sessionID)
			cameraList[sessionID] = camera
		print(camera.getID())
		_format, _data = str(request.body).split(';base64,')
		#Convert the string into an image
		file = ContentFile( base64.b64decode(_data))
		#Open image
		img = Image.open(file)
		#Enqueue
		camera.enqueue_input(img)
		#Get processed image
		processedResult = camera.get_frame()
		#Create dict for response
		res = {'camera_frame':processedResult[0],'alarm':processedResult[1]}
		#Convert to Json and send response
		return HttpResponse(json.dumps(res),content_type='application/json')


        