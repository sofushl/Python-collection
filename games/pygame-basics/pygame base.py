import pygame, math, random
pygame.init()
clock = pygame.time.Clock()
width = 800
height = 600
screen = pygame.display.set_mode((width, height)) # Setter opp vinduet
running = True

while running:

    clock.tick(30)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
