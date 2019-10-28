#!/usr/bin/python3
############################################################
# Class SmartPiCamContr
# This class realizes the application control code for
# the pi using a camera and a Edge TPU for inferencing.
#
# File: smartCamContr.py
# Author: Detlef Heinze 
# Version: 1.3     Date: 28.10.2019       
###########################################################
from picamera import PiCamera
from time import sleep
from edgetpu.detection.engine import DetectionEngine
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
        
        modelFile= 'mobilenet_ssd_v2_coco_quant_postprocess_edgetpu.tflite'
        objectLabelsFile= 'coco_labels.txt'
        print("Reading Model: ", modelFile)
        self.engine= DetectionEngine(modelFile)
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
        flatArray= picData.flatten() #3D to 1D conversion
        print('Input array size: ', flatArray.shape)
        #Call the TPU to detect objects on the image with a neural network
        result = self.engine.detect_with_input_tensor(flatArray,
                                                      threshold=self.minObjectScore,
                                                      top_k=10)
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
                if obj.label_id in objectIdsOfInterest:
                    if self.labels:
                        lbl= self.labels[obj.label_id]
                        print(lbl, obj.label_id)
                    print ('score = ', obj.score)
                    box = obj.bounding_box.flatten()
                    box *= self.cameraResolution[1]  #scale up to resolution
                    print ('box = ', box.tolist())
                    detectedObjList.append( (lbl, box) )
        if len(detectedObjList) == 0:
            print ('No object detected!')
        return detectedObjList
    
    #Step 15: Depending on the detected objects and location
    #take desired action
    def processResult(self, detectedObjects):
        print('Number of detected objects: ', len(detectedObjects))
                
    
    