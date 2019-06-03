import turtle
bob = turtle.Turtle()
turtle.tracer(1000)
turtle.colormode(255)
bob.color(0,230,255)
bob.pensize(2)
bob.hideturtle()


def koch(length, depth):
    if depth == 0:
        bob.fd(length)
    else:
        koch(length / 3, depth - 1)
        bob.lt(60)
        koch(length / 3, depth - 1)
        bob.rt(120)
        koch(length / 3, depth - 1)
        bob.lt(60)
        koch(length / 3, depth - 1)
        

        
        
for i in range(3):
    koch(200, 5)
    bob.rt(120)
turtle.mainloop()