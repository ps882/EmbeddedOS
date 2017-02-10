import RPi.GPIO as GPIO          #import important libraries
import time
import os


GPIO.setmode(GPIO.BCM)            #set BCM mode for GPIO


GPIO.setup(6, GPIO.OUT)           #set 6th pin as OUT pin
p=GPIO.PWM(6,50)                  #set the pin 6 at freq 50
p.start(0)
try:
	while 1:                     #polling loop
			for dc in range (0,101,5):      #inc dc
					p.ChangeDutyCycle(dc)
					time.sleep(0.1)
			for dc in range (100,-1,-5):   #dec dc for anti
				p.ChangeDutyCycle(dc)
				time.sleep(0.1)
except q:
	pass
p.stop()                                #stop the pwm
GPIO.cleanup()
quit()                          #exit out of loop
 