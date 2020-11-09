#!/usr/bin/python3
############################################################
# Class SmartPiCamContr
# This class realizes the application control code for
# the pi using a camera and a Edge TPU for inferencing.
# The EdgeTPU is accessed via the PyCoral-API
#
# File: smartCamContr.py
# Author: Detlef Heinze 
# Version: 1.5     Date: 9.11.2020      
###########################################################
from picamera import PiCamera
from time import sleep
from pycoral.utils import edgetpu
from pycoral.utils import dataset
from pycoral.adapters import common
from pycoral.adapters import detect
from PIL import Image
import numpy as np

class SmartPiCamContr(object):
    
    # Step 2: Constructor which defines default values for settings
    def __init__(self, appDuration=30,
                 cameraResolution= (304, 304),
                 useVideoPort = True,
                 minObjectScore= 0.35):
        self.cameraResolution= cameraResolution
        self.useVideoPort= useVideoPort
        self.appDuration= appDuration #seconds to run
        self.minObjectScore= minObjectScore
        
        modelFile= 'ssd_mobilenet_v2_coco_quant_postprocess_edgetpu.tflite'
        objectLabelsFile= 'coco_labels.txt'
        print("Reading Model: ", modelFile)
        
        # Initialize the TF interpreter
        self.interpreter = edgetpu.make_interpreter(modelFile)
        self.interpreter.allocate_tensors()
        
        print("Reading object labels: ", objectLabelsFile)
        self.labels= self.readLabelFile(objectLabelsFile)
        print("Minimal object score: ", self.minObjectScore)
        
   
    # Step 4: Configure PiCam
    # Return parameter: created PiCam
    def configurePiCam(self):
        print("\nConfigure and warming up PiCamera")
        self.cam = PiCamera()
        self.cam.resolution= self.cameraResolution
        print("Camera resolution: " + repr(self.cam.resolution))
        self.cam.start_preview()
        sleep(2)
        self.cam.stop_preview()
        return self.cam
    
    #Step 7: Take a photo returned as numpy array
    def takePhoto(self):
        picData = np.empty((self.cameraResolution[1],
                            self.cameraResolution[0], 3),
                            dtype=np.uint8)
        self.cam.capture(picData, format= 'rgb', use_video_port=self.useVideoPort) #24bit rgb format
        # Coco-Model requires 300 x 300 resolution
        # Remove last 4 rows and last 4 colummns in all 3 dimensions
        picData= picData[:-4, :-4]
        return picData
    
    # Function to read labels from text files.
    def readLabelFile(self, file_path):
        with open(file_path, 'r') as f:
            lines = f.readlines()
        ret = {}
        for line in lines:
            pair = line.strip().split(maxsplit=1)
            ret[int(pair[0])] = pair[1].strip()
        return ret

    #Step 10: Predict the picture by running it on the TPU
    def predict(self, picData):
        print("\nPredicting imgage on TPU")
        print('Shape of data: ', picData.shape)
        #Call the TPU to detect objects on the image with a neural network
        common.set_input(self.interpreter, picData)
        self.interpreter.invoke()
        result=  detect.get_objects(self.interpreter, self.minObjectScore)
        
        return result
    
    #Step 12: Analyse the result of inferencing on the TPU.
    #The result is analysed and all objects will be set as detected
    #if they belong to the objects IDs of interest
    def analyseResult(self, predResult, objectIdsOfInterest):
        print ("Analysing results...")
        detectedObjList= []
        lbl= ''
        if predResult:
            for obj in predResult:
                if obj.id in objectIdsOfInterest:
                    if self.labels:
                        lbl= self.labels[obj.id]
                        print(lbl, obj.id)
                    print ('score = ', obj.score)
                    box= (obj.bbox.xmin, obj.bbox.ymax,
                          obj.bbox.xmax, obj.bbox.ymin) 
                    print ('box = ', box)
                    detectedObjList.append( (lbl,box ))
        if len(detectedObjList) == 0:
            print ('No object detected!')
        return detectedObjList
    
    #Step 15: Depending on the detected objects and location
    #take desired action
    def processResult(self, detectedObjects):
        print('Number of detected objects: ', len(detectedObjects))
                
    
    