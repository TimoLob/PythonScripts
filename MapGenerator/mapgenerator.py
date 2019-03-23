import time
from noise import *
import numpy as np
import pygame
import math
import random
import sys
#https://en.wikipedia.org/wiki/Point_in_polygon


width,height = 1000,1000
#random.seed(31)
seedx = random.randint(0,100000)
seedy = random.randint(0,100000)
tilesize = 1
rec=0


pygame.init()


screen = pygame.display.set_mode([width,height])


class Map:
    numContinents = random.randint(5,7)
    numIslands = random.randint(10,100)
    tilesX,tilesY = 1000,1000
    continents = []
    tilemap = None

    def generateContinent(self,x,y,size):
        global screen
        global tilesize
        currentX=x
        currentY=y
        for i in range(size):
            placed=False


            while not placed:
                r = random.randint(0,3)
                if(r==0):
                    currentX+=1
                elif(r==1):
                    currentX-=1
                elif(r==2):
                    currentY-=1
                elif(r==3):
                    currentY+=1

                if(currentX<0):
                    currentX = 0
                if(currentY<0):
                    currentY = 0
                if(currentX>=self.tilesX):
                    currentX = self.tilesX-1
                if(currentY>=self.tilesY):
                    currentY = self.tilesY-1
                if(self.tilemap[currentX][currentY]==0):
                    self.tilemap[currentX][currentY]=1
                    placed=True
                    #print(tilesize)
        self.draw(screen,tilesize)


    def __init__(self):
        self.tilemap = [[0 for x in range(self.tilesY)] for y in range(self.tilesX)]
        for i in range(self.numContinents):
            self.generateContinent(random.randint(0,self.tilesX),random.randint(0,self.tilesY),random.randint(500,3000)*5)
        for i in range(self.numIslands):
            self.generateContinent(random.randint(0,self.tilesX),random.randint(0,self.tilesY),random.randint(10,20)*5)

    def draw(self,screen,tilesize):
        screen.fill([0,10,200])
        color = [0,200,0]
        for x in range(self.tilesX):
            for y in range(self.tilesY):
                if self.tilemap[x][y]==1:
                    #print(x,y,tilesize)
                    #pygame.draw.rect(screen,color,[x*tilesize,y*tilesize,(x+1)*tilesize,(y+1)*tilesize],0)
                    screen.set_at([x,y],color)

        pygame.display.flip()

# True if point is in Shape
def rayCheck(shape,point,rightmost):
    crosses = 0
    #print(point)
    for x in range(point[0],rightmost):
        if [x,point[1]] in shape:
            crosses+=1
    return not crosses%2==0



def genFromShape(map,points):
    tilemap = map.tilemap
    topleft = [1000,1000]
    bottomright = [0,0]

    for p in points:
        if p[0]<topleft[0]:
            topleft[0]=p[0]
        if p[1]<topleft[1]:
            topleft[1]=p[1]

        if p[0]>bottomright[0]:
            bottomright[0]=p[0]
        if p[1]>bottomright[1]:
            bottomright[1]=p[1]

    print(topleft,bottomright)
    for x in range(topleft[0],bottomright[0]):
        for y in range(topleft[1],bottomright[1]):
            if(rayCheck(points,[x,y],bottomright[0])):
                tilemap[x][y]=1


mousePressed=False
draggedPoints = []
red,green,blue = [255,0,0],[0,255,0],[0,0,255]
lineColor=red

map = Map()

start = time.time()
map.draw(screen,tilesize)
end = time.time()
print(end-start)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousePressed=True
        elif event.type == pygame.MOUSEBUTTONUP:
            mousePressed=False
        elif(event.type == pygame.KEYDOWN):
            if event.key == pygame.K_SPACE:
                genFromShape(map,draggedPoints)
                draggedPoints=[]
                map.draw(screen,tilesize)
            elif event.key == pygame.K_r:
                lineColor=red
            elif event.key == pygame.K_g:
                lineColor=green
            elif event.key == pygame.K_b:
                lineColor=blue
    if mousePressed:
        x,y=pygame.mouse.get_pos()
        draggedPoints.append([x,y])
    if(len(draggedPoints)>2):
        pygame.draw.lines(screen,lineColor,False,draggedPoints,2)
        pygame.display.flip()
