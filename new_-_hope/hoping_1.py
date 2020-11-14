print(4*6)
print("jaś jest głupi")
print('oh shit, here we go again')
print("it\'s a \\\\ rainy day")



dniwtyg = 7
minwh = 60
hwdniu = 24
h25wdniu = 25

doba25tyg = dniwtyg*minwh*h25wdniu
dobatyg = dniwtyg*minwh*hwdniu


print(dniwtyg*minwh*hwdniu)
print(dniwtyg*minwh*h25wdniu)
print("wynik:")
print(doba25tyg-dobatyg)

print("Gdyby doba miałaby 25h zyskalibyśmy 420 minut tygodnjowo")

print(10//3)
print("reszta: "+ str(10%3))




a=12.5
b=16.7

print("Pole: "+str(a*b))
print("Obwód: "+str(a*2+2*b))


print(89.59*0.15)
print(13.4385+89.59)
print(103.0285/3)
print('34.34')


rachunek = input("Jaki był rachunek? ")
liczba_osob = input("Ile osób? ")
procnapiw = input("Ile chcesz zapłacić napiwku? ")

rachunek = float(rachunek)
liczba_osob = int(liczba_osob)
procnapiw = int(procnapiw)
napiwekwartosc = procnapiw*0.01
napiwek = rachunek*napiwekwartosc
rachnapiw = rachunek + napiwek


print("Jedna osoba płaci: "+str(rachnapiw/liczba_osob))

droga = input('Długość drogi km ')
predkosc = input('Prędkosc km/h ')


print('Długość drogi wynosi: '+ str(droga)+ ' km')
