import pygame as pg
from classes import button

pg.init()

#Constands 
#COLORS
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
LIGHT_BLUE = (135,206,251)

#fonts
TITLE_FONT = pg.font.SysFont('comicans',70)
MIDDLE_FONT = pg.font.SysFont('comicans',50)
QUESTION_FONT = pg.font.SysFont('comicans',35)

#Win settings
WIDTH,HEIGHT = 900,500
FPS = 60
win = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("Quiz game")
icon = pg.image.load("img/icon.png")
pg.display.set_icon(icon)
background = pg.image.load("img/background.png")



#Buttons 
WIDTH_MainButton = 300
HEIGHT_MainButton = 150
mainButton = button(LIGHT_BLUE,(WIDTH/2-WIDTH_MainButton/2),(HEIGHT/2-HEIGHT_MainButton/2),WIDTH_MainButton,HEIGHT_MainButton,"START GAME")

