from turtle import Turtle

N = 5

turtles = []

for i in range(N):
    turtle = Turtle()
    turtle._rotate(i/N*360)
    turtles.append(turtle)

for _ in range(50):
    for turtle in turtles:
        turtle.forward(10)
