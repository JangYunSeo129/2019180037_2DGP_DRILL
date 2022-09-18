import turtle

count = 6
while count > 0:
    turtle.forward(500)
    turtle.penup()
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(500)
    turtle.left(180)
    turtle.pendown()
    count -= 1

turtle.penup()
turtle.goto(500,0)
turtle.pendown()
turtle.left(90)

count = 6
while count > 0:
    turtle.forward(500)
    turtle.penup()
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(500)
    turtle.left(180)
    turtle.pendown()
    count -= 1
turtle.exitonclick()
