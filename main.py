import math
import pygame
import Color
import random
from Field import Field
# from Text import GENERAL_TEXT as gt
# from Text import GAME_OVER_TEXT as go

pygame.init()
WIDTH,HEIGHT=640,640
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Minesweeper")

FPS=60

def update_window(fields) :
    WIN.fill(Color.BLACK)

    for fieldRow in fields :
        for field in fieldRow :
            field.clicked()
            field.update(WIN)

    pygame.display.update()
    pygame.display.flip()

def generate_fields(row:int,col:int,rectSize=16,initX=0,initY=0) -> list :

    mineIndexes=[]
    totalMines=row*col
    for i in range(0,int(math.sqrt(row*col))) :
        mineIndexes.append(random.randint(0,totalMines))

    fields=[]
    posY=initY
    index=0
    
    for c in range(0,col) :
        fieldsRow=[]
        posX=initX

        for r in range(0,row) :
            field=Field(posX,posY,rectSize,False,0)
            if index in mineIndexes :
                field.isMine=True
                if c-1 > 0 :
                    if r-1 > 0 :
                        fields[c-1][r-1].value += 1
                    fields[c-1][r].value += 1
                    if r+1 < row :
                        fields[c-1][r+1].value += 1
                if r-1 > 0 :
                    fields[c][r-1].value += 1
                if r+1 < row :
                    fields[c][r+1].value += 1
                if c+1 < col :
                    if r-1 > 0 :
                        fields[c+1][r-1].value += 1
                    fields[c+1][r].value += 1
                    if r+1 < row :
                        fields[c+1][r+1].value += 1
            posX += rectSize+1
            fieldsRow.append(field)
            index += 1
        posY += rectSize+1
        fields.append(fieldsRow)
    return fields

# def initiate_field_values(oldFields:list,row:int,col:int) -> list :
#     fields=oldFields

#     return fields

def main() :
    gameRunning=True
    clock=pygame.time.Clock()

    fields=generate_fields(16,16,30,10,10)

    while gameRunning :
        clock.tick(FPS)
        
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                gameRunning=False

        update_window(fields)
    return 0

main()