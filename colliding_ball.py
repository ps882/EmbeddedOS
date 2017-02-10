import pygame
import signal
import sys
import os
import math


def signal_handler(signal, frame):
    try:
        os._exit()
    except:
        print "couldnt kill using sys.exit, using os.kill"
        os.kill(os.getpid(), 9)

def get_distfrmcoord(xA,yA,xB,yB):
    return(math.sqrt((xA-xB)**2+(yA-yB)**2))

signal.signal(signal.SIGINT, signal_handler)

pygame.init()
ScreenSize = width,height = 320, 240
#ScreenSize = width,height = 820, 640
MyClock = pygame.time.Clock()
BallASpeed = [2,2]
BallBSpeed = [1,1]

BLACK = 0 , 0 , 0
work_screen = pygame.display.set_mode(ScreenSize)
BallA = pygame.image.load("./BallA.png")
BallARect = BallA.get_rect(center=(50,50))
BallB = pygame.image.load("./BallA.png")
BallBRect = BallB.get_rect(center=(150,150))

while 1:
    BallARect = BallARect.move(BallASpeed)
    if BallARect.left < 0 or BallARect.right > width:
        BallASpeed[0] = -BallASpeed[0]
    if BallARect.top < 0 or BallARect.bottom > height:
        BallASpeed[1] = -BallASpeed[1]
    BallBRect = BallBRect.move(BallBSpeed)
    if BallBRect.left < 0 or BallBRect.right > width:
        BallBSpeed[0] = -BallBSpeed[0]
    if BallBRect.top < 0 or BallBRect.bottom > height:
        BallBSpeed[1] = -BallBSpeed[1]


    if get_distfrmcoord(BallARect.x,BallARect.y,BallBRect.x,BallBRect.y) < 100:
        BallASpeed[0] = -BallASpeed[0]
        BallASpeed[1] = -BallASpeed[1]
        BallBSpeed[0] = -BallBSpeed[0]
        BallBSpeed[1] = -BallBSpeed[1]


    work_screen.fill(BLACK)
    work_screen.blit(BallA,BallARect)
    work_screen.blit(BallB,BallBRect)
    pygame.display.flip()

    MyClock.tick(250)
