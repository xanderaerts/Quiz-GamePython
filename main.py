import pygame
import os 
import linecache
from constants import *
from classes import *
import random

pygame.init()

def draw_mainscreen():
    title = TITLE_FONT.render("Quiz Game",1,BLACK)
    win.blit(background,(0,0))
    win.blit(title,(WIDTH/2 - title.get_width()/2,30))

    mainButton.draw(win)

    draw_highScore()

    pygame.display.update()


def loadAmount():
    F = open("data/questions.txt","r")
    line = F.readline()
    amount = int(line)
    
    return amount


def randomizeQ(amountQ):
    order = []
    print(amountQ)

    while(len(order) < amountQ):
        q = random.randint(1,amountQ)
        print("het getal",q)
        if(q not in order):
            order.append(q)
            print(order)
    print("order of list",order) 
    return order
           
def startGame():
    score = 0
    totQuestions = loadAmount()
    questoinsOrder = randomizeQ(totQuestions)
    for i in questoinsOrder:

        win.blit(background,(0,0))

        question = {}
        load_question(question,i)
        check = print_question(question,score)

        if(check == True):
            score += 1
            win.blit(background,(0,0))
            
            correct = TITLE_FONT.render("CORRECT",1,GREEN)
            win.blit(correct,(WIDTH/2 - correct.get_width()/2,30))

            win.blit(correctEmoji,(WIDTH/2-correctEmoji.get_width()/2,100))
            pygame.display.update()
            pygame.time.delay(800)

        elif(check == False):
            
            win.blit(background,(0,0))
            
            wrong = TITLE_FONT.render("WRONG",1,RED)
            win.blit(wrong,(WIDTH/2 - wrong.get_width()/2,30))

            win.blit(wrongEmoji,(WIDTH/2-wrongEmoji.get_width()/2,100))

            pygame.display.update()
            pygame.time.delay(800)

        pygame.display.update() 
    return score

def load_question(question,questionNR):
    keywords = ["vraag","answerA","answerB","answerC","correct_answer"]

    lineNR = 5 * (questionNR-1) + 2
    for i in range (0,5):
        line = linecache.getline("data/questions.txt",lineNR)
        if(i<5):
            question[keywords[i]] = line[:-1]
        else:
             question[keywords[i]] = line
        lineNR += 1

def print_score(score):
    score = str(score)
    text = LITTLE_FONT.render("Score: "+score,1,BLACK)
    win.blit(text,(800,50))

def print_question(question,score):

    questionVraag = QUESTION_FONT.render(question['vraag'],1,BLACK)
    win.blit(questionVraag,(WIDTH/2 - questionVraag.get_width()/2,20))

    andwoordA = question['answerA']
    andwoordB = question['answerB']
    andwoordC = question['answerC']

    answerAButton = button(LIGHT_BLUE,(WIDTH/2-500/2),150,500,50,andwoordA)
    answerAButton.draw(win)
    anwserBButton = button(LIGHT_BLUE,(WIDTH/2-500/2),210,500,50,andwoordB)
    anwserBButton.draw(win)
    answerCButton = button(LIGHT_BLUE,(WIDTH/2-500/2),270,500,50,andwoordC)
    answerCButton.draw(win)

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
    F = open("data/highscore.txt","r")
    line = F.readline()
    F.close()
    return line


def draw_highScore():
    highscore = getHighScore()
    text = MIDDLE_FONT.render("HighScore: "+highscore,1,BLACK)
    win.blit(text,(WIDTH/2 - text.get_width()/2,400 ))

def writeHighScore(score):
    F = open("data/highscore.txt","w")
    F.write(str(score))
    F.close()



def draw_EndScreen(score):
    run = True
    while(run):
        title = TITLE_FONT.render("Quiz Game",1,BLACK)
        thanks = MIDDLE_FONT.render("Thanks for playing",1,BLACK)
        score = str(score)
        scoreMessage = LITTLE_FONT.render("Je score is: "+score,1,BLACK)

        win.blit(background,(0,0))
        win.blit(title,(WIDTH/2 - title.get_width()/2,30))
        win.blit(thanks,(WIDTH/2-thanks.get_width()/2,100))
        win.blit(scoreMessage,(WIDTH/2-scoreMessage.get_width()/2,150))

        restartButton.draw(win)

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
                return False

            if(event.type == pygame.MOUSEBUTTONDOWN):
                if(restartButton.isOver(pos)):
                    run = False
                    return True

        pygame.display.update()


#main loop of the game
def main():
    clock = pygame.time.Clock()
    run = True
    while(run):
        clock.tick(FPS)
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
           
            if event.type == pygame.QUIT:
                run = False
            if(event.type == pygame.MOUSEBUTTONDOWN):
                if(mainButton.isOver(pos)):
                    score = startGame()

                    highscore = getHighScore()
                    highscore = int(highscore)
                    
                    if(score > highscore):
                        writeHighScore(score)
                    run = draw_EndScreen(score)
        draw_mainscreen()
        
    pygame.quit()


if __name__ == "__main__": #runs the game only when this file is run, not when imported by another file
    main()


pygame.quit()