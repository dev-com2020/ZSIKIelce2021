import turtle

t = turtle.Turtle()
t.shape('turtle')
t.color('red')
t.pensize(7)
t.penup()
t.goto(-200,100)
t.pendown()
t.forward(300)

t.shape('turtle')
t.color('blue')
t.pensize(7)
t.penup()
t.goto(-200,-100)
t.pendown()
t.forward(300)

turtle.exitonclick()