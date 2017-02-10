
import RPi.GPIO as GPIO           #import libraries
import time
import os
from numpy import arange

GPIO.setmode(GPIO.BCM)           #set BCM mode for GPIO


GPIO.setup(6, GPIO.OUT)           #set pin as OUT GPIO
p=GPIO.PWM(6,46.51)               #initialize the pwm object
p.start(6.97)                     #initialize the dc to stop
for dc in arange (6.97,6.1,-0.07):  #inc the dc variable
        p.ChangeDutyCycle(dc)       #give new value to p object
        print dc
        time.sleep(3)             #sleep for 3 sec
for dc in arange (6.97,7.8,0.101):  #dec the dc variable
	p.ChangeDutyCycle(dc)        #set the new value of p object
	print dc 
        time.sleep(3)

p.stop()                         #stop the object
GPIO.cleanup()                   #cleanup GPIO pin initialization
quit()
