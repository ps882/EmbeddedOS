#!/usr/bin/python

import subprocess


#file_name=raw_input("Enter the video file you want to play > ")
#print file_name

while True:
# subprocess.call(["/usr/bin/mplayer",file_name])
cmd=raw_input("Enter cmd > ")
print cmd
with open("/home/pi/fifos/mplayer","w") as file:
file.write(cmd + "\n")
