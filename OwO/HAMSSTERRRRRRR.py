import pygame
pygame.init()
ekran = pygame.display.set_mode([600,600])

zegar = pygame.time.Clock()
d = 200
c = 200
x = 300
y = 300
vx = 3
vy = 2
vdv = 4
xdx = 5 
rozmiar = 20
rozmiarek = 30
uruchomiona = True
while uruchomiona:
    zegar.tick(60)
    #rozmiar += 0.05 
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT: uruchomiona = False
        if zdarzenie.type == pygame.KEYDOWN:    #sparwdzanie czy klawisz został naciśnięty
            if zdarzenie.key == pygame.K_LEFT:  #czy klawisz w lewo jest XD (nie)
                vx -= 1
                xdx -= 1
            elif zdarzenie.key == pygame.K_RIGHT:  #klawisz w prawo is the only RIGHT way
                vx += 1
                xdx += 1
            elif zdarzenie.key == pygame.K_DOWN: #if you'r going dow then im going with you
                vy += 1
                vdv += 1
            elif zdarzenie.key == pygame.K_UP:  #upper down doesn't exist (i think)
                vy -= 1
                vdv -= 1
            elif zdarzenie.key == pygame.K_TAB:  #zatrzym sie
                x = 300
                y = 300

    ekran.fill([254, 254, 254])
    pygame.draw.circle(ekran, [255,204,102], [x,y], rozmiar, 10)
    pygame.draw.circle(ekran, [206, 182, 251], [d,c], rozmiarek, 3)
    pygame.display.flip()
    x += vx
    y += vy
    d += xdx
    c += vdv
    if(x > 600-rozmiar or x < rozmiar):
        vx *= -1
    if(y > 600-rozmiar or y < rozmiar):
        vy *= -1

    if(d > 600-rozmiarek or d < rozmiarek):
        xdx *= -1
    if(c > 600-rozmiarek or c < rozmiarek):
        vdv *= -1
pygame.quit() 