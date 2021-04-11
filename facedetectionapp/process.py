import cv2 as cv2
import dlib
import base64
from scipy.spatial import distance as dist
import numpy as np
from PIL import Image
from threading import Thread
import time
from django.core.files.base import ContentFile
import io

    #Convert to np array
def shape_to_np(shape, dtype="int"):
    # initialize the list of (x, y)-coordinates
    coords = np.zeros((shape.num_parts, 2), dtype=dtype)
    # loop over all facial landmarks and convert them
    # to a 2-tuple of (x, y)-coordinates
    for i in range(0, shape.num_parts):
        coords[i] = (shape.part(i).x, shape.part(i).y)
    # return the list of (x, y)-coordinates
    return coords

#Calculate Eye Aspect Ratio
def eye_aspect_ratio(eye):
    # compute the euclidean distances between the two sets of
    # vertical eye landmarks (x, y)-coordinates
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    # compute the euclidean distance between the horizontal
    # eye landmark (x, y)-coordinates
    C = dist.euclidean(eye[0], eye[3])
    # compute the eye aspect ratio
    ear = (A + B) / (2.0 * C)
    # return the eye aspect ratio
    return float(ear)

class webopencv(object):
    def __init__(self):
        # defining face detector & predictor
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor('static/shape_predictor_68_face_landmarks.dat')
        # define two constants, one for the eye aspect ratio to indicate
        # blink and then a second constant for the number of consecutive
        # frames the eye must be below the threshold for to set off the
        # alarm
        self.EYE_AR_THRESH = 0.3
        self.EYE_AR_CONSEC_FRAMES = 28
        # initialize the frame counter as well as a boolean used to
        # indicate if the alarm is going off
        self.COUNTER = 0
        self.ALARM_ON = False
        #Grab left and right eye indices
        self.lStart = 42
        self.lEnd = 48
        self.rStart = 36
        self.rEnd = 42
        pass

    def process(self, img):
        frame = np.array(img)
        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.detector(grayFrame,0)
        for face in faces:
            shape = self.predictor(grayFrame,face)
            shape = shape_to_np(shape)
            #Extract left and right eye using defined coordinates
            leftEye = shape[self.lStart:self.lEnd]
            rightEye = shape[self.rStart:self.rEnd]
            #Get eye aspect ratio(EAR)
            leftEAR = eye_aspect_ratio(leftEye)
            rightEAR = eye_aspect_ratio(rightEye)
            #Get avg eye aspect ratio
            avgEAR = float((leftEAR+rightEAR)/2.0)
            #compute convex hull
            leftEyeHull = cv2.convexHull(leftEye)
            rightEyeHull = cv2.convexHull(rightEye)
            #Visualize each eye
            cv2.drawContours(frame,[leftEyeHull], -1, (0,255,0), 1)
            cv2.drawContours(frame,[rightEyeHull], -1, (0,255,0), 1)
            if avgEAR < self.EYE_AR_THRESH:
                self.COUNTER += 1
                print(self.COUNTER)
                if self.COUNTER >= self.EYE_AR_CONSEC_FRAMES:
                    cv2.putText(frame,'ALERT!!!',(10,30),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),1) 
            else:
                self.COUNTER = 0
            #Add text showing ratio
            cv2.putText(frame,"EAR: {:.2f}".format(avgEAR), (300, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        ret, jpeg = cv2.imencode('.jpg',frame)
        jpeg_b64 = base64.b64encode(jpeg)
        return jpeg_b64
