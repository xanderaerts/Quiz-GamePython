import pygame
from classes import button

pygame.init()

#Constands 
#COLORS
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
LIGHT_BLUE = (135,206,251)

#fonts
TITLE_FONT = pygame.font.SysFont('comicans',70)
MIDDLE_FONT = pygame.font.SysFont('comicans',50)
QUESTION_FONT = pygame.font.SysFont('comicans',35)
SCORE_FONT = pygame.font.SysFont('comicans',25)

#IMAGES
DEFAULT_SIZE_IMG = (200,200)
img1 = pygame.image.load("img/correctEmoji.png")
correctEmoji = pygame.transform.scale(img1,DEFAULT_SIZE_IMG)
img2 = pygame.image.load("img/wrongEmoji.png")
wrongEmoji = pygame.transform.scale(img2,DEFAULT_SIZE_IMG)

#Win settings
WIDTH,HEIGHT = 900,500
FPS = 60
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Quiz game")
icon = pygame.image.load("img/icon.png")
pygame.display.set_icon(icon)
background = pygame.image.load("img/background.png")



#Buttons 
WIDTH_MainButton = 300
HEIGHT_MainButton = 150
mainButton = button(LIGHT_BLUE,(WIDTH/2-WIDTH_MainButton/2),(HEIGHT/2-HEIGHT_MainButton/2),WIDTH_MainButton,HEIGHT_MainButton,"START GAME")

