import pygame as pg
from Vektor import *

width, height = 800,800
scale = min(width, height)//40

g = 0

dx = 1e3
FPS = 60
secs = 60


def elastic_collision_2d(r1, r2, v1, v2, m1, m2):
    
    n = r1 - r2
    n = n / linalg.norm(n)
    t = array([-n[1], n[0]])

    # Velocity components along n and t
    v1n = dot(v1, n)
    v1t = dot(v1, t)
    v2n = dot(v2, n)
    v2t = dot(v2, t)

    # New normal velocities after collision (1D elastic collision formula)
    v1n_new = (v1n * (m1 - m2) + 2 * m2 * v2n) / (m1 + m2)
    v2n_new = (v2n * (m2 - m1) + 2 * m1 * v1n) / (m1 + m2)

    # Final velocities
    v1_final = v1n_new * n + v1t * t
    v2_final = v2n_new * n + v2t * t
    
    return v1_final, v2_final

class Ball():
    def __init__(self, r = 1, c = (255,255,255), x = width//2, y = height//2, vx = 0, vy = 0):
        self.r = scale*r
        self.c = c
        self.p = v(x,y)
        self.s = self.p/scale
        self.v = v(vx,vy)
        self.a = v(0,0)
        self.m = r
        self.p_list = []
    
    def draw(self, screen, t):
        pg.draw.circle(screen, self.c, self.p_list[t], self.r)

    
    def update(self):
        self.v = self.v + self.a/dx
        self.s = self.s + self.v/dx
        self.p = self.s*scale

        if self.p[0] <= self.r or self.p[0] >= width-self.r:
            self.v[0] = -1*self.v[0]

        if self.p[1] <= self.r or self.p[1] >= height-self.r:
            self.v[1] = -1*self.v[1]


baller = [Ball(r=1,c=(255,0,0), vx=15,vy=10, x=200, y=200), Ball(r=1,c=(0,255,0), x=400, y=260, vx=2, vy=12), Ball(r=1,c=(0,255,255), x=700, y=300, vx=-11, vy=20), Ball(r=1,c=(255,255,0), vx=15,vy=10, x=500, y=200), Ball(r=1,c=(255,0,255), x=400, y=500, vx=2, vy=12), Ball(r=1,c=(0,0,255), x=600, y=700, vx=-11, vy=20), Ball(r=1,c=(255,120,0), x=600, y=400, vx=-11, vy=20)]


tot_E = sum(i.m*length(i.v) for i in baller)

def frames():
    for i in range(int(dx/FPS)):
        completed = []
        for i in baller:
            for j in baller:
                if j!=i and i.r+j.r >= length (i.p-j.p) and (i,j) not in completed and (j,i) not in completed:
                    completed.append((i,j))
                    i.v, j.v = elastic_collision_2d(i.p, j.p, i.v, j.v, i.m, j.m)


        for i in baller:
            i.update()
    for i in baller:
        i.p_list.append(i.p)

frames()
    

pg.init()
clock = pg.time.Clock()



screen = pg.display.set_mode((width, height))

running = True

t=0
while t < secs*FPS:
    
        screen.fill((0,0,0))

        frames()
        for i in baller:
            i.draw(screen,t)

        t+=1

        clock.tick(FPS)
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                t = secs*FPS
pg.quit()
