from turtle import forward, left, right, exitonclick, speed

speed(0)

for i in range(4000):  # 8, 16, 4
    forward(0.001 * i)
    left(1.8)

exitonclick()
