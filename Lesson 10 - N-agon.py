import turtle
import math

n = int(input("How many sides should the shape have?\n"))
radius = float(input("What should the radius be?\n"))
turtle.radians()

turtle.pu()
turtle.goto(0,radius)
turtle.right(math.pi/n)
turtle.pd()

for i in range(n):
    turtle.forward(math.sin(math.pi/n)*radius*2)
    turtle.right(math.pi/n*2)