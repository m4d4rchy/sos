#!/usr/bin/python3
import pygame
from pygame.locals import *
'''import sosAlgorithms import *'''

def menu():
    GREY = (70, 70, 70)
    BLACK = (0, 0 ,0)
    YELLOW = (255, 100, 0)
    pygame.init()
    mySurface = pygame.display.set_mode((900, 600))
    pygame.display.set_caption('SOS')
    inProgress = True

    while inProgress:
        mouse = pygame.mouse.get_pos()
        mySurface.fill(GREY)
        displayLogo(mySurface)
        drawButton(mySurface, BLACK, 0)
        if ((380 + 150) > mouse[0] > 380 and (240 + 50) > mouse[1] > 240):
                    drawButton(mySurface, YELLOW, 1)
        elif ((380 + 150) > mouse[0] > 380 and (310 + 50) > mouse[1] > 310):
                    drawButton(mySurface, YELLOW, 2)
        pygame.display.update()
        for event in pygame.event.get():
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

def drawButton(mySurface, textColor, option):
    WHITE = (255, 255, 255)
    BLACK = (0, 0 ,0)
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

def drawBoard(mySurface, n):
    WHITE = (255, 255, 255)
    x = 60
    y = 60
    size = 70
    i = 0
    j = 0
    while (i != n):
        while (j != n):
            drawBoardCell(mySurface, WHITE, x, y, size)    
            x = x + size
            j = j + 1
        j = 0
        i = i + 1
        x = 60
        y = y + size

def drawBoardCell(mySurface, COLOR, x, y, size):
    pos1 = (x, y)
    pos2 = (x + size, y)
    pos3 = (x + size, y + size)
    pos4 = (x, y + size)
    pygame.draw.line(mySurface, COLOR, pos1, pos2)
    pygame.draw.line(mySurface, COLOR, pos2, pos3)
    pygame.draw.line(mySurface, COLOR, pos3, pos4)
    pygame.draw.line(mySurface, COLOR, pos4, pos1)   

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

def displayPlayer(mySurface, n, player):
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    font = pygame.font.Font('font/Washington.ttf', 48)
    if (player == 1):
        text = font.render('<--', True, BLUE)
        textRect = text.get_rect()
        textRect.topleft = (800, 200)
        mySurface.blit(text, textRect)
    else:
        text = font.render('<--', True, RED)
        textRect = text.get_rect()
        textRect.topleft = (800, 300)
        mySurface.blit(text, textRect)

def drawCell(mySurface, board, i, j, player):
    letter = ''
    x = 60 * j + 35
    y = 60 * i + 35
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    font = pygame.font.Font('font/Washington.ttf', 48)
    if (board[i][j] == 1):
        letter = 'S'
    else:
        letter = 'O'
    if (player == 1):
        text = font.render(letter, True, BLUE)
        textRect = text.get_rect()
        textRect.topleft = (x, y)
        mySurface.blit(text, textRect)
    else:
        text = font.render(letter, True, BLUE)
        textRect = text.get_rect()
        textRect.topleft = (x, y)
        mySurface.blit(text, textRect)

def gameloop():
    board = [[1] * n for i in range(6)]
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
        drawBoard(mySurface, 6)
        drawCell(mySurface, board, 0, 0, 1):
        pygame.display.update()
    pygame.quit()

menu()  

'''def drawLines(mySurface,lines,player):

def displayWinner(mySurface,n,scores):'''
