import RPi.GPIO as GPIO          #import libraries
import time
import os
from numpy import arange

GPIO.setmode(GPIO.BCM)           #set BCM mode


GPIO.setup(6, GPIO.OUT)          #set all the pins for IN/OUT
GPIO.setup(5, GPIO.OUT)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)

start_time=time.time()

p=GPIO.PWM(6,46.51)           #initialize the pwm pbject for pins
p1=GPIO.PWM(5,46.51)
while True:                   #poll the loop
	left_fwd=GPIO.input(17)   #set the variables for GPIO
	left_stp=GPIO.input(22)
	left_bwd=GPIO.input(23)
	right_fwd=GPIO.input(27)
	right_stp=GPIO.input(13)
	right_bwd=GPIO.input(19)
	


	if left_fwd==False:   #condition for left forward
		p.start(6.2)

	elif left_stp==False:  #condition for left stop
		p.ChangeDutyCycle(0)

		
	elif left_bwd==False:     #condition for left back
		#p.stop()
		p.start(7.7)
	elif right_fwd==False:   #condition for right forward
		p1.start(6.2)
		
	elif right_stp==False:  #condition for right stop
		p1.ChangeDutyCycle(0)

	elif right_bwd==False:     #condition for right back
		#p1.stop()
		p1.start(7.7)
	if (time.time()-start_time)>60: #exit if running for 1 min
		GPIO.cleanup()
		quit()	





