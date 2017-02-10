#!/bin/bash


/usr/bin/python /home/pi/python_scripts/gpio_fifo.py  &
sudo SDL_VIDEODRIVER=fbcon SDL_FBDEV=/dev/fb1 /usr/bin/mplayer -input file=/home/pi/fifos/mplayer -vo sdl -framedrop /home/pi/bigbuckbunny320p.mp4 

