import turtle
t = turtle.Turtle()
t.hideturtle()
turtle.tracer(1000)
turtle.colormode(255)
t.color((0, 150, 0))
t.penup()
t.goto(-330, 0)               #Positions the turtle nicely so that the fern is sort of centered
t.pendown()


def fern(length):
    if length <= 0.50:
        t.fd(length)          #Base case: Move forward and backward
        t.bk(length)
    else:
        t.fd(length)          
        t.lt(90)
        fern(length * 0.35)   #Calls itself after a left turn to draw a new leaf
        t.rt(180)
        fern(length * 0.35)   #Then turns 180 to draw ferns on the other side
        t.lt(90)              
        t.lt(3)               #Slight left turn to curve
        fern(length * 0.87)
        t.rt(3)
        t.bk(length)          #Returns to original position when recurses are finished
        
        
        
fern(75)
turtle.mainloop()