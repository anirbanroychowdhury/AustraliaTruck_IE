# Name: Process file mian use is for helper functions to detect eyes and drowsiness
# Main Job: Has helper functions for eye and fatigue detection
#
# Author: Anirban Roy Chowdhury
# Craated Date: 30 March 2021
# Version: 1.1.0
# ClassID# 1000

# Class Usage
#   1. Has helper function for OpenCV
#   2.returns the jpeg coded frame after processing

import cv2 as cv2
import dlib
import base64
from scipy.spatial import distance as dist
import numpy as np


def get_top_lip_center(landmarks):
    top_lip_pts = []
    for i in range(50,53):
        top_lip_pts.append(landmarks[i])
    for i in range(61,64):
        top_lip_pts.append(landmarks[i])
    top_lip_all_pts = np.squeeze(np.asarray(top_lip_pts))
    top_lip_mean = np.mean(top_lip_pts, axis=0)
#     print("top lip: %s",top_lip_mean[1])
    return int(top_lip_mean[1])

def get_bottom_lip_center(landmarks):
    bottom_lip_pts = []
    for i in range(65,68):
        bottom_lip_pts.append(landmarks[i])
    for i in range(56,59):
        bottom_lip_pts.append(landmarks[i])
    bottom_lip_all_pts = np.squeeze(np.asarray(bottom_lip_pts))
    bottom_lip_mean = np.mean(bottom_lip_pts, axis=0)
#     print("bottom lip: %s",bottom_lip_mean[1])
    return int(bottom_lip_mean[1])

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
        self.EYE_AR_THRESH = 0.36
        self.EYE_AR_CONSEC_FRAMES = 10
        # initialize the frame counter as well as a boolean used to
        # indicate if the alarm is going off
        self.COUNTER = 0
        self.ALARM_ON = False
        #Grab left and right eye indices
        self.lStart = 42
        self.lEnd = 48
        self.rStart = 36
        self.rEnd = 42
        #Grab top and bottom lips
        # self.topLipStart = 
        #Count of eye blinks
        self.EYE_BLINK_COUNT = 0
        self.YAWN_COUNT = 0

    def process(self, img):
        #Get frame in np array
        frame = np.array(img)
        #Convert to gray 
        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #Detect faces
        faces = self.detector(grayFrame,1)
        #for each face
        for face in faces:
            #predict face in image
            shape = self.predictor(grayFrame,face)
            #change shape
            shape = shape_to_np(shape)
            #Extract left and right eye using defined coordinates
            leftEye = shape[self.lStart:self.lEnd]
            rightEye = shape[self.rStart:self.rEnd]
            #Get mouth
            mouth = shape[49:68]
            #Get eye aspect ratio(EAR)
            leftEAR = eye_aspect_ratio(leftEye)
            rightEAR = eye_aspect_ratio(rightEye)
            #GET top and bottom lip center
            topLipCenter = get_top_lip_center(shape)
            bottomLipCenter = get_bottom_lip_center(shape)
            #calculate lip distance between top and bottom
            lipDistance = abs(topLipCenter-bottomLipCenter)
#             print("Lip distance is",lipDistance)
            #Get avg eye aspect ratio
            avgEAR = float((leftEAR+rightEAR)/2.0)
            #compute convex hull
            leftEyeHull = cv2.convexHull(leftEye)
            rightEyeHull = cv2.convexHull(rightEye)
            #compute convex hull
            mouthHull = cv2.convexHull(mouth)
            #Visualize each eye and mouth
            cv2.drawContours(frame,[leftEyeHull], -1, (0,255,0), 1)
            cv2.drawContours(frame,[rightEyeHull], -1, (0,255,0), 1)
            cv2.drawContours(frame,[mouthHull], -1, (0,255,0), 1)
            if lipDistance > 25:
                self.YAWN_COUNT += 1
            if avgEAR < self.EYE_AR_THRESH:
                print(f'counter inside threshold{self.COUNTER}')
                self.EYE_BLINK_COUNT += 1
                self.COUNTER += 1
                if self.COUNTER >= self.EYE_AR_CONSEC_FRAMES:
                    if not self.ALARM_ON:
                        self.ALARM_ON = True
                    cv2.putText(frame,'ALERT!!!',(10,30),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),1) 
            else:
                self.ALARM_ON = False
                self.COUNTER = 0
                # self.EYE_BLINK_COUNT = 0
                # self.YAWN_COUNT = 0
            #Add text showing ratio
            cv2.putText(frame,"EAR: {:.2f}".format(avgEAR), (300, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            cv2.putText(frame,"You have blinked: {:.2f}".format(self.EYE_BLINK_COUNT), (300, 50),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            cv2.putText(frame,"Yawn Count: {:.2f}".format(self.YAWN_COUNT), (300, 70),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        ret, jpeg = cv2.imencode('.jpg',frame)
        jpeg_b64 = base64.b64encode(jpeg)
        jpeg_b64 = jpeg_b64.decode('utf-8')
        data = [jpeg_b64,self.ALARM_ON]
        return data
