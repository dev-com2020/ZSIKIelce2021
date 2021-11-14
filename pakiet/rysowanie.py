import turtle

t = turtle.Turtle()
t.shape('turtle')
turtle.bgcolor('blue')
t.color('red')
t.begin_fill()
t.circle(50)
t.end_fill()
t.penup()
t.goto(-200, 0)
t.pendown()
t.color("yellow")
t.write("Piszę w żółwiu!", font=("Arial", 30, "bold"))
t.hideturtle()
t.write(t.position())
print(t.position())


# t.forward(200)
# t.right(90)
# t.forward(150)
# t.right(90)
# t.forward(100)
# t.left(60)
# t.back(152)
# t.circle(30)
# t.home()

# t.circle(50)
# t.right(45)
# t.circle(60)
# t.right(45)
# t.circle(70)
# t.right(45)
# t.circle(80)


turtle.exitonclick()
