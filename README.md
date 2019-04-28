# SmartPiCam
Real time object detection with Raspberry Pi, Google Edge TPU and Python

Willkommen bei der SmartPiCam! (see English version below)

Dieses Projekt realisiert eine smarte Kamera mit dem Raspberry Pi, die in Echtzeit mit Hilfe der 
Edge TPU von Google die Objekte "Apfel" und "Flasche" erkennt. Das neuronale Netz basiert auf einem von Google trainierten Modell
auf Basis des COCO-Datensatzes mit der Architektur "MobileNet SSD v2". Das Inferencing findet auf der Edge TPU statt. Der Raspberry Pi
kann dadurch 6 - 7,3 Bilder pro Sekunde anzeigen und erkannte Objekte kennzeichnen(TPU Konfiguration mit normaler Geschwindigkeit).
Die Bilder haben eine Auflösung von 300 x 300 Pixel. Das "Video SmartPiCam HD" zeigt eine Aufnahme
des Desktops vom Raspberry Pi in Echtzeit. Im Ordner "SmartPiCam" befinden sich eine Installationsanleitung
und die Python Quellen.

Welcome to the SmartPiCam!

This project realizes a smart camera with the Raspberry Pi. It detects the objects "apple" and "bottle" in real time using 
the Edge TPU from Google. The neural network is based on a model trained at Google on basis of the
COCO-Dataset with the architecture "MobileNet SSD v2". Inferencing is executed on the Edge TPU. 
The Raspberry Pi is therefore able to detect and mark objects on 6 - 7.3 pictures per second 
(TPU configuration with default operating frequency). The pictures have a resolution of 300 x 300 Pixel. 
The "Video SmartPiCam HD" shows a real time recording of the pi's desktop. See folder "SmartPiCam" 
for an installation manual and the python sources.
