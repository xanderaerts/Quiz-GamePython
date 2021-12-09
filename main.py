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
    win.blit(title,(WIDTH/2 - title.get_width()/2,30))

    mainButton.draw(win,(0,0,0))

    pg.display.update()

def startGame():
    inGame = True
    while(inGame):
        win.blit(background,(0,0))

        vragen = []
        load_question(vragen)    
        questions = QUESTION_FONT.render(vragen[0],1,BLACK)
        win.blit(questions,(WIDTH/2 - questions.get_width()/2,20))

        andwoordA = vragen[1]
        andwoordB = vragen[2]
        #andwoordC = vragen[3]

        answerA = button(LIGHT_BLUE,(WIDTH/2-500/2),150,500,50,andwoordA)
        answerA.draw(win,(0,0,0))
        anwserB = button(LIGHT_BLUE,(WIDTH/2-500/2),210,500,50,andwoordB)
        anwserB.draw(win,(0,0,0))
        #answerC = button(LIGHT_BLUE,(WIDTH/2-500/2),260,500,50,andwoordC)
        #answerC.draw(win,(0,0,0))
        
        for event in pg.event.get():
            pos = pg.mouse.get_pos()
            if(event.type == pg.MOUSEBUTTONDOWN):
                if(answerA.isOver(pos)):
                    print("a")


        pg.display.update()
    

def load_question(questions):
    FILE = open("questions.txt","r")

    for i in range (1,4):
        question = FILE.readline()
        questions.append(question[:-1])
    FILE.close()


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