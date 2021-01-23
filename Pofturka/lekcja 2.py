from turtle import Screen, Turtle
from random import randint


screen = Screen()
turtle = Turtle()



for i in range(100):
    r = randint(1,100)
    direction = randint(1,2)
    print(r)
    turtle.forward(20)
    turtle.left(r)


screen.mainloop()