import pygame as pg
import numpy as np

def vecp(p, p1):
    return np.array([(p1[0]-p[0]),(p1[1]-p[1])])

def vec(x, y):
    return np.array([x,y])

def length(vector):
    return (vector[0]**2 + vector[1]**2)**(1/2)

def angle(u, v):
    return np.acos( (u[0]*v[0] + u[1]*v[1]) / (length(u)*length(v)) )

def rotate_vector(vector, angle):  # Convert degrees to radians
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    return np.dot(rotation_matrix, vector)

g = 0.001


# Initialiserer/starter pygame
pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 1000
VINDU_HOYDE  = 600  
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

class Ball:
  """Klasse for å representere en ball"""
  def __init__(self, x, y, fart, radius, vindusobjekt):
    """Konstruktør"""
    self.p = vec(x,y)
    self.v = vec(fart,0)
    self.radius = radius
    self.vindusobjekt = vindusobjekt
    self.next = False
    self.nextv = 0
  
  def tegn(self):
    """Metode for å tegne ballen"""
    pg.draw.circle(self.vindusobjekt, (255, 69, 0), self.p, self.radius) 


  def flytt(self):
    """Metode for å flytte ballen"""
    # Sjekker om ballen er utenfor høyre/venstre kant
    if ((self.p[0] - self.radius) <= 0) or ((self.p[0] + self.radius) >= self.vindusobjekt.get_width()):
      self.v[0] = -self.v[0]
    if (self.p[1] - self.radius) <= 0 or ((self.p[1] + self.radius) >= self.vindusobjekt.get_height()):
        self.v[1] = -self.v[1]
    else:
       self.v[1] += g

    if self.next:
       self.v = self.nextv
       self.next = False
    
    self.p = self.p+self.v  


    for i in balls:
       if self == i:
          pass
       elif length(vecp(self.p,i.p)) <= self.radius+i.radius:
          vs = self.v + i.v
          ang = angle(self.v,vs)
          if ang==0:
            self.nextv = rotate_vector(self.v, np.pi)
          else:
            self.nextv = rotate_vector(self.v, np.pi+2*ang)
          self.next = True

    
    
    

# Lager et Ball-objekt
balls = [Ball(40, 50, 0.1, 20, vindu), Ball(470, 50, 0.1, 20, vindu)] 
# Gjenta helt til brukeren lukker vinduet
fortsett = True
while fortsett:

    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    # Farger bakgrunnen lyseblå
    vindu.fill((135, 206, 235))

    # Tegner og flytter ballen
    for i in balls:
        i.tegn()
        i.flytt()

    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()