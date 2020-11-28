J = [3,3,3]
G = [0,2,1]
P = [13,10,12]

czekolady =[J,P,G]

for u in czekolady:
    print(u)



r=czekolady[2][1]
print(r*0)
print('wyjumaju ' + str(r*0))

czekolady[1][1] = 0

print(czekolady)


czekolady[1][2]=czekolady[1][2]*3

for u in czekolady:
    print(u)


