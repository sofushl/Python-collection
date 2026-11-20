import pygame
import sys

pygame.init()
RØD = (255, 0, 0)
GRØNN = (0, 255, 0)
BLÅ = (0, 0, 255)
HVIT = (255, 255, 255)

skjermstørrelse = bredde, høyde = 500, 500
skjerm = pygame.display.set_mode(skjermstørrelse) # For automatisk størrelse på skjermen skriver du ingenting i parentesen.
klokke = pygame.time.Clock()


rekt = pygame.Rect(0, 0, 20, 20) #rektangel med størrelse 20x20 piksler
rekt.center = skjerm.get_rect().center # setter midten av rektangelet i midten av skjermen

a = 1

run = True
x = 0
a_x = 0
a_y = 0

while run:
    klokke.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    knapper = pygame.key.get_pressed()

    a_x += (knapper[pygame.K_d] - knapper[pygame.K_a]) * a
    a_y += (knapper[pygame.K_s] - knapper[pygame.K_w]) * a

    if a_x > 0:
        a_x -=a/2
    if a_x < 0:
        a_x +=a/2

    if rekt.y < høyde-20:
        a_y += 1
    elif rekt.y > høyde-20:
        a_y = 0
        rekt.y = høyde-20

    print (a_y, a_x)

    rekt.x += a_x
    rekt.y += a_y


    rekt.centerx = rekt.centerx % skjerm.get_width()  #dette gjør at rektangelet dukker opp på samme sted på andre siden av skjermen hvis du går utenfor

    skjerm.fill(0)
    pygame.draw.rect(skjerm, RØD, rekt)
    pygame.display.flip()

pygame.quit()
sys.exit()


pygame.draw.rect(screen, (255,0,0),pygame.Rect(x, y, 20, 20))
