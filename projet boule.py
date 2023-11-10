#yyo
import pygame, sys
import time
from pygame.locals import *

pygame.display.init()
fenetre = pygame.display.set_mode((640, 480))
fenetre.fill([0,0,0])

x = 300
y = 200
dx = 4
dy = -3
couleur = (45,170,250)

while True :
    fenetre.fill([0,0,0])
    pygame.draw.circle(fenetre,couleur,(x,y),10)

    x += dx
    y += dy
    
    if x < 10:
        dx = dx*(-1)
    elif x > 630:
        dx = dx*(-1)
    elif y < 10:
        dy = dy*(-1)
    elif y > 470:
        dy = dy*(-1)


    


    pygame.display.update()

    # routine pour pouvoir fermer «proprement» la fenêtre Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
    time.sleep(0.1)