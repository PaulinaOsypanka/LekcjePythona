import turtle
import random
import time

#blokowanie kliknięć przed obliczeniem poprzedniego :D
czygotowe = True


window = turtle.Screen()
BOK = 600
X = -300
Y = 300
window.setup(BOK, BOK)
window.title('Kółko i krzyżyk')
window.bgcolor('black')
xo = turtle.Turtle()
xo.color('white')
xo.speed(78)
xo.pensize(7)
#xo.hideturtle()
tablica = [[None, None, None],
           [None, None, None],
           [None, None, None]]
kolej = random.choice(['x', 'o'])
# linie
ODSTĘP = int(BOK / 3)
for a in [1, 2]:
    xo.penup()
    xo.goto(X + a * ODSTĘP, Y)
    xo.pendown()
    xo.goto(X + a * ODSTĘP, -Y)
    xo.penup()
    xo.goto(X, Y - a * ODSTĘP)
    xo.pendown()
    xo.goto(-X, Y - a * ODSTĘP)


def sprawdz():
    # po skosie
    if tablica[0][0] == tablica[1][1] == tablica[2][2]: return tablica[2][2]
    if tablica[0][2] == tablica[1][1] == tablica[2][0]: return tablica[2][0]
    # w wierszu
    for w in range(3):
        if tablica[w][0] != None and tablica[w][0] == tablica[w][1] == tablica[w][2]: return tablica[w][0]

    # w kolumnie
    for k in range(3):
        if tablica[0][k] != None and tablica[0][k] == tablica[1][k] == tablica[2][k]: return tablica[0][k]
    
    return None


def click(x, y):
    global kolej

    global czygotowe
    if czygotowe != True:
        return
    czygotowe = False
    # które to pole
    kolumna = 0
    wiersz = 0
    if x < X + ODSTĘP:
        kolumna = 0
    elif x > X + 2 * ODSTĘP:
        kolumna = 2
    else:
        kolumna = 1
    if y < Y - 2 * ODSTĘP:
        wiersz = 2
    elif y > Y - ODSTĘP:
        wiersz = 0
    else:
        wiersz = 1
    # pole jest puste ?
    if tablica[wiersz][kolumna] != None: return
    # narysować
    kolumna_środek = (kolumna * ODSTĘP + ODSTĘP / 2) - BOK / 2
    wiersz_środek = (-wiersz * ODSTĘP - ODSTĘP / 2) + BOK / 2
    xo.penup()
    xo.goto(kolumna_środek - 25, wiersz_środek - 25)
    #pisz z lub o
    xo.write(kolej, font=('Turtul', 50))

    tablica[wiersz][kolumna] = kolej
    #czyja kolej
    if kolej == 'o':
        kolej = 'x'
    elif kolej == 'x':
        kolej = 'o'
    # sprawdź
    if sprawdz() != None:
        xo.penup()
        xo.goto(-150, 0)
        xo.clear()
        xo.write(" Wygrało " + sprawdz(), font=("Turtul", 50))
        return

    czygotowe = True


window.onclick(click)
window.listen()
window.mainloop()
