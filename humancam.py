#!/ubr/bin/env python
# -*- coding: utf-8 -*-
import io
import RPi.GPIO as GPIO
import time
import picamera
import cv2
import numpy as np

faceCade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml')
pin = 2 #set ledpin
camera = picamera.PiCamera() #set camera
camera.resolution = (320, 240)
camera.rotation = 180
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
i=0

def humancam():
    while 1:
        start = time.clock() 
        camera.capture('i.jpg')
        image = cv2.imread('i.jpg', cv2.IMREAD_COLOR)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        face = faceCade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=2, minSize=(30, 30))

        if len(face) > 0 :
            for rect in face :
                cv2.rectangle(image, tuple(rect[0:2]), tuple(rect[0:2]+rect[2:4]), (0,0,255), thickness=2)
            GPIO.output(pin, True)
        else:
            GPIO.output(pin, False)

        get_image_time = int((time.clock()-start)*1000)
        cv2.putText(image, str(get_image_time)+"ms", (10, 10), 1, 1, (255, 0, 0))
        cv2.imshow("Camera Test", image)
        if cv2.waitKey(1) == 32 : #32:[Space]
            cv2.imwrite(str(i)+".jpg", image)
            i+=1
            print("Save Image..."+str(i)+".jpg")
        elif cv2.waitKey(1) == 27 : #27:[Esc]
            cv2.destroyAllWindows()
            break
"""
1. make html on python
2. type keybord
3. led light
4. debug
"""

if __name__=='__main__':
    humancam()
