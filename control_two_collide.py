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
pygame.display.set_caption("Collision control")
workspace = pygame.display.set_mode(ScreenSize)
my_font = pygame.font.Font(None,20)
running = 1

BallAOldSpeed = BallASpeed = [4,4]
BallBOldSpeed = BallBSpeed = [3,3]
BallA = pygame.image.load("./BallA.png")
BallARect = BallA.get_rect(center=(50,50))
BallB = pygame.image.load("./BallA.png")
BallBRect = BallB.get_rect(center=(450,400))
main_menu = 1
pause = 1
inc = 1
dec = 1

control_buttons={'Start':(width/4,height*8/10),'Quit':(width*3/4,height*8/10)}
subcontrol_buttons={'Pause':(width/8,height*8/10),'Fast':(width*3/8,height*8/10),'Slow':(width*5/8,height*8/10),'Back':(width*7/8,height*8/10)}

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
                if main_menu == 1:
                    if xcoord < width*1/2 and xcoord > 0 and ycoord > height*3/4 and ycoord < height:
                        main_menu = 0
                    elif xcoord > width*1/2 and xcoord < width and ycoord > height*3/4 and ycoord < height:
                        running = 0
                else:
                    if xcoord < width*2/8 and xcoord > width/8 and ycoord > height*3/4 and ycoord < height:
                        #do something
                        print "Got pause"
                        if pause == 1:
                            print "inside pause yes"
                            BallAOldSpeed = BallASpeed[:]
                            BallBOldSpeed = BallBSpeed[:]
                            BallASpeed[0] = 0
                            BallASpeed[1] = 0
                            BallBSpeed[0] = 0
                            BallBSpeed[1] = 0
                            pause = 0
                            #print BallASpeed,BallBSpeed
                        else:
                            print "inside start yes"
                            BallASpeed = BallAOldSpeed[:]
                            BallBSpeed = BallBOldSpeed[:]
                            pause = 1
                            #print BallASpeed,BallBSpeed
                    elif xcoord < width*4/8 and xcoord > width*3/8 and ycoord > height*3/4 and ycoord < height:
                        #do something else
                        print "Got fast"
                        if pause == 1:
                            print BallASpeed,BallBSpeed
                            BallASpeed[0] = BallASpeed[0] + inc*(BallASpeed[0]/abs(BallASpeed[0]))
                            BallASpeed[1] = BallASpeed[1] + inc*(BallASpeed[1]/abs(BallASpeed[1]))
                            BallBSpeed[0] = BallBSpeed[0] + inc*(BallBSpeed[0]/abs(BallBSpeed[0]))
                            BallBSpeed[1] = BallBSpeed[1] + inc*(BallBSpeed[1]/abs(BallBSpeed[1]))
                            print BallASpeed,BallBSpeed
                    elif xcoord < width*6/8 and xcoord > width*5/8 and ycoord > height*3/4 and ycoord < height:
                        #do something else
                        print "Got slow"
                        if pause == 1:
                            print BallASpeed,BallBSpeed
                            BallASpeed[0] = BallASpeed[0] - dec*(BallASpeed[0]/abs(BallASpeed[0]))
                            BallASpeed[1] = BallASpeed[1] - dec*(BallASpeed[1]/abs(BallASpeed[1]))
                            BallBSpeed[0] = BallBSpeed[0] - dec*(BallBSpeed[0]/abs(BallBSpeed[0]))
                            BallBSpeed[1] = BallBSpeed[1] - dec*(BallBSpeed[1]/abs(BallBSpeed[1]))
                            print BallASpeed,BallBSpeed
                    elif xcoord < width*8/8 and xcoord > width*7/8 and ycoord > height*3/4 and ycoord < height:
                        main_menu = 1
                        print "Got back"

    if main_menu == 0:
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
        for subbutton_text,subbutton_coord in subcontrol_buttons.items():
            subcontrol_text = my_font.render(subbutton_text, True, WHITE)
            subcontrol_rect = subcontrol_text.get_rect(center=subbutton_coord)
            workspace.blit(subcontrol_text,subcontrol_rect)


    if main_menu == 1:
        workspace.fill(BLACK)
        for button_text,button_coord in control_buttons.items():
            control_text = my_font.render(button_text, True, WHITE)
            control_rect = control_text.get_rect(center=button_coord)
            workspace.blit(control_text,control_rect)
    pygame.display.flip()

    MyClock.tick(30)
