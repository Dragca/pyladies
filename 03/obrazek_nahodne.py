#program vykresli dav smajliku, pozice jsou náhodné, bude kreslit, dokud ti nedojde baterka

from turtle import forward, back, right, left, setpos, up, down, circle, exitonclick, color, pencolor, fillcolor, pensize, begin_fill, end_fill, speed
from random import randrange

speed = 0

def oko(): # vykresleni oka
    down()
    fillcolor('black')
    begin_fill()
    circle(6) 
    end_fill()
    up()


while True:
    x = randrange(-450, 450, 10)
    y = randrange(-400, 400, 10)
    up()
    setpos(x, y)
    down()  
    pensize(2)
    pencolor("black")
    fillcolor("yellow")
    begin_fill()
    circle(50) #oblicej
    end_fill()
    up()
    circle(50, 180)
    right(45)
    down()
    for n in range(4): #vlasy
        forward(30)
        back(30)
        right(30)
    up() 
    right(105) #otočení želvy směrem od vrcholu hlavy k obličeji
    forward(30) # posun na leve oko
    right(90)
    forward(20)
    oko() # vykresleni leveho oka
    back(40) #přesun na prave oko
    oko() #vykresleni praveho oka
    forward(20) # navrat do poloviny obličeje a posun ke kresbe usmevu
    left(90)
    forward(55)
    left(90)
    down()
    pensize(5)
    pencolor('red')
    circle(30,90) #vykresleni prave poloviny ust
    up()
    for _ in range(2): #navrat do poloviny ust
        left (90)
        forward(30)
    right(90)
    down()              # vykresleni leve poloviny ust
    circle(-30,90)
    up()
    for _ in range(2): #navrat do poloviny usmevu
        right(90)
        forward(30)
    up()
    forward(15)
    left(90)          
    
exitonclick()