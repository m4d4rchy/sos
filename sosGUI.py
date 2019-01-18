#!/usr/bin/python3
import pygame
from pygame.locals import *
from sosAlgorithms import *

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
                    gameloop(6, 70)
                    inProgress = False
                if ((380 + 150) > mouse[0] > 380 and (310 + 50) > mouse[1] > 310):
                    gameloop(6, 70)
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
    drawBoardLetter(mySurface, x, y, size)

def drawBoardLetter(mySurface, x, y, size):
    ORANGE = (255,140,0)
    font = pygame.font.Font('font/Washington.ttf', 45)
    text = font.render('S | O', True, ORANGE)
    textRect = text.get_rect()
    textRect.topleft = (x, (y + 15))
    mySurface.blit(text, textRect)

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
    x = (60 + 27 - (j + 5)) * (j + 1)
    y = (60 + 13) * (i + 1)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    font = pygame.font.Font('font/Washington.ttf', 55)
    clearCell(mySurface, board, i, j)
    if (board[i][j] == 1):
        print("draw s")
        letter = 'S'
    elif(board[i][j] == 2):
        print("draw o")
        letter = 'O'
    if (player == 1):
        text = font.render(letter, True, BLUE)
        textRect = text.get_rect()
        textRect.topleft = (x, y)
        mySurface.blit(text, textRect)
    else:
        text = font.render(letter, True, RED)
        textRect = text.get_rect()
        textRect.topleft = (x, y)
        mySurface.blit(text, textRect)

def clearCell(mySurface, board, i, j):
    GREY = (70, 70, 70)
    x = 61 * (j + 1) + (j * 9)
    y = 61 * (i + 1) + (i * 9)
    rect = (x, y, 69, 69)
    pygame.draw.rect(mySurface, GREY, rect)

def drawLines(mySurface, lines, player):
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    
    if (lines):
        x = 60 * (lines[1] + 1)
        y = 60 * (lines[0] + 1) + 35
        x1 = 70 * (lines[3] + 1) + 20
        y1 = 60 * (lines[2] + 1) + 35
        pos1 = (x, y)
        pos2 = (x1, y1)
        if (player == 1):
            pygame.draw.line(mySurface, RED, pos1, pos2)
            print("drawing", pos1, pos2)
        elif (player == 2):
            pygame.draw.line(mySurface, BLUE, pos1, pos2)

def selectSquare(mySurface, board, n, size):
    i = 0
    j = 0
    x = 70
    y = 70
    half = size/2
    position = [-1, -1]
    mouse = pygame.mouse.get_pos() 

    while (j != n):
        while (i != n):
            if ((60 + (x - half)) > mouse[0] > (60 + (size * i) - half) and (60 + y) > mouse[1] > (60 + (size * j))
            and possibleSquare(board, n, j, i) == True):
                position[0] = i
                position[1] = j
                print("s", i, j, x, y, mouse[0], mouse[1])
                board[j][i] = 1
                return (position)
            elif ((60 + x) > mouse[0] > (60 + (size * i) + half) and (60 + y) > mouse[1] > (60 + (size * j))
            and possibleSquare(board, n, j, i) == True):
                position[0] = i
                position[1] = j
                print("o", i, j)
                board[j][i] = 2
                return (position)
            x = x + size
            i = i + 1
        i = 0
        x = 60 
        j = j + 1
        y = y + size
    return (position)


def gameloop(n, size):
    board = [[0] * 6 for i in range(6)]

    GREY = (70, 70, 70)
    pygame.init()
    mySurface = pygame.display.set_mode((900, 600))
    pygame.display.set_caption('SOS')
    inProgress = True
    player = 1
    length = 0
    scores = [0, 0]

    mySurface.fill(GREY)
    drawBoard(mySurface, n)
    while inProgress:
        position = [-1, -1]
        lines = []
        displayScore(mySurface, 6, scores)
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                position = selectSquare(mySurface, board, n, size)
                print(board)
            if event.type == QUIT:
                inProgress = False
        if (position[0] != -1):
            drawCell(mySurface, board, position[1], position[0], player)
            updateScoreS(board, n, position[1], position[0], scores, player, lines)
            drawLines(mySurface, lines , player)
            displayScore(mySurface, 6, scores)
            if (player == 2):
                player = 1
            else:
                player = player + 1
        pygame.display.update()
    pygame.quit()

menu()

'''def displayWinner(mySurface,n,scores):
        selectSquare(mySurface, board, n)'''