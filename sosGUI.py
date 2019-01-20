#!/usr/bin/python3
import pygame
from pygame.locals import *
from sosGAME import *

#Resolution
heigth = 600
width = 900

#Colours
GREY = (70, 70, 70)
BLACK = (0, 0 ,0)
WHITE = (255, 255, 255)
YELLOW = (255, 100, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

#Game Setting
tableSize = 6
squareSize = 70

def menu():
    pygame.init()
    mySurface = pygame.display.set_mode((width, heigth))
    pygame.display.set_caption('SOS')
    inProgress = True

    mySurface.fill(GREY)
    displayLogo(mySurface)
    drawButton(mySurface, BLACK, 0)
    while inProgress:
        mouse = pygame.mouse.get_pos()
        if ((380 + 150) > mouse[0] > 380 and (240 + 50) > mouse[1] > 240):
                    drawButton(mySurface, YELLOW, 1)
        elif ((380 + 150) > mouse[0] > 380 and (310 + 50) > mouse[1] > 310):
                    drawButton(mySurface, YELLOW, 2)
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if ((380 + 150) > mouse[0] > 380 and (240 + 50) > mouse[1] > 240):
                    gameloop(tableSize, squareSize)
                    inProgress = False
                if ((380 + 150) > mouse[0] > 380 and (310 + 50) > mouse[1] > 310):
                    gameloop(tableSize, squareSize)
                    inProgress = False
            if event.type == QUIT:
                inProgress = False
        pygame.display.update()
    pygame.quit()


def displayLogo(mySurface):
    '''if (pygame.time.get_ticks() == time):
        if (COLOR == BLUE):
            COLOR = RED
        if (COLOR == RED):
            COLOR = BLUE
        time = time + 2000'''
    textRect = logoText.get_rect()
    textRect.topleft = (320, 110)
    mySurface.blit(logoText, textRect)


def drawButton(mySurface, textColor, option):
    pygame.draw.rect(mySurface, WHITE, (380,240,150,50))
    pygame.draw.rect(mySurface, WHITE, (380,310,150,50))
    fontSolo = pygame.font.Font('font/solid.ttf', 50)
    fontMult = pygame.font.Font('font/solid.ttf', 20)
    if (option == 1):
        text = fontSolo.render('SOLO', True, textColor)
    else:
        text = fontSolo.render('SOLO', True, BLACK)
    textRect = text.get_rect()
    textRect.topleft = (386, 249)
    mySurface.blit(text, textRect)
    if (option == 2):
        text = fontMult.render('MULTIPLAYER', True, textColor)
    else:
        text = fontMult.render('MULTIPLAYER', True, BLACK)
    textRect.topleft = (383, 328)
    mySurface.blit(text, textRect)

menu()