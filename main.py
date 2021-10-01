import pygame as pg
import os

pg.init()


#Constands 
#COLORS
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)

WIDTH,HEIGHT = 900,500
FPS = 60


#window settings
WIN = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("Quiz game")

#Functions
def draw_window():
    WIN.fill(WHITE)
    pg.display.update()
    



#main loop of the game
def main():
    #clock = pg.time.clock()
    run = True
    while(run):
        #clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        draw_window()
       


    pg.quit()


if __name__ == "__main__": #runs the game only when this file is run, not when imported by another file
    main()


pg.quit()