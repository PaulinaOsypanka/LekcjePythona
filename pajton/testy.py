imie=['Bartek', 'Mateusz', 'Kuba', 'Janek']
czasownik=["robi", "myje", "kupuje", "podnosi"]
rzeczownik=["dziecko", "samolot", "telefon", "książkę"]

from random import randint
def wybierz(slowo):
    liczba_slow = len(slowo)
    wybranaLiczba = randint(0, liczba_slow-1)
    wybraneSlowo = slowo[wybranaLiczba]
    return wybraneSlowo

while True:
    print(wybierz(imie), wybierz(czasownik), wybierz(rzeczownik))
    input()
