import turtle
import numpy as np

ratio = 15/20
# ratio = 1/2
# ratio = 2/1
# ratio = 3/2
# ratio = 1/1
# # ratio = 5/4

turtle.speed(0)
turtle.bgcolor('black')
turtle.pencolor('white')
turtle.pensize(3)
turtle.penup()

cx = 0
cy = np.pi/2

dx = 0.06
dy = dx * ratio

m = 200
dm = 0.08
while True:
    x = np.cos(cx) * m
    y = np.cos(cy) * m

    turtle.goto(x, y)

    cx += dx
    cy += dy
    m -= dm
    turtle.pendown()

    if m < dm:
        break

turtle.done()