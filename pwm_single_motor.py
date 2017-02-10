import RPi.GPIO as GPIO       #import the libraries
import time
import os


GPIO.setmode(GPIO.BCM)    #set BCM mode for GPIO


GPIO.setup(6, GPIO.OUT)   # set pin as OUT
p=GPIO.PWM(6,46.51)       #initialize the freq on pin6
p.start(6.97)             #set the initial dutycycle to 6.97

time.sleep(30)            #sleep while calibrating
GPIO.cleanup()
