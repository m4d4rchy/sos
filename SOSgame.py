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

def newBoard(n):
    board = [[0] * n for i in range(n)]
    return(board)

def possibleSquare(board, n, i, j):
    if ((i >= 0 and j >= 0) and (i <= n and j <= n) and board[i][j] == 0):
        return(True)
    else:
        return(False)

'''def updateScoreS(board, n, i, j, scores, player, lines):
    if (i == 0 and j == 0):
        if (board[i][j + 1] == 2 and board[i][j + 2] == 1):
            scores[player - 1] = scores[player - 1] + 1
            lines.extend([i, j, i, j + 2])
    elif (i == (n - 1) and j == (n - 1)):
    elif (i == 0):
    elif (i == (n - 1)):
    elif (j == 0):
    elif (j == (n - 1)):
    else:'''


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