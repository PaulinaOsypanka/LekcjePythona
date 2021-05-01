import pygame


def srodek_elipsy(a,b,c,d):
    i = a+c/2
    j = b+d/2
    return (i,j)

def wsp_elipsy(k,l,x,y):
    e = k-x/2
    f = l-y/2
    g = x
    h = y
    return(e,f,g,h)


def do_gory(a,b,c,d, kolor1, kolor2):
    (i,j) = srodek_elipsy(a,b,c,d)
    # druga na górze
    (e,f,g,h) = wsp_elipsy(i,b,c/2,d/3)
    pygame.draw.ellipse(screen,kolor1,[e,f,g,h],0)
    a=e
    b=f
    c=g
    d=h
    (i,j) = srodek_elipsy(a,b,c,d)
    (e,f,g,h) = wsp_elipsy(i,b,c/2,d/3)
    # 3 na górze
    pygame.draw.ellipse(screen,kolor2,[e,f,g,h],0)


def do_lewej(a,b,c,d, kolor1, kolor2):
    (i,j) = srodek_elipsy(a,b,c,d)
    # druga po lewej
    (e,f,g,h) = wsp_elipsy(a,j,c/4,d/2)
    pygame.draw.ellipse(screen,kolor1,[e,f,g,h],0)
    a=e
    b=f
    c=g
    d=h
    (i,j) = srodek_elipsy(a,b,c,d)
    (e,f,g,h) = wsp_elipsy(a,j,c/4,d/2)
    # 3 na górze
    pygame.draw.ellipse(screen,kolor2,[e,f,g,h],0)

def do_prawej(a,b,c,d, kolor1, kolor2):
    (i,j) = srodek_elipsy(a,b,c,d)
    # druga po lewej
    (e,f,g,h) = wsp_elipsy(a+c,j,c/4,d/2)
    pygame.draw.ellipse(screen,kolor1,[e,f,g,h],0)
    a=e
    b=f
    c=g
    d=h
    (i,j) = srodek_elipsy(a,b,c,d)
    (e,f,g,h) = wsp_elipsy(a+c,j,c/4,d/2)
    # 3 na górze
    pygame.draw.ellipse(screen,kolor2,[e,f,g,h],0)



pygame.init()
screen=pygame.display.set_mode([640,480])
screen.fill([255,255,255])
a = 100
b = 100
c = 400
d = 300

kolor0 = [255,204,153]
kolor1 = [165,110,19]
kolor2 = [0,110,0]

# pierwsza elipsa
pygame.draw.ellipse(screen,kolor0,[a,b,c,d],0)



do_gory(a,b,c,d,kolor1,kolor2)
do_lewej(a,b,c,d,kolor1,kolor2)
do_prawej(a,b,c,d,kolor1,kolor2)
 








pygame.display.flip()
koniec=False
while(not koniec): 
    for event in pygame.event.get(): 
        if event.type ==pygame.QUIT:
            koniec=True
pygame.quit()