import pygame
import Color

FIELD_COLOR=Color.WHITE
FLAG_COLOR=Color.GREEN
MINE_COLOR=Color.RED

class Field :

    def __init__(self,x:int,y:int,size=16,mine=False,value=0) :
        self.isOpen=False
        self.isFlagged=False
        self.isMine=mine
        self.value=value
        self.rect=pygame.Rect(x,y,size,size)

    def clicked(self) :
        mouse=pygame.mouse
        if self.rect.collidepoint(mouse.get_pos()) :
            if mouse.get_pressed()[0] and not self.isFlagged :
                self.isOpen=True
                print(self.value)

            if mouse.get_pressed()[2] and not self.isOpen :
                self.isFlagged=True

    def update(self,win=pygame.display) :
        if self.isOpen :
            if self.isMine :
                pygame.draw.rect(win,MINE_COLOR,self.rect,width=3)
            else :
                pygame.draw.rect(win,FIELD_COLOR,self.rect,width=3)
        else :
            if self.isFlagged :
                pygame.draw.rect(win,FLAG_COLOR,self.rect)
            else : 
                pygame.draw.rect(win,FIELD_COLOR,self.rect)