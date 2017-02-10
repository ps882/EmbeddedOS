
import pygame               #import libraries
import RPi.GPIO as GPIO
import time
import os



GPIO.setmode(GPIO.BCM)                                                                            #set GPIO mode to Broadcom

GPIO.setup(6, GPIO.OUT)                                                                           #set two pins to OUT 6 pins to Input
GPIO.setup(5, GPIO.OUT)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)

leftServo = GPIO.PWM(6,46.51)                                                                     #assign the OUT pins to right and left servo PWM objects
rightServo = GPIO.PWM(5,46.51)

pygame.init()                                                                                     #initialize the pygame objects

screenSize = width,height =  320,240                                                              #set screensize and other variables
directionInfoL = "L-Stopped"
directionInfoR = "R-Stopped"
right = 0
left = 0
pygame.display.set_caption("Servo Control")
workSpace = pygame.display.set_mode(screenSize)
buttonFont = pygame.font.Font(None,20)
displayFont = pygame.font.Font(None,30)
#set my buttons dictionary
myButtons = {"Quit":(width/4,height*3/4),"Panic":(width*3/4,height*3/4),"Left":(width/4,height/3),"Right":(width*3/4,height/3)}

panicColor = 255,0,0                                                                               #initiate to RED
panicOn = 1
BLACK = 0,0,0            #define the BLACK and WHITE color
WHITE = 255,255,255
running = 1
myClock = pygame.time.Clock()                                                            #initialize the pygame clock to adjust FPS

def writeScreen():  #define the write screen function for pygame
    global directionInfoR
    global directionInfoL
    global right
    global left
#define the variables as global so that they can be accessed from different functions
#    print "left",directionInfoL,"right",directionInfoR
#write text and button on woorkspace
    workSpace.fill(BLACK)
    sur_text = displayFont.render(directionInfoL, True, WHITE)
    sur_rect = sur_text.get_rect(center=myButtons["Left"])
    workSpace.blit(sur_text,sur_rect)
 
    sur_text = displayFont.render(directionInfoR, True, WHITE)
    sur_rect = sur_text.get_rect(center=myButtons["Right"])
    workSpace.blit(sur_text,sur_rect)
 
    sur_text = buttonFont.render("Quit", True, WHITE)
    sur_rect = sur_text.get_rect(center=myButtons["Quit"])
    workSpace.blit(sur_text,sur_rect)
 
    sur_text = buttonFont.render("Panic", True, panicColor)
    sur_rect = sur_text.get_rect(center=myButtons["Panic"])
    workSpace.blit(sur_text,sur_rect)
 
    pygame.display.flip() 
 
def rightFwd():    #function for right forward motion
    global directionInfoR
    global directionInfoL
    global right
    global left
    rightServo.start(6.2)
    directionInfoR = "R-Forward"
    print "inside right forward",directionInfoR
    right = 1
    writeScreen()

def rightBwd():    #function for right backward motion
    global directionInfoR
    global directionInfoL
    global right
    global left
    rightServo.start(7.7)
    directionInfoR = "R-Backward"
    right = -1
    writeScreen()

def rightStop():     #function for right stop motion
    global directionInfoR
    global directionInfoL
    global right
    global left
    rightServo.ChangeDutyCycle(0)
    directionInfoR = "R-Stopped"
    right = 0
    writeScreen()

def leftFwd():      #function for left forward motion
    global directionInfoR
    global directionInfoL
    global right
    global left
    leftServo.start(7.7)
    directionInfoL = "L-Forward"
    left = 1
    writeScreen()

def leftBwd():        #function for left backward motion
    global directionInfoR
    global directionInfoL
    global right
    global left
    leftServo.start(6.2)
    directionInfoL = "L-Backward"
    left = -1
    writeScreen()

def leftStop():     #functino for left stop motion
    global directionInfoR
    global directionInfoL
    global right
    global left
    leftServo.ChangeDutyCycle(0)
    directionInfoL = "L-Stopped"
    left = 0
    writeScreen()

writeScreen()      #call write screen initially, otherwise call on button events

while running:
    left_fwd=GPIO.input(17)
    left_stp=GPIO.input(22)
    left_bwd=GPIO.input(23)
    right_fwd=GPIO.input(27)
    right_stp=GPIO.input(13)
    right_bwd=GPIO.input(19)
    
    if left_fwd == False:  #loop for physical buttons
        leftFwd()

    elif left_stp == False:
        leftStop()

    elif left_bwd == False:
        leftBwd()

    elif right_fwd == False:
        rightFwd()

    elif right_stp == False:
        rightStop()

    elif right_bwd == False:
        rightBwd()

    for event in pygame.event.get():         #loop for tft button presses
        if event.type == pygame.QUIT:
            print "inside quit event"
            running = 0
        elif event.type == pygame.MOUSEBUTTONDOWN :
            down_coord = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP :
            up_coord = pygame.mouse.get_pos()
            if up_coord == down_coord or up_coord != down_coord:
                xcoord,ycoord = down_coord
                if xcoord < width/3 and xcoord > width/5 and ycoord < height and ycoord > height*3/5: #quit case
                    running = 0
                elif xcoord < width and xcoord > width*3/5 and ycoord < height and ycoord > height*3/5: #Panic case
                    if panicOn:    #Check if panic or resume press
                        #stop both the servo motors
                        #save the ongoing directions
                        oldRight = right
                        oldLeft = left
                        panicColor = 0,255,0
                        rightStop()
                        leftStop()
                        panicOn = 0
#                        writeScreen()
                    else:
                        #start both the servo motors
                        panicColor = 255,0,0
                #check for old directions and call apt functions
                        if oldRight > 0:
                            rightFwd()
                        elif oldRight < 0:
                            rightBwd()
                        else:
                            rightStop()
                        if oldLeft > 0:
                            leftFwd()
                        elif oldLeft < 0:
                            leftBwd()
                        else:
                            leftStop()
                        panicOn = 1
#                        writeScreen()

    myClock.tick(30)
print "outside running"
pygame.quit()      #close the pygame objects
GPIO.cleanup()
