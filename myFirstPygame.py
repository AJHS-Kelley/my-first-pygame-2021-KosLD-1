# My First PyGame, Bruce Smith, 11/30/21, 1:16PM, v0.2

import pygame, sys
from pygame.locals import *

# Initialize PyGame
pygame.init()

# Setup the Window to draw on.
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('My First PyGame')