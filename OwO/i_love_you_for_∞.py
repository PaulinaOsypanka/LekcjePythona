class HodTog:
    def __init__ (self):
        self.temperatura = 'zimny'
        self.podgrzanie = 0
        self.dodatki = []
    def podgrzej(self,czas):
        self.podgrzanie = self.podgrzanie + czas    
        if self.podgrzanie < 4:
            self.temperatura = "zimny"
        elif self.podgrzanie < 7:
            self.temperatura = "ciepły"
        elif self.podgrzanie < 10:
            self.temperatura = "goroący"
        else:
            self.temperatura = 'spalony'

    def dodaj(self,dodatek):
        self.dodatki.append(dodatek)



h1 = HodTog()
h1.podgrzej(3)
print(h1.temperatura)
h2 = HodTog()
h2.podgrzej(5)
print(h2.temperatura)
h3 = HodTog()
h3.podgrzej(7)
print(h3.temperatura)

h1.podgrzej(3)
h2.podgrzej(1)
h3.podgrzej(3)

print('PRERWAA')

print(h1.temperatura)
print(h2.temperatura)
print(h3.temperatura)

h1.dodaj('nic')

print(h1.dodatki)