import pygame as pg
import os 
from constants import *
from classes import *

pg.init()



#Functions
def draw_mainscreen():
    win.fill(WHITE)
    title = TITLE_FONT.render("Quiz Game",1,BLACK)
    win.blit(background,(0,0))
    win.blit(title,(WIDTH/2 - title.get_width()/2,20))

    mainButton.draw(win,(0,0,0))

    pg.display.update()

def startGame():
    drawGameScreen()


def drawGameScreen():
    win.fill(GREEN)
    pg.display.update()



#main loop of the game
def main():
    clock = pg.time.Clock()
    run = True
    while(run):
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        draw_mainscreen()

        for event in pg.event.get():
            pos = pg.mouse.get_pos()
        if(event.type == pg.MOUSEBUTTONDOWN):
            if(mainButton.isOver(pos)):
                startGame()


    pg.quit()


if __name__ == "__main__": #runs the game only when this file is run, not when imported by another file
    main()


pg.quit()