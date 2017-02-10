
import RPi.GPIO as GPIO     #import the libraries
import time
import os
from numpy import arange

GPIO.setmode(GPIO.BCM)     #set BCM mode


GPIO.setup(6, GPIO.OUT)   #set the servo pins as out
GPIO.setup(5, GPIO.OUT)

p=GPIO.PWM(5,46.51)       #initialize the pwm objects
p1=GPIO.PWM(6,46.51)


p.start(6.4)             #start the servos, forward 1 foot
p1.start(7.3)
time.sleep(3)
p.ChangeDutyCycle(0)
p1.ChangeDutyCycle(0)
time.sleep(1)


p.start(7.3)           #reverse the directions, backward 1 foot
p1.start(6.4)
time.sleep(3)
p.ChangeDutyCycle(0)
p1.ChangeDutyCycle(0)
time.sleep(1)

p.start(6.4)             #move in same direction, pivot left
p1.start(6.4)
time.sleep(1)           #sleep for 1 sec
p.ChangeDutyCycle(0)
p1.ChangeDutyCycle(0)
time.sleep(1)
p.start(7.3)            #pivot right
p1.start(7.3)
time.sleep(1.5)
p.ChangeDutyCycle(0)
p1.ChangeDutyCycle(0)
time.sleep(1)


