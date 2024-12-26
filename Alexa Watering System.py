import cv2
from PIL import Image
import pytesseract
import pyttsx3
import cv2
from time import sleep
import tensorflow as tf
import time
import numpy as np
from darkflow.net.build import TFNet


import serial
ser = serial.Serial('COM5',baudrate='9600',timeout=1)
ser.flushInput()
def serial():
    print("press button with in 15 sec....")
    sleep(10)
    a1 = ser.readline().decode('ascii')
    print(a1)
    if(a1=="1"):
        headset()
    elif(a1=="2"):
        vibration()
 
   
##serial 1
def headset():
    pytesseract.pytesseract.tesseract_cmd ='C:/Program Files/Tesseract-OCR/Tesseract.exe'
    en = pyttsx3.init()
    en.setProperty('rate', 80)

    cap = cv2.VideoCapture(0)
    #print("ok")  
    ret, frame = cap.read()
    #frame = cv2.imread("1.png")
    cv2.imshow('frame',frame)
    cv2.imwrite("1.jpg",frame)
    img =Image.open ("1.jpg")
    text = pytesseract.image_to_string(img, config="")
    print (text)
    en.say(text)
    en.runAndWait()
    serial()


##serial 2
def vibration():
    pytesseract.pytesseract.tesseract_cmd ='C:/Program Files/Tesseract-OCR/Tesseract.exe'
    en = pyttsx3.init()
    en.setProperty('rate', 80)

    cap = cv2.VideoCapture(0)
    #print("ok")  
    ret, frame = cap.read()
    #frame = cv2.imread("1.png")
    cv2.imshow('frame',frame)
    cv2.imwrite("1.jpg",frame)
    img =Image.open ("1.jpg")
    text = pytesseract.image_to_string(img, config="")
    print (text)
    en.say(text)
    en.runAndWait()
    ser.write('2'.encode())
    serial()
