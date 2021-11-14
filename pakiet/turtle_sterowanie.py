import turtle

t = turtle.Turtle()

def up():
    t.forward(90)

def down():
    t.back(50)

def left():
    t.left(30)

def right():
    t.right(30)


turtle.onkey(up, 'w')
turtle.onkey(down, 's')
turtle.onkey(left, 'a')
turtle.onkey(right, 'd')

turtle.listen()
turtle.mainloop()
