#!/usr/bin/python3
import pygame
from pygame.locals import *
'''import sosAlgorithms import *'''

def menu():
    GREY = (70, 70, 70)
    pygame.init()
    mySurface = pygame.display.set_mode((900, 600))
    pygame.display.set_caption('SOS')
    inProgress = True

    while inProgress:
        mouse = pygame.mouse.get_pos()
        mySurface.fill(GREY)
        displayLogo(mySurface)
        drawButton(mySurface)
        pygame.display.update()
        for event in pygame.event.get():
            '''if ((380 + 150) > mouse[0] > 380 and (240 + 50) > mouse[1] > 240):
                    buttonHover()
                if ((380 + 150) > mouse[0] > 380 and (310 + 50) > mouse[1] > 310):
                    buttonHover()'''
            if event.type == MOUSEBUTTONDOWN:
                if ((380 + 150) > mouse[0] > 380 and (240 + 50) > mouse[1] > 240):
                    gameloop()
                    inProgress = False
                if ((380 + 150) > mouse[0] > 380 and (310 + 50) > mouse[1] > 310):
                    gameloop()
                    inProgress = False
            if event.type == QUIT:
                inProgress = False
    pygame.quit()

def displayLogo(mySurface):
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    font = pygame.font.Font('font/solid.ttf', 100)
    text = font.render('S O S', True, BLUE)
    textRect = text.get_rect()
    textRect.topleft = (320, 110)
    mySurface.blit(text, textRect)

def drawButton(mySurface):
    WHITE = (255, 255, 255)
    BLACK = (0, 0 ,0)
    pygame.draw.rect(mySurface, WHITE, (380,240,150,50))
    pygame.draw.rect(mySurface, WHITE, (380,310,150,50))
    fontSolo = pygame.font.Font('font/solid.ttf', 50)
    text = fontSolo.render('SOLO', True, BLACK)
    textRect = text.get_rect()
    textRect.topleft = (386, 249)
    mySurface.blit(text, textRect)
    fontMult = pygame.font.Font('font/solid.ttf', 20)
    text = fontMult.render('MULTIPLAYER', True, BLACK)
    textRect.topleft = (383, 328)
    mySurface.blit(text, textRect)

def drawBoard(mySurface, n):
    WHITE = (255, 255, 255)
    pos1 = (50, 60)
    pos2 = (550, 60)
    pos3 = (50, 500)
    pos4 = (550, 500)
    count = 0
    pygame.draw.line(mySurface, WHITE, pos1, pos2)
    pygame.draw.line(mySurface, WHITE, pos1, pos3)
    pygame.draw.line(mySurface, WHITE, pos3, pos4)
    pygame.draw.line(mySurface, WHITE, pos4, pos2)
    drawBoardLine(mySurface, WHITE)

'''def drawBoardCell(mySurface, x, y):'''

    

def drawBoardLine(mySurface, WHITE):
    pos1 = (150, 60)
    pos2 = (150, 500)
    pos3 = (250, 60)
    pos4 = (250, 500)
    pos5 = (350, 60)
    pos6 = (350, 500)
    pos7 = (450, 60)
    pos8 = (450, 500)
    pos9 = (550, 60)
    pos10 = (550, 500)
    pygame.draw.line(mySurface, WHITE, pos1, pos2)
    pygame.draw.line(mySurface, WHITE, pos3, pos4)
    pygame.draw.line(mySurface, WHITE, pos5, pos6)
    pygame.draw.line(mySurface, WHITE, pos7, pos8)
    pygame.draw.line(mySurface, WHITE, pos9, pos10)

def displayScore(mySurface, n, scores):
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    font = pygame.font.Font('font/Washington.ttf', 48)
    text = font.render('Blue:', True, BLUE)
    textRect = text.get_rect()
    textRect.topleft = (600, 200)
    mySurface.blit(text, textRect)
    text = font.render('Red:', True, RED)
    textRect.topleft = (600, 300)
    mySurface.blit(text, textRect)

def gameloop():
    GREY = (70, 70, 70)
    pygame.init()
    mySurface = pygame.display.set_mode((900, 600))
    pygame.display.set_caption('SOS')
    inProgress = True

    while inProgress:
        for event in pygame.event.get():
            if event.type == QUIT:
                inProgress = False
        mySurface.fill(GREY)
        drawBoard(mySurface, 2)
        displayScore(mySurface, 1, 2)
        pygame.display.update()
    pygame.quit()

menu()

'''def displayPlayer(mySurface, n, player):

def drawCell(mySurface,board,i,j,player):

def drawLines(mySurface,lines,player):

def displayWinner(mySurface,n,scores):'''
