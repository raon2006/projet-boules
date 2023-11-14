#yyo
import pygame, sys
import time
import random
from pygame.locals import *

pygame.display.init()
fenetre = pygame.display.set_mode((640, 480))
fenetre.fill([0,0,0])
mylist = ["100", "230","65","122","20","80","166","44","87","249"]
r = random.choice(mylist)
g = random.choice(mylist)
b = random.choice(mylist)
couleur2 = (r,g,b)

x = 300
y = 200
dx = 4
dy = -3

x3 = 300
y3 = 400
dx3 = 4
dy3 = -2

x2 = 400
y2 = 100
dx2 = 5
dy2 = -4

couleur = (90,255,255)
couleur4 = (244, 189, 3)
couleur3 = (89,233,12)

class balle:
    def __init__(self,x,y,dx,dy):
        self.x = x
        self.dx = dx
        self.y = y
        self.dy = dy 
    def draw(self):
        pygame.draw.circle(fenetre,couleur,(self.x,self.y),10)
    def move(self):
        self.x +=  self.dx
        self.y +=  self.dy
    def paroi(self):
        if self.x < 10:
            self.dx *= (-1)
        elif self.x > 630:
            self.dx *= (-1)
        elif self.y < 10:
            self.dy *= (-1)
        elif self.y > 470:
            self.dy *= (-1)

balle1 =balle(56,75,2,5)
liste = [balle1]


def collision(n):
    if x == x2 or y == y2:
        dx = dx(-1)
        dx2 = dx2(-1)
        print("collision")
        collision(9)


      


while True :
    fenetre.fill([0,0,0])
    pygame.draw.circle(fenetre,couleur,(x,y),10)
    pygame.draw.circle(fenetre,couleur3,(x2,y2),5) #normalement ici c'est couleur2 et pas couleur3
    balle1.draw()
    balle1.move()
    balle1.paroi()
    x += dx
    y += dy
    x2 += dx2
    y2 += dy2
    x3 += dx3
    y3 += dy3

    for b in liste:
        b.draw()
        b.move()

    if x < 10:
        dx *= (-1)
    elif x > 630:
        dx *= (-1)
    elif y < 10:
        dy *= (-1)
    elif y > 470:
        dy *= (-1)


    if x2 < 10:
        dx2 *= (-1)
    elif x2 > 630:
        dx2 *= (-1)
    elif y2 < 10:
        dy2 *= (-1)
    elif y2 > 470:
        dy2 *= (-1)

    



    pygame.display.update()

    # routine pour pouvoir fermer «proprement» la fenêtre Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
    time.sleep(0.01)