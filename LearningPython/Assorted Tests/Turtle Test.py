import turtle
import random

turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()
sp = 0
turtle1.speed(sp)
turtle2.speed(sp)

turtle1.color('red')
turtle2.color('blue')

while True:
    d1 = random.randint(0, 359);
    if d1 <= 179:
        turtle1.left(d1)
    else:
        turtle1.right(360 - d1)

    d1 = random.randint(0, 359);
    if d1 <= 179:
        turtle2.left(d1)
    else:
        turtle2.right(360 - d1)

    turtle1.forward(random.randint(1, 20));
    turtle2.forward(random.randint(1, 20));


