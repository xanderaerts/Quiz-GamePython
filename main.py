import pygame
import os 
import linecache
from constants import *
from classes import *

pygame.init()

#Functions
def draw_mainscreen():
    #win.fill(WHITE)
    title = TITLE_FONT.render("Quiz Game",1,BLACK)
    win.blit(background,(0,0))
    win.blit(title,(WIDTH/2 - title.get_width()/2,30))

    mainButton.draw(win,(0,0,0))

    draw_highScore()

    pygame.display.update()


def loadAmount():
    F = open("questions.txt","r")
    line = F.readline()
    amount = int(line)
    
    return amount

def startGame():
    score = 0
    totQuestions = loadAmount()
    for i in range (0,totQuestions):
        win.blit(background,(0,0))

        question = {}
        load_question(question,i+1)
        check = print_question(question,score)

        if(check == True):
            i =0
            score += 1
            while(i < 150):
                win.blit(background,(0,0))
                i = i + 1 

                correct = TITLE_FONT.render("CORRECT",1,GREEN)
                win.blit(correct,(WIDTH/2 - correct.get_width()/2,30))

                win.blit(correctEmoji,(WIDTH/2-correctEmoji.get_width()/2,100))
                pygame.display.update()

        elif(check == False):
            i =0
            while(i < 150):
                win.blit(background,(0,0))
                i = i + 1 

                wrong = TITLE_FONT.render("WRONG",1,RED)
                win.blit(wrong,(WIDTH/2 - wrong.get_width()/2,30))

                win.blit(wrongEmoji,(WIDTH/2-wrongEmoji.get_width()/2,100))

                pygame.display.update()

        pygame.display.update() 
    return score

def load_question(question,questionNR):
    keywords = ["vraag","answerA","answerB","answerC","correct_answer"]

    lineNR = 5 * (questionNR-1) + 2
    for i in range (0,5):
        line = linecache.getline("questions.txt",lineNR)
        if(i<5):
            question[keywords[i]] = line[:-1]
        else:
             question[keywords[i]] = line
        lineNR += 1

def print_score(score):
    print(score)
    score = str(score)
    text = SCORE_FONT.render("Score: "+score,1,BLACK)
    win.blit(text,(800,50))

def print_question(question,score):

    questionVraag = QUESTION_FONT.render(question['vraag'],1,BLACK)
    win.blit(questionVraag,(WIDTH/2 - questionVraag.get_width()/2,20))

    andwoordA = question['answerA']
    andwoordB = question['answerB']
    andwoordC = question['answerC']

    answerAButton = button(LIGHT_BLUE,(WIDTH/2-500/2),150,500,50,andwoordA)
    answerAButton.draw(win,(0,0,0))
    anwserBButton = button(LIGHT_BLUE,(WIDTH/2-500/2),210,500,50,andwoordB)
    anwserBButton.draw(win,(0,0,0))
    answerCButton = button(LIGHT_BLUE,(WIDTH/2-500/2),270,500,50,andwoordC)
    answerCButton.draw(win,(0,0,0))

    print_score(score)
    pygame.display.update()

    check = None    
    while(check == None):
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if(event.type == pygame.MOUSEBUTTONDOWN):
                if(answerAButton.isOver(pos)):
                    check =  check_answer("A",question['correct_answer'])
                    return check
                elif(anwserBButton.isOver(pos)):
                    check = check_answer("B",question['correct_answer'])
                    return check
                elif(answerCButton.isOver(pos)):
                    check = check_answer("C",question['correct_answer'])
                    return check
                continue


def check_answer(userInput,correct_answer):
    if(userInput == correct_answer):
        return True
    else:
        return False

def getHighScore():
    with open('questions.txt','r') as file:
        for line in file:
            pass
        highscore = line
        return highscore



def draw_highScore():
    highscore = getHighScore()
    text = MIDDLE_FONT.render("HighScore: "+highscore,1,BLACK)
    win.blit(text,(WIDTH/2 - text.get_width()/2,400 ))
    


#main loop of the game
def main():
    clock = pygame.time.Clock()
    run = True
    while(run):
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_mainscreen()

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
        if(event.type == pygame.MOUSEBUTTONDOWN):
            if(mainButton.isOver(pos)):
                score = startGame()
                highscore = getHighScore()
                highscore = int(highscore)
                if(score > highscore):
                    F = open("questions.txt","a")
                    F.write(getHighScore())
                    F.close()


    pygame.quit()


if __name__ == "__main__": #runs the game only when this file is run, not when imported by another file
    main()


pygame.quit()