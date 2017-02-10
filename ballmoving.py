import pygame
import signal
import sys
import os


def signal_handler(signal, frame):
    try:
        os._exit()
    except:
        print "couldnt kill using sys.exit, using os.kill"
        os.kill(os.getpid(), 9)

signal.signal(signal.SIGINT, signal_handler)

pygame.init()
ScreenSize = width,height = 320, 240
MyClock = pygame.time.Clock()
MyClock.tick(50)
BallASpeed = [2,2]
BallBSpeed = [3,3]

BLACK = 0 , 0 , 0
work_screen = pygame.display.set_mode(ScreenSize)
BallA = pygame.image.load("./BallA.png")
BallARect = BallA.get_rect()

while 1:
    BallARect = BallARect.move(BallASpeed)
    if BallARect.left < 0 or BallARect.right > width:
        BallASpeed[0] = -BallASpeed[0]
    if BallARect.top < 0 or BallARect.bottom > height:
        BallASpeed[1] = -BallASpeed[1]

    work_screen.fill(BLACK)
    work_screen.blit(BallA,BallARect)
    pygame.display.flip()

    MyClock.tick(50)
