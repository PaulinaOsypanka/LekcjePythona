import pygame, sys

pygame.init()
screen=pygame.display.set_mode([640,480])
screen.fill([255,255,255])
pygame.draw.ellipse(screen,[255,204,153],[150,100,220,150],0)
pygame.draw.ellipse(screen,[165,110,19],[222,80,68,49],0)
pygame.display.flip()
koniec=False
while(not koniec): 
    for event in pygame.event.get(): 
        if event.type ==pygame.QUIT:
            koniec=True
pygame.quit()