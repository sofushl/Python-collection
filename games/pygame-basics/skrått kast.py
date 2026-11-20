import pygame, math, random
pygame.init()
RØD = (255, 0, 0)
GRØNN = (0, 255, 0)
BLÅ = (0,0, 255)
HVIT = (255, 255, 255)
SORT = (0,0,0)
clock = pygame.time.Clock()
width = 800
height = 600
# Setter opp vinduet
screen = pygame.display.set_mode((width, height))

running = True

xpos = 1
ypos = 599
x0 = xpos
y0 = ypos

vx = 6
vy = -20
ay = 0.4
while running:
    if xpos > width or xpos < 0:
        vx = vx * (-1)

    if ypos > height or ypos < 0:
        vy = vy * (-1)
        ypos -= 1


    screen.fill(SORT)
    pygame.draw.circle(screen, HVIT, (x0, y0), 15, 0)
    pygame.draw.circle(screen, RØD, (xpos, ypos), 15, 0)
    xpos += vx
    vy += ay
    ypos += vy

    clock.tick(60)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
