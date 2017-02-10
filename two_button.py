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
#ScreenSize = width,height = 320, 240
ScreenSize = width,height = 820, 640
MyClock = pygame.time.Clock()
WHITE = 255, 255, 255
BLACK = 0, 0, 0,
workspace = pygame.display.set_mode(ScreenSize)
my_font = pygame.font.Font(None,20)
running = 1

BallASpeed = [2,2]
BallBSpeed = [1,1]
BallA = pygame.image.load("./BallA.png")
BallARect = BallA.get_rect(center=(50,50))
BallB = pygame.image.load("./BallA.png")
BallBRect = BallB.get_rect(center=(450,400))
ball_video = 0

control_buttons={'Start':(width/4,height*3/4),'Quit':(width*3/4,height*3//4)}

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print "inside quit event"
            running = 0
        elif event.type == pygame.MOUSEBUTTONDOWN:
            down_coord = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            up_coord = pygame.mouse.get_pos()
            if up_coord == down_coord or up_coord != down_coord:
                xcoord,ycoord = down_coord
                if xcoord > width*1/2 and xcoord < width and ycoord > height*3/4 and ycoord < height:
                    ball_video = 0
                    running = 0
                elif xcoord < width*1/2 and xcoord > 0 and ycoord > height*3/4 and ycoord < height:
                    ball_video = 1

    if ball_video == 1:
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


        workspace.fill(BLACK)
        workspace.blit(BallA,BallARect)
        workspace.blit(BallB,BallBRect)
    for button_text,button_coord in control_buttons.items():
        control_text = my_font.render(button_text, True, WHITE)
        control_rect = control_text.get_rect(center=button_coord)
        workspace.blit(control_text,control_rect)
    pygame.display.flip()

    MyClock.tick(50)
