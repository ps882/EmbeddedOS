import pygame
import os
import sys
import time
import signal


def signal_handler(signal,frame):
    try:
        os.exit()
    except:
        print "couldnt kill using sys.exit, using os.kill"
        os.kill(os.getpid(), 9)

signal.signal(signal.SIGINT, signal_handler)

pygame.init()
pygame.display.set_caption('Get Coordinates')
screen_size = width,height = 320,240
MyClock = pygame.time.Clock()
WHITE = 255, 255, 255
BLACK = 0, 0, 0,
workspace = pygame.display.set_mode(screen_size)
my_font = pygame.font.Font(None,20)
quit_button = {'Quit':(280,200)}
running = 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print "inside quit event"
            running = 0
        elif event.type == pygame.MOUSEBUTTONDOWN :
            down_coord = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP :
            up_coord = pygame.mouse.get_pos()
            if up_coord == down_coord or up_coord != down_coord:
                xcoord,ycoord = down_coord
                if xcoord > width*3/4 and xcoord < width and ycoord > height*3/4 and ycoord < height:
                    running = 0
                else:
                    mycoord = "Hit at " + str(down_coord)
                    print mycoord
                    coord_text = my_font.render(mycoord, True, WHITE)
                    coord_rect = coord_text.get_rect(center=down_coord)
                    workspace.fill(BLACK)
                    workspace.blit(coord_text,coord_rect)
        quit_text = my_font.render("Quit", True, WHITE)
        quit_rect = quit_text.get_rect(center=(280,200))
        workspace.blit(quit_text,quit_rect)
        pygame.display.flip()
    MyClock.tick(30)
print "outside running"
time.sleep(4)
pygame.quit()
