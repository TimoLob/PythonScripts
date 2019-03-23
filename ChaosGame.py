#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame
import random
import math


# In[2]:


pygame.init()
width = 1800
height = 1000
x = int(width/2)
y = int(height/2)
screen = pygame.display.set_mode([width,height])
screen.fill([255,255,255])

percentStep = 0.5

chaospoints = []
numPoints = 3
r = min(width/2,height/2)
for i in range(numPoints):
    angle = i * math.pi*2 / numPoints
   
    chaospoints.append([int(math.cos(angle)*r+width/2),int(math.sin(angle)*r+height/2)])


# In[3]:


color = [0,0,0]
running = True
prev = random.randint(0,len(chaospoints)-1)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #screen.fill([255,255,255])
    for point in chaospoints:
        pygame.draw.circle(screen, [0,0,255], point, 5)
    pygame.draw.circle(screen, color, [x,y], 1)
    
    ran = random.randint(0,len(chaospoints)-1)
    #if(ran==prev):
     #   continue
    tX,tY = chaospoints[ran]
    prev = ran
    x+= int(percentStep*(tX-x))
    y+= int(percentStep*(tY-y))
    #x = int((x+tX)/2)
    #y = int((y+tY)/2)
    color = [x%255,y%255,int((x*y)%255)]
    pygame.display.update()


# In[ ]:





# In[ ]:




