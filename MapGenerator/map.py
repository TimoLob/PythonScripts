from noise import pnoise2
import numpy as np
import pygame
import math
import random
import sys

def map(x,a,b,c,d): # number,from,to,from,to
    return (x-a)/(b-a) * (d-c)+c

width,height = 1500,700
seedx = random.randint(0,100000)
seedy = random.randint(0,100000)
tilesize = 5
waterpercent = 60
pygame.init()
tilemap = [[0 for x in range(int(height/tilesize))] for y in range(int(width/tilesize))]

for x in range(int(width/tilesize)):
    for y in range(int(height/tilesize)):
        n=map(pnoise2(x/20+seedx,y/20+seedy,10),-1,1,0,100)
        tilemap[x][y]=100-n


screen = pygame.display.set_mode([width,height])
for x in range(int(width/tilesize)):
    for y in range(int(height/tilesize)):
        color = [0,10,200]
        if tilemap[x][y]<waterpercent:
            color = [0,10,200*(tilemap[x][y])/100+50]
        else:
            t = tilemap[x][y]-waterpercent+30
            color = [200*t/100,255-255*t/100+10,0]
        pygame.draw.rect(screen,color,[x*tilesize,y*tilesize,(x+1)*tilesize,(y+1)*tilesize],0)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            print(tilemap[int(x/tilesize)][int(y/tilesize)])
