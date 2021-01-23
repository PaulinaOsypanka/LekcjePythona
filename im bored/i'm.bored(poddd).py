i_lista = []

for i in range(5):
   i_lista.append(input('Daj imie ' + str(i+1) + ' '))

print(i_lista)

sorting = input('Czy chcesz posortować swoją listę imion? (wpisz \'tak\' lub \'nie\')')

sorting.lower()

if sorting == 'tak'
    i_lista.sort()
    print(i_lista)

elif sorting == 'nie'
    print('Ugh, czemu nie? \*foch\*')

else:
    print('syntax error')
