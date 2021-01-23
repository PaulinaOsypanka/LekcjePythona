imiona=['Paula','Jaś','Patryk','Jakiś random']
imionka= imiona[:2]

print(imiona[:3])

print(imiona[2:4])
print(imiona[2:])

print(len(imiona))
print(len(imionka))

u_miecia = imiona[:]
imioneczka_czwóreczka = imiona

imioneczka_czwóreczka[3] = 'coś'

print(imiona)
print(imioneczka_czwóreczka)
print(u_miecia)



