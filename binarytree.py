import turtle
import sys

def b(t, s, depth, ps, color):
  t.pensize(ps)
  ##if color <= 255:        ## To enable color changing through depths; dark -> light
  ##  t.color(0, color, 0)
  ##else:
  ##  t.color(0, 255, 0)
  t.color(0, color, 0)
  
  if depth <= 0:
    t.color(0,255,0)
    t.fd(s)
    t.bk(s)
    t.color(0,color,0)
  else:
    
    t.fd(s)
    t.lt(30)
    b(t, s*0.75, depth-1, ps-0.75, color)
    t.rt(60)
    b(t, s*0.75, depth-1, ps-0.75, color)
    t.lt(30)
    t.bk(s)
    
if len(sys.argv) > 1:          #This script takes 2 arguments: Depth and pen size
  depth = int(sys.argv[1])  #Depth
else:
  depth = 5

if len(sys.argv) > 2:
  pensize = int(sys.argv[2])    #Pen size; shouldn't be too low or it will throw an error
else:                          #because it decreases in the recursive function and I haven't
  pensize = depth            #put in any lower bound

bob = turtle.Turtle()
turtle.tracer(5000)  #Enabling tracer makes it much faster

turtle.colormode(255)
color = 100

bob.hideturtle()

bob.lt(90)  #Making the tree in the right direction
bob.penup() #and starting further down
bob.bk(350)
bob.pendown()

b(bob, 200, depth, pensize, color)

turtle.mainloop()