import turtle

def up_move():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def left_move():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def down_move():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()

def right_move():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()
    
def restart():
    turtle.reset()

turtle.shape('turtle')

turtle.onkey(up_move, 'W')
turtle.onkey(left_move, 'A')
turtle.onkey(down_move, 'S')
turtle.onkey(right_move, 'D')
turtle.onkey(restart, 'Escape')
turtle.listen()
