#!/usr/bin/python3
import pygame
from pygame.locals import *

#Colours
GREY = (70, 70, 70)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255,140,0)
GREEN = (50, 70, 50)

#Initialize
pygame.init()

#Font
logoFont = pygame.font.Font('font/solid.ttf', 100)
boardFont = pygame.font.Font('font/Washington.ttf', 45)
scoreFont = pygame.font.Font('font/Washington.ttf', 48)
playerFont = pygame.font.Font('font/Washington.ttf', 48)
cellFont = pygame.font.Font('font/Washington.ttf', 55)

#Text
logoText = logoFont.render('S O S', True, BLUE)
boardText = boardFont.render('S | O', True, ORANGE)
bscoreText = scoreFont.render('Blue:', True, BLUE)
rscoreText = scoreFont.render('Red:', True, RED)
player1onText = playerFont.render('<--', True, BLUE)
player2onText = playerFont.render('<--', True, RED)
playeroffText = playerFont.render('<--', True, GREY)