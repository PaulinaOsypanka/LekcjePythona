class Ball:
    size = 5
    direction = None
    material = "wood"
    color = "brown"
    weight = 5

    def __init__(self,size):
        self.size = size


smallBall = Ball(4)
bigBall = Ball(44)

print(smallBall.size)
print(bigBall.size)

class Postac:
    imie = "Amenikorunika"
    czy_idzie = False
    ktora_strona = None
    
    
    def __init__ (self,imie):
        self.imie = imie

    def Idz(self,ktora_strona_wyw):
        self.czy_idzie = True
        self.ktora_strona = ktora_strona_wyw

    def Stoj(self):
        self.czy_idzie = False
        self.ktora_strona = None


postac1 = Postac("Komputrominka")
postac2 = Postac("Amenikorunika")

print(postac1.imie)
print(postac2.imie)

postac2.Idz(ktora_strona_wyw="Prawo")
print(postac2.ktora_strona)

postac2.Stoj()
print(postac2.ktora_strona)
print(postac2.czy_idzie)
