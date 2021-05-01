import pygame
pygame.init()
ekran = pygame.display.set_mode([600,600])

zegar = pygame.time.Clock()

x = 300
y = 300
vx = 2
vy = 1
rozmiar=30
uruchomiona = True
while uruchomiona:
    zegar.tick(60)
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT: uruchomiona = False
    ekran.fill([255, 255, 255])
    pygame.draw.circle(ekran, [255,0,0], [x,y], rozmiar, 1)
    pygame.display.flip()
    x += vx
    y += vy
    if(x > 600-rozmiar or x < rozmiar):
        vx *= -1
    if(y > 600-rozmiar or y < rozmiar):
        vy *= -1
pygame.quit() 