import pygame as pygame
import simpleguitk

display_width = 800
display_height = 600

backgroun_color = (34,139,34)
grey = (220,220,220)
black = (0,0,0)
green = (0,200,0)
red = (225,0,0)
light_slat = (119,136,153)
dark_slat = (47,79,79)
dark_red = (255, 0, 0)

pygame.init()
font = pygame.font.SysFont("Arial", 20)
textfont = pygame.font.SysFont("Comic Sans MS", 35)
game_end = pygame.font.SysFont("Arial", 100)
blackjack = pygame.font.SysFont("roboto", 70)



SUITS = ["C", "S", "H", "D"]
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)


#btw ez nem az enyem rakerestem, hogy black jack pygame assets es ezt talaltam egy kis ido utan
card_images = simpleguitk.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")
card_back = simpleguitk.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")  