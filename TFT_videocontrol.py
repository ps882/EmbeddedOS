#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import os


GPIO.setmode(GPIO.BCM)


GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

status_flag=0


while True:
play_status= GPIO.input(17)
vid_fwd= GPIO.input(22)
vid_bwd= GPIO.input(23)
vid_quit= GPIO.input(27)


if play_status == False:
if status_flag:
status_flag=0
print('Video has been unpaused')
with open("/home/pi/fifos/mplayer","w") as fifo:
fifo.write("pause" + "\n")
time.sleep(0.3)
else:
status_flag=1
print('Video has been paused')
with open("/home/pi/fifos/mplayer","w") as fifo:
                                fifo.write("pause" + "\n")
time.sleep(0.3)
elif vid_fwd == False:
print('Video has been forwarded by 10 sec')
with open("/home/pi/fifos/mplayer","w") as fifo:
fifo.write("seek 10" + "\n") 
        time.sleep(0.3)
elif vid_bwd == False:
print('Video has been backwarded by 10 sec')
with open("/home/pi/fifos/mplayer","w") as fifo:
fifo.write("seek -10" + "\n") 
        time.sleep(0.3)
elif vid_quit == False:
print('Video has been exited')
with open("/home/pi/fifos/mplayer","w") as fifo:
fifo.write("quit" + "\n") 
        time.sleep(0.3)
exit()
