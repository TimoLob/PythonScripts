#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame
import numpy as np
import random
import time
pygame.init()


# In[2]:


screen = pygame.display.set_mode((400,800))
width, height = 100,200
print(width,height)
grid = np.zeros((width,height))


# In[3]:


def nextStep(grid):
    width, height = grid.shape
    nextGrid = np.zeros((width,height))
    for i in range(width):
        for j in range(height):
            sumOfNeighbors = 0
            for k in (-1,0,1):
                for l in (-1,0,1):
                    x = (i+k+width) % width
                    y = (j+l+height) % height
                    sumOfNeighbors+=grid[x][y]
            sumOfNeighbors -= grid[i][j]
            if sumOfNeighbors == 3:
                nextGrid[i][j]=1
            elif grid[i][j]==1 and sumOfNeighbors in (2,3):
                nextGrid[i][j]=1
                #print("keep alive",i,j)

    #print(nextGrid)
    return nextGrid
                


# In[4]:


def draw(grid,w,h):
    width ,height = grid.shape
    tilesize = int(np.min((w/width,h/height)))

    canvas = pygame.Surface((w,h))
    for i in range(width):
        for j in range(height):
            color = (0,0,0)
            if grid[i][j]:
                color = (255,255,255)
            pygame.draw.rect(canvas,color,(i*tilesize,j*tilesize,tilesize,tilesize),0)

    return canvas


# In[5]:


def initRandomly(grid,num):
    width,height = grid.shape
    for n in range(num):
        x = random.randint(0,width-1)
        y = random.randint(0,height-1)
        grid[x][y]=1

    return grid


# In[6]:


running = True
pause = False
grid = initRandomly(grid,5000)
clock = pygame.time.Clock()
screenwidth, screenheight = screen.get_size()
tilesize = int(np.min((screenwidth/width,screenheight/height)))
framecount = 0


# In[7]:


while running:
    if pygame.mouse.get_pressed()[0]:
        x,y = pygame.mouse.get_pos()
        x = int(x/tilesize)
        y = int(y/tilesize)
        print(x,y)
        grid[x][y]=1
    elif pygame.mouse.get_pressed()[2]:
        x,y = pygame.mouse.get_pos()
        x = int(x/tilesize)
        y = int(y/tilesize)
        print(x,y)
        grid[x][y]=0
    screen.blit(draw(grid,screenwidth,screenheight),(0,0,screenwidth,screenheight))
    if not pause and framecount % 60==0:
        grid = nextStep(grid)
    
    pygame.display.update()

    #clock.tick(10)
    framecount+=1
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            pygame.quit()
        elif(event.type == pygame.KEYDOWN):
            if event.key == pygame.K_SPACE:
                pause = not pause


# In[ ]:





# In[ ]:




