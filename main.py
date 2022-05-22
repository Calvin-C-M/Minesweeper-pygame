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

def generate_fields(col:int,row:int,rectSize=16,initX=0,initY=0) -> list :
    fields=[]
    posY=initY
    
    for c in range(0,col) :
        fieldsRow=[]
        posX=initX

        for r in range(0,row) :
            field=Field(posX,posY,rectSize,False,0)
            posX += rectSize+1
            fieldsRow.append(field)
        posY += rectSize+1
        fields.append(fieldsRow)
    return fields

def generate_mine_index(col:int,row:int) -> list :
    mineIndexes=[]
    totalMines=row*col
    for i in range(0,int(math.sqrt(row*col))) :
        mineIndexes.append(random.randint(0,totalMines))

    return mineIndexes

def generate_mines(oldFields:list,row:int,col:int) -> list :
    mineIndex=generate_mine_index(col,row)
    fields=oldFields
    index=0
    for c in range(0,col) :
        for r in range(0,row) :
            if index in mineIndex :
                fields[c][r].isMine=True
                if c-1 > 0 :
                    if r-1 >= 0 :
                        fields[c-1][r-1].value += 1
                    fields[c-1][r].value += 1
                    if r+1 < row :
                        fields[c-1][r+1].value +=1

                if r-1 >= 0 :
                    fields[c][r-1].value += 1
                if r+1 < row :
                    fields[c][r+1].value += 1

                if c+1 < col :
                    if r-1 >= 0 : 
                        fields[c+1][r-1].value += 1
                    fields[c+1][r].value += 1
                    if r+1 < row :
                        fields[c+1][r-1].value += 1
            index += 1 
    return fields

def main() :
    gameRunning=True
    clock=pygame.time.Clock()

    row=16
    col=16

    fields=generate_fields(col,row,30,10,10)
    fields=generate_mines(fields,row,col)

    while gameRunning :
        clock.tick(FPS)
        
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                gameRunning=False

        update_window(fields)
    return 0

main()