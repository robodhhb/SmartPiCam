#!/usr/bin/python3
############################################################
# File smartPiCamMainNoDisp.py
# This is the main application file for the smart Pi camera.
# It implements object detection with the Coral USB
# Accelarotor (Edge TPU Coprozessor) using a model
# trained on the COCO dataset. The code for display of 
# images is removed for increasing performance..
#
# File: smartPiCamMainNoDisp.py
# Author: Detlef Heinze 
# Version: 1.0      Date: 06.04.2019       
###########################################################

from tkinter import *
import time 
from PIL import Image, ImageTk
import smartPiCamContr as SPCC_Contr


#IDs of objects of interest to be detected
#for this application. 43 = bottle, 52 = apple in COCO-Dataset
objectIdsOfInterest = { 43, 52} 

#Terminate program
def terminate():
    print("Program terminates")
    camera.close()
    appWin.destroy()

#Create controller and warm up cam
print('SmartPiCam Application (No Display) 1.0\n')
spcc= SPCC_Contr.SmartPiCamContr()
camera= spcc.configurePiCam()
count=0

#Create main application wmindow
appWin = Tk()
appWin.wm_title("Smart PiCam 1.0")
lblPicTaken= Label(appWin, text="No picture is displayed for higher performance")
lblPicTaken.pack(anchor=W, pady=5)

#Start main loop of application
timeout = time.time() + spcc.appDuration

print('\nApplication starts...\n')
appWin.update()
while time.time() < timeout:
    picData= spcc.takePhoto()
    #Run neural network on Edge TPU Accelarotor
    result= spcc.predict(picData)
    
    detectedObjects= spcc.analyseResult(result, objectIdsOfInterest)
    spcc.processResult(detectedObjects)
    count += 1
print("\nDuration of running application has been reached.")
print("Number of processed images: ", count)
print("Duration: ", spcc.appDuration, "seconds.")
terminate()
