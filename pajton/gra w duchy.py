# Gra w duchy
from random import randint
print('Gra w duchy')
nie_mam_odwagę = True
wynik = 0

while nie_mam_odwagę:
    drzwi_ducha = randint(1, 3)
    print('Przed tobą troje drzwi...')
    print('za jednymi jest duch')
    print('które otwierasz?')
    numer = input('1, 2 czy 3: ')
    numer_drzwi = int(numer)
    if numer_drzwi == drzwi_ducha:
        print('DUCH')
        nie_mam_odwagę = False
        mam_odwagę = True
       
    else:
        print('nie ma ducha')
        print('duch był za drzwiami:',drzwi_ducha,'a ty wybrałaś/eś:',numer_drzwi)
        print('wchodzisz do następnego pokoju')
        wynik = wynik + 1
while mam_odwagę:
    drzwizduchem = randint(1, 10)
    print('po każdym zdaniu klikaj enter')
    input()
    print('walcz!')
    input()
    print('oh nie on ucieka!')
    input()
    print('teraz musisz go dogonić...')
    input()
    print('(instrukcja)wybieraj numery dzrwi, musisz się postarać aby trafić w drzwi ducha')
    print('duch wleciał do innego korytarza,w tym korytarzu jest 10 drzwi')
    input()
    print('OSTRZERZENIE')
    input()
    input()
    input()
    print('za złymi drzwiami są pułapki')
    input()
    print('dobra...')
    input()
    print('ktore drzwi wybierasz?')
    pin = input('1, 2, 3, 4, 5, 6, 7, 8, 9 czy 10???????  ')
    pin_dodrzwi = int(pin)
    if pin_dodrzwi == drzwizduchem:
        print('Świetnie! Idż dalej, tylko uważaj na pułapki!!!')

    else:

        print('Uważaj! Uchhhh to złe drzwi! Wpadłaś/eś do pułapki')
        mam_odwagę = False

print('KONIEC GRY!!!!!')
print('Dzięki, że zagrałaś/eś w moją grę!')
print('Pa pa, do następnego razu!')
