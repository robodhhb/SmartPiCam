Installation der SmartPiCam Applikation (see English Version below)
===================================================================
Voraussetzung: Raspberry Pi 2/3 Model B/B+ and 4 mit Raspbian/ Pi OS
Getestet auf Model 3 B+ mit: 
     - Raspbian/ Pi OS Buster und Python 3.7.3 


Empfohlen: Update von Raspbian/ Pi OS
- sudo apt update
- sudo apt full-upgrade

Die Installation besteht aus:

1) Raspbian/Pi OS z.B. installiert mit NOOBS
   Siehe https://www.raspberrypi.org/help/
   und https://www.raspberrypi.org/documentation/installation/
   
2) Anmeldung als user "pi". 
 
3) Setup der Raspberry Pi Camera V2:
   Siehe https://www.raspberrypi.org/documentation/configuration/camera.md

4) Optional: Zugriff auf den Pi über VNC von einem PC aus:
   https://www.raspberrypi.org/documentation/remote-access/vnc/README.md

5) Installation der Edge TPU:
   Achtung: Erst SW installieren, dann Edge TPU über USB anschließen!
   Siehe den Get Started Giude:
   https://coral.withgoogle.com/docs/accelerator/get-started/
   Installation:
        1) Install Edge TPU Runtime
        2) Install TensorFlow Lite API
        3) Install PyCoral API
           https://coral.ai/docs/edgetpu/tflite-python/#run-an-inference-with-the-pycoral-api
   Es reicht aus, die Edge TPU mit "default operating frequency" zu installieren.
   
6) Download des GitHub-Repository 
   auf dem Raspberry Pi unter dem user "pi":
   https://github.com/robodhhb/SmartPiCam

7) LXTerminal öffnen und zip-Datei mit unzip in einem Ordner Ihrer Wahl entpacken
   
8) In den Ordner "SmartPiCam_with_PyCoral_API" mit cd wechslen

9) Programm starten:
    python3 smartPiCamMain.py
   
Bekannte Probleme:
a)  Falls das Paket "ImageTk" nicht gefunden wird, muss es noch
    installiert werden mit:
    sudo apt install python3-pil.imagetk

b) Meldung nach dem Laden des Modells:
   W0422 10:54:13.042898    2007 package_registry.cc:65] 
   Minimum runtime version required by package (5) is lower than expected (10)
   Google arbeitet an diesem Progblem, das jedoch kein Auswirkung auf das Program hat.
   Die Meldung kann ignoriert werden. 


    
========================English Version====================================
Installation of the application "SmartPiCam"
--------------------------------------------
Prerequisite: Raspberry Pi 2/3 Model B/B+ and 4 with Raspbian/PI OS 
Tested on Model 3 B+ with:
     - Raspbian/ Pi OS Buster und Python 3.7.3 

Recommended: Update of Raspbian/ Pi OS
- sudo apt update
- sudo apt full-upgrade

Installation steps:

1) Install Raspbian e.g. with NOOBS
   See https://www.raspberrypi.org/help/
   and https://www.raspberrypi.org/documentation/installation/
   
2) Login as user "pi". 
 
3) Setup  Raspberry Pi Camera V2:
   See https://www.raspberrypi.org/documentation/configuration/camera.md

4) Optional: Access the Pi desktop with VNC via a PC:
   https://www.raspberrypi.org/documentation/remote-access/vnc/README.md

5) Installation of the Edge TPU:
   Caution: First install the software then connect Edge TPU to the USB-Port!
   See: Get started guide:
   https://coral.withgoogle.com/docs/accelerator/get-started/
   Installation:
        1) Install Edge TPU Runtime
        2) Install TensorFlow Lite API
        3) Install PyCoral API
           https://coral.ai/docs/edgetpu/tflite-python/#run-an-inference-with-the-pycoral-api
   It is sufficient to install the Edge TPU with default operating frequency.
   
6) Download the GitHub-Repository 
   on the Raspberry Pi under the user "pi":
   https://github.com/robodhhb/SmartPiCam
   
7) Open LXTerminal and unzip downloaded file in a folder of your choice
   
8) Change directory to "SmartPiCam_with_PyCoral_API"

9) Run the program:
    python3 smartPiCamMain.py
   
Known issues:
a)  If the paket "ImageTk" cannot be found, it has to be installed with:
    sudo apt install python3-pil.imagetk

b) After loading the model, the following message can be ignored. 
   Google is working on it.
   W0422 10:54:13.042898    2007 package_registry.cc:65] 
   Minimum runtime version required by package (5) is lower than expected (10)


 
      
   

