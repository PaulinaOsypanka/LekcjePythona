punkty = input('Ile punktów wostałeś? ')

if int(punkty) > 65:
    print('5 lub wyżej. Nieźle :D')
elif int(punkty) == 65:
    print('4 lub 3. Nawet spoko.')
elif int(punkty) < 65:
    print('2 lub niżej, słabo.')
else:
    print('SYNTAX ERROR')


punkty = int(input('Ile punktów dostałeś? '))


if punkty == 100:
    print('Brawo, dostał*ś 6! (Wszyscy wiemy, że ściągał*ś)')
elif punkty == 90 or punkty > 90:
    print('5, nieźle')
elif punkty == 80 or punkty > 80:
    print('4, nawet spoczko :D')
elif punkty == 70 or punkty > 70:
    print(['3, uczył*ś się?'])
elif punkty == 60 or punkty > 60:
    print('Jejjj 2! WOW! Ale się cieszę, że nie 1')
else:
    print('Jedyneczka do dzienniczka :D')
