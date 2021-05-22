import pygame
pygame.init()
ekran = pygame.display.set_mode([600,600])
class Pikachu:
    def __init__ (self, rozmiar, x, y, vx, vy, ekranix, ekran_i_grek, kolor):
        self.rozmiar = rozmiar
        self.kolor = kolor
        self.x = x
        self.y = y
        self.vx = vx 
        self.vy = vy
        self.ekranix = ekranix 
        self.ekran_i_grek = ekran_i_grek

    def anime(self, ish):
        self.ish = ish
        if(self.x > self.ekranix - self.rozmiar or self.x < self.rozmiar):
            self.vx *= -1
        if(self.y > self.ekran_i_grek - self.rozmiar or self.y < self.rozmiar):
            self.vy *= -1
        self.x += self.vx
        self.y += self.vy
        pygame.draw.circle(ekran, self.kolor, [self.x,self.y], self.rozmiar, 5)


    def nowicjusz(self,clownfish):
        if clownfish == pygame.K_LEFT:  #czy klawisz w lewo jest XD (nie)
                self.vx -= 1
        elif clownfish == pygame.K_RIGHT:  #klawisz w prawo is the only RIGHT way
                self.vx += 1
        elif clownfish == pygame.K_DOWN: #if you'r going dow then im going with you
                self.vy += 1
        elif clownfish == pygame.K_UP:  #upper down doesn't exist (i think)
                self.vy -= 1
        elif clownfish == pygame.K_TAB:  #zatrzym sie
                self.x = 300
                self.y = 300



zegar = pygame.time.Clock()
ekranix = 600
ekran_i_grek = 600
ish = 'soup'
x = 300
y = 300
vx = 3
vy = 2
rozmiar = 20
uruchomiona = True
Pika = [Pikachu(49,400,300,vx,vy,ekranix,ekran_i_grek,[197, 198, 255]), Pikachu(rozmiar, x, y, vx, vy, ekranix, ekran_i_grek,[247, 223, 213]), Pikachu(20,30,40,3,8,ekranix, ekran_i_grek,[210, 248, 221])]
while uruchomiona:
    zegar.tick(60)
    #rozmiar += 0.05 
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT: uruchomiona = False
        if zdarzenie.type == pygame.KEYDOWN:    #sparwdzanie czy klawisz został naciśnięty
            for a in Pika:
                a.nowicjusz(zdarzenie.key)
            
           

    ekran.fill([000, 000, 000])
    for i in Pika:
        i.anime(ish)
    pygame.display.flip()


    

pygame.quit() 