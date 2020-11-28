litery = []

litery.append('a')
litery.append('b')
litery.append('c')
litery.append('d')
litery.append('e')
litery.append('z')
litery.append('o')


print (litery)

litery.sort()

print (litery)


litery[3] = 'x'

print (litery)

nowe_litery = []

nowe_litery.append('d')
nowe_litery.append('m')


litery.extend(nowe_litery)

print (litery)

litery.insert(4, nowe_litery)

print (litery)

920935734

