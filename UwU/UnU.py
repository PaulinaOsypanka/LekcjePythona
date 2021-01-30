def monej(grosz,gr2,gr5,gr10,gr20,gr50,zl1):
    grosiczki = grosz + gr2*2 + gr5*5 + gr10*10 + gr20*20 + gr50*50 + zl1 *100
    zloty = grosiczki/100
    return zloty

A = monej(3,6,0,5,6,30,10)
print(A)

B = monej(20,10,15,13,0,0,2)
print(B)

C = monej(100,180,5,0,0,0,0)
print(C)

all = C + B + A
print(all)