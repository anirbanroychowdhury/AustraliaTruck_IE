# Name: Camera Queue
# Main Job: initaite a camera at the start of app opening, it will create a queue to display the frames in order
#
# Author: Anirban Roy Chowdhury
# Craated Date: 30 March 2021
# Version: 1.1.0
# ClassID# 1000

# Class Usage
#   1. Camera class is used to manage the frames and its respective queueu

import threading
from time import sleep


class Camera(object):
    #Creates a Camera object
    def __init__(self, process):
        self.to_process = []
        self.to_output = []
        self.to_alarm = []
        self.process = process
        #Create and start a thread when an pbject is initiated
        thread = threading.Thread(target=self.keep_processing, args=())
        thread.daemon = True
        thread.start()

    #if the queue has a frame send the frame to be displayed
    def process_one(self):
        if not self.to_process:
            return
        #Get the frame
        camera_frame = self.to_process.pop(0)
        #process it using OpenCV and get the result
        #result[0] - proessed frame
        #result[1] - Alarm boolean value
        #result[2] - No of eye blinks
        result = self.process.process(camera_frame)
        #append the results in their respective queues
        self.to_output.append(result[0])
        self.to_alarm.append(result[1])
        # print(result[2])
    
    #keep sending the images
    def keep_processing(self):
        while True:
            self.process_one()

    #Add an image to the queue
    def enqueue_input(self, input):
        self.to_process.append(input)

    #Get the image to be displayed if the queue is not empty
    def get_frame(self):
        while not self.to_output:
            sleep(0.01)
        data = [self.to_output.pop(0),self.to_alarm.pop(0)]
        return data
