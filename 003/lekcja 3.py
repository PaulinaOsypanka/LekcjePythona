from random import randint
from turtle import Screen, Turtle
screen = Screen()
turtle = Turtle()

r = randint (1,5)


while True:     
    r = randint (1,10)
    direction = randint (0,2)
    if direction == 1:
        turtle.left(45)
        

    if direction == 0:
        turtle.right(45)

    turtle.forward(r)

    lans = randint (1,100000)
    
    print (str(lans) + " " + str(turtle.pos))
    if lans > 99900:
        break

        
        
    



















screen.mainloop()