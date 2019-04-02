from turtle import forward, left, exitonclick, setpos, up, down

up()
setpos(-250, -250)
down()

for i in range (60):
    for j in range(4):
        forward(i*2)
        left(90)
    left (10)
exitonclick()


