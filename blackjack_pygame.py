import pygame as pygame
from blackjack_deck import *
from constants import *
import sys
import time
pygame.init

clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((display_width,display_height))


pygame.display.set_caption("FeketeJani")
gameDisplay.fill(backgroun_color)
pygame.draw.rect(gameDisplay,grey, pygame.Rect(0,0,250,700))

