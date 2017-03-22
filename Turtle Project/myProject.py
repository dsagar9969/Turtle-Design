#MyMainProgram

from myPolygon import *
from myTears2 import *
import turtle

bob=turtle.Turtle()

turtle.colormode(255)
bob.speed(0)
turtle.bgcolor("black")

#The following code draws colored magenta squares in a spiraled loop 

for times in range(256):
    bob.begin_fill()
    c=(times,255-times,0)
    bob.color(times,0,255)
    polygon(bob,4,100)
    bob.left(50)
    bob.forward(times)
    bob.end_fill()

bob=turtle.Turtle()

turtle.colormode(255)
bob.speed(0)

#The following code draws colored red triangles in a spiraled loop

for times in range(222):
    bob.begin_fill()
    c=(times,255-times,0)
    bob.color(times,0,0)
    polygon(bob,3,25)
    bob.left(50)
    bob.forward(times)
    bob.end_fill()

#The following code uses an imported tear function to draw small cyan colored lines in a circular motion

bob.left(45)
for times in range(30):
    tear2(bob)
    bob.pu()
    bob.left(36)
    bob.forward(56)
    bob.pd()

