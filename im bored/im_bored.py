
andu = []

andu.append('d')
andu.append('z')
andu.append('i')
andu.append('e')
andu.append('c')
andu.append('k')
andu.append('o')

print(andu)

print(andu[3])

slon = []
slon = ['s', 'ł', 'o', 'n', 'i', 'a']

andu.extend(slon)

print(andu)

del andu[10]

print(andu)



gdzie_jest_o = andu.index('o')

print('no, o jest na pozycji ', gdzie_jest_o)