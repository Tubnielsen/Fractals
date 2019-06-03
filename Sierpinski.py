import turtle
bob = turtle.Turtle()
turtle.tracer(1000)
turtle.colormode(255)
bob.fillcolor(255,0,0)
bob.hideturtle()


def sierpinski(length, depth):
    if depth == 0:
        bob.begin_fill()
        for i in range(3):
            bob.fd(length)
            bob.lt(120)
        
        bob.end_fill()
        
    else:
        sierpinski(length / 2, depth - 1)
        bob.fd(length / 2)
        sierpinski(length / 2, depth - 1)
        bob.bk(length / 2)
        bob.lt(60)
        bob.fd(length / 2)
        bob.right(60)
        sierpinski(length/2,depth-1)
        bob.left(60)
        bob.bk(length/2)
        bob.right(60)
        
        
        
sierpinski(300,5)
        
turtle.mainloop()
        
        
        
        
