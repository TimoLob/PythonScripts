#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame
from pygame.math import Vector2
import random


# In[2]:


pygame.init()
height = 800
width = 800
screen = pygame.display.set_mode((height, width))
pygame.display.set_caption('Flocking Simulation')
clock = pygame.time.Clock()


# In[3]:


class Flock:
    def __init__(self,width,height,num):
        self.w = width
        self.h = height
        self.num = num
        self.boids = []
        for _ in range(num):
            self.boids.append(Boid(self.w,self.h))
            
    def update(self):
        detectionRange = 100
        separationRange = 50
        for boid in self.boids:
            alignmentSteering = Vector2(0,0)
            cohesionSteering = Vector2(0,0)
            separationSteering = Vector2(0,0)
            total = 0
            sepTotal = 0
            for other in self.boids:
                if boid!=other:
                    dist = boid.pos.distance_to(other.pos)
                    if dist < detectionRange:
                        alignmentSteering+=other.vel
                        cohesionSteering+=other.pos
                        total+=1
                    if dist < separationRange and dist>0:
                        diff = boid.pos-other.pos
                        diff /= (dist*dist)
                        separationSteering+=diff
                        sepTotal+=1
            if total!=0:
                #print(total)
                alignmentSteering/=total
                cohesionSteering/=total
                cohesionSteering-=boid.pos
                alignmentSteering.scale_to_length(boid.maxSpeed)
                alignmentSteering.scale_to_length(boid.maxSpeed)
                alignmentSteering-=boid.vel
                cohesionSteering-=boid.vel

                boid.applyForce(alignmentSteering)
                boid.applyForce(cohesionSteering)
            if sepTotal!=0:
                separationSteering/=sepTotal
                separationSteering.scale_to_length(boid.maxSpeed)
                separationSteering-=boid.vel
                boid.applyForce(separationSteering)
            boid.update()
            
            
    def draw(self,screen):
        for boid in self.boids:
            x = int(boid.pos.x)
            y = int(boid.pos.y)
            pygame.draw.circle(screen,[0,0,255],[x,y],3)
                    


# In[4]:


class Boid:
    def __init__(self,w,h):
        self.w = w
        self.h = h
        self.pos = Vector2(random.randint(0,w),random.randint(0,h))
         
        self.vel = Vector2(1,0)
        self.vel = self.pos.rotate(random.randint(0,360))
        self.acc = Vector2(0,0)
        self.mass = 1
        self.maxSpeed = 2
        self.maxForce = 0.02
        
    def update(self):
        
        
        self.pos = self.pos + self.vel
        self.vel = self.vel + self.acc
        self.acc *= 0
        self.vel.scale_to_length(min(self.vel.length(),self.maxSpeed))
        
        if self.pos.x > self.w:
            self.pos.x = 0
        elif self.pos.x < 0:
            self.pos.x = self.w
        if self.pos.y > self.h:
            self.pos.y = 0
        elif self.pos.y < 0:
            self.pos.y = self.h
            
        
    
    def applyForce(self,f):
        f/=self.mass
        if f.length()<0.00001:
            return
        f.scale_to_length(min(self.maxForce,f.length()))
        self.acc += f
        #print(self.acc)


# In[5]:


flock = Flock(width,height,200)


# In[6]:


running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill([0,0,0])
    flock.update()
    flock.draw(screen)
    pygame.display.update()


# In[ ]:





# In[ ]:




