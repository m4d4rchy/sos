#!/usr/bin/python3
import pygame
from pygame.locals import *
from sosAlgorithms import *
from sosINIT import *

def drawBoard(mySurface, n):
    x = 70
    y = 70
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
        x = 70
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
    textRect = boardText.get_rect()
    textRect.topleft = (x, (y + 15))
    mySurface.blit(boardText, textRect)

def displayTeam(mySurface):
    textRect = bscoreText.get_rect()
    textRect.topleft = (600, 200)
    mySurface.blit(bscoreText, textRect)
    textRect.topleft = (600, 300)
    mySurface.blit(rscoreText, textRect)

def displayScore(mySurface, n, scores):
    clearScore(mySurface)
    player1str = str(scores[0])
    player2str = str(scores[1])
    player1 = score1Font.render(player1str, True, WHITE)
    player2 = score1Font.render(player2str, True, WHITE)
    textRect = player1.get_rect()
    textRect.topleft = (715, 190)
    mySurface.blit(player1, textRect)
    textRect.topleft = (715, 290)
    mySurface.blit(player2, textRect)

def clearScore(mySurface):
    rect = (715, 190, 70, 70)
    pygame.draw.rect(mySurface, GREY, rect)
    rect = (715, 290, 70, 70)
    pygame.draw.rect(mySurface, GREY, rect)

def displayPlayer(mySurface, n, player):
    if (player == 1):
        textRect = player1onText.get_rect()
        textRect.topleft = (800, 200)
        mySurface.blit(player1onText, textRect)
        textRect = playeroffText.get_rect()
        textRect.topleft = (800, 300)
        mySurface.blit(playeroffText, textRect)
    if (player == 2):
        textRect = playeroffText.get_rect()
        textRect.topleft = (800, 200)
        mySurface.blit(playeroffText, textRect)
        textRect = player2onText.get_rect()
        textRect.topleft = (800, 300)
        mySurface.blit(player2onText, textRect)


def drawCell(mySurface, board, i, j, player):
    letter = ''
    clearCell(mySurface, board, i, j)
    if (board[i][j] == 1):
        x = 71 + (j * 70) + 18
        y = 71 + (i * 70) + 12
        letter = 'S'
    elif(board[i][j] == 2):
        x = 71 + (j * 70) + 22
        y = 71 + (i * 70) + 12
        letter = 'O'
    if (player == 1):
        text = cellFont.render(letter, True, BLUE)
        textRect = text.get_rect()
        textRect.topleft = (x, y)
        mySurface.blit(text, textRect)
    else:
        text = cellFont.render(letter, True, RED)
        textRect = text.get_rect()
        textRect.topleft = (x, y)
        mySurface.blit(text, textRect)

def clearCell(mySurface, board, i, j):
    x = 71 + (j * 70)
    y = 71 + (i * 70)
    rect = (x, y, 69, 69)
    pygame.draw.rect(mySurface, GREEN, rect)

def drawLines(mySurface, lines, player):
    if (lines):
        x = 70 * (lines[1] + 1) + 15 
        y = 70 * (lines[0] + 1) + 35
        x1 = 70 * (lines[3] + 1) + 55
        y1 = 70 * (lines[2] + 1) + 35
        pos1 = (x, y)
        pos2 = (x1, y1)
        if (player == 1):
            pygame.draw.line(mySurface, BLUE, pos1, pos2)
        elif (player == 2):
            pygame.draw.line(mySurface, RED, pos1, pos2)

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
            if ((70 + (x - half)) > mouse[0] > (70 + (size * i) - half) and (70 + y) > mouse[1] > (70 + (size * j))
            and possibleSquare(board, n, j, i) == True):
                position[0] = i
                position[1] = j
                board[j][i] = 1
                return (position)
            elif ((70 + x) > mouse[0] > (70 + (size * i) + half) and (70 + y) > mouse[1] > (70 + (size * j))
            and possibleSquare(board, n, j, i) == True):
                position[0] = i
                position[1] = j
                board[j][i] = 2
                return (position)
            x = x + size
            i = i + 1
        i = 0
        x = 70
        j = j + 1
        y = y + size
    return (position)

def gameloop(n, size):
    pygame.init()
    mySurface = pygame.display.set_mode((width, heigth))
    board = [[0] * 6 for i in range(6)]
    pygame.display.set_caption('SOS')
    inProgress = True
    player = 1
    length = 0
    scores = [0, 0]

    mySurface.fill(GREY)
    drawBoard(mySurface, n)
    displayTeam(mySurface)
    while inProgress:
        position = [-1, -1]
        lines = []
        displayScore(mySurface, 6, scores)
        displayPlayer(mySurface, n, player)
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                position = selectSquare(mySurface, board, n, size)
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

'''def displayWinner(mySurface,n,scores):
        selectSquare(mySurface, board, n)'''