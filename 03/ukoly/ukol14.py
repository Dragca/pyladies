from turtle import forward, left, exitonclick, setpos, up, down

up()
setpos(80, 80)
down()

for j in range(18):
    for i in range(4):
        forward(50)
        left(90)
    left(20)

exitonclick()

