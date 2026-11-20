from numba import njit
import numpy as np
import matplotlib.pyplot as plt
from time import sleep as wait
import pygame
print("imported")

dt = 0.001
L = 150
O = 2*np.pi*L
o = O/360
m = 10
g = -9.81  *100
k = 0.00005

p1vlist = []
p1tlist = []
p2vlist = []
p2tlist = []

@njit
def update_pos(theta, v, dt):
    return theta - (v*dt/o)

@njit
def height(theta):
  if theta > 180:
    temp = 360 - theta
  else:
    temp = theta
  
  h = (np.sin(np.radians(temp-90))*L)+L
  return h  

@njit
def vel(v,theta,other):
  if height(theta) > 0:
      if theta < 180:
        v+=dt*(-g*np.cos(np.radians(theta-90)) -k*v*abs(v) +abs(other)**0.03*other*0.002) 
      elif theta > 180:
        v+=dt*(-g*np.cos(np.radians(theta-90)) -k*v*abs(v) +abs(other)**0.03*other*0.002)
  return v

@njit
def pos(theta, L):
  y = np.cos(np.radians(theta))*L
  x = np.sin(np.radians(theta))*L
  return x+400,y+400

@njit
def pos2(theta, L, otherx, othery):
  y = np.cos(np.radians(theta))*L
  x = np.sin(np.radians(theta))*L
  return x+otherx,y+othery

p1vlist = [-100]
p1tlist = [181]
p2vlist = [500]
p2tlist = [180]

p1positions = []
p2positions = []
i = 0

while i < 1000000:
    i+=1
    theta = p1tlist[-1]
    v = p1vlist[-1]
    
    theta = update_pos(theta,v,dt)
    v = vel(v,theta,p2vlist[-1])
    
    if theta >= 360:
        theta = 0
    elif theta < 0:
        theta = 360
    
    p1tlist.append(theta)
    p1vlist.append(v)
    
    otherx, othery = pos(theta,L)
    p1positions.append((otherx,othery))
    
    theta = p2tlist[-1]
    v = p2vlist[-1]
    
    theta = update_pos(theta,v,dt)
    v = vel(v,theta,p1vlist[-1]) +abs(p1vlist[-1])**0.01*p1vlist[-1]*0.001
    
    if theta >= 360:
        theta = 0
    elif theta < 0:
        theta = 360
    
    p2tlist.append(theta)
    p2vlist.append(v)    
    p2positions.append((pos2(theta,L,otherx,othery)))  

pygame.init()

clock = pygame.time.Clock()
width = 800
height = 800



screen = pygame.display.set_mode((width, height))
font = pygame.font.Font("freesansbold.ttf", int(round(width/50, 0)))
running = True
t = 0



while running:

    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (0,0,0), p1positions[t], 25, 0)
    pygame.draw.line(screen, (0, 0, 0), [400,400], p1positions[t], 5)
    
    pygame.draw.circle(screen, (0,0,0), p2positions[t], 25, 0)
    pygame.draw.line(screen, (0, 0, 0), p1positions[t], p2positions[t], 5)
    
    skrift = font.render(f"Theta 1: {p1tlist[t]:<.0f}\u00b0 Speed 1: {p1vlist[t]:<.0f}units,  Theta 2: {p2tlist[t]:<.0f}\u00b0 Speed 2: {p2vlist[t]:<.0f}units", True, (0,0,0))
    screen.blit(skrift, (0,0))



    clock.tick(10000)
    t += 1
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()