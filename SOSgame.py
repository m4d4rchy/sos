#!/usr/bin/python3

import pygame
import sys
import random
from pygame.locals import *

def drawBoard(maSurface, n):
    WHITE = (255, 255, 255)
    pos1 = (50, 60)
    pos2 = (550, 60)
    pos3 = (50, 500)
    pos4 = (550, 500)
    count = 0
    pygame.draw.line(maSurface, WHITE, pos1, pos2)
    pygame.draw.line(maSurface, WHITE, pos1, pos3)
    pygame.draw.line(maSurface, WHITE, pos3, pos4)
    pygame.draw.line(maSurface, WHITE, pos4, pos2)

def gameloop():
    GREY = (70, 70, 70)
    pygame.init()
    maSurface = pygame.display.set_mode((900, 600))
    pygame.display.set_caption('SOS')
    inProgress = True
    while inProgress:
        for event in pygame.event.get():
            if event.type == QUIT:
                inProgress = False
        maSurface.fill(GREY)
        drawBoard(maSurface, 2)
        pygame.display.update()
    pygame.quit()

gameloop()