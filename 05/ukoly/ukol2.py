from turtle import forward, right, left, penup, pendown, exitonclick
from math import sqrt
x = 25

def domecek(x):
    for _ in range(4):
        forward(x)
        left(90)
    left(45)
    forward(sqrt(2)*x)
    left(90)
    for _ in range(2):
        forward(sqrt(2)*x/2)
        left(90)
    forward(sqrt(2)*x)
    left(45)
    forward(x)

for _ in range(3):
    domecek(x)
    x = 2 * x

exitonclick()