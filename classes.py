import pygame as pg


pg.init()
MIDDLE_FONT = pg.font.SysFont('comicans',50)

#default button
class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win):            
        pg.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            textButton = MIDDLE_FONT.render(self.text, 1, (0,0,0))
            win.blit(textButton, (self.x + (self.width/2 - textButton.get_width()/2), self.y + (self.height/2 - textButton.get_height()/2)))

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False