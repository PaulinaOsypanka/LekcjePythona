from turtle import Screen, Turtle


screen = Screen()
turtle = Turtle()

for x in range (360):
    turtle.forward(x)
    turtle.left(100)
turtle.forward(100)

screen.mainloop()