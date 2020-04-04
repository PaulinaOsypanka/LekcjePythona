from tkinter import Tk, Canvas
from kolko_i_krzyzyk___FUNKCJE import *

tura = 1

def pozycja(klik): 
    global tura
    global zajety_kibel

     
    
    p = pole(klik.x,klik.y)


    if zajety_kibel[p - 1] == 0:
        zajety_kibel[p - 1] = tura
        print (zajety_kibel)
    else:
        return



    if p>0:
        x = (((p - 1)//3)+1)*100
        y = (((p - 1)%3)+1)*100

        
        if tura == 1:
            c.create_line(x,y,x+100,y+100)
            c.create_line(x+100,y,x,y+100)

        if tura == 2:
            c.create_oval(x,y,x+100,y+100)

    for i in range (0,3):
        if zajety_kibel[i + 3] == zajety_kibel[i + 6]:
            if tura == 1:
                print("łiner is kżyszyk")
                return
            
            if tura == 2:
                print("łiner is kułko")
                return

    if tura == 1:
        tura = 2

    else :
        tura = 1

zajety_kibel = [0,0,0,0,0,0,0,0,0]


ono = Tk ()
ono.geometry ('500x500+300+300')

c = Canvas(ono , width=5000, height=5000)
c.pack()



c.create_line(100,100,100,400)
c.create_line(100,100,400,100)
c.create_line(400,100,400,400)
c.create_line(100,400,400,400)

c.create_line(200,100,200,400)
c.create_line(300,100,300,400)
c.create_line(100,200,400,200)
c.create_line(100,300,400,300)




ono.bind("<Button 1>",pozycja)








ono.mainloop()