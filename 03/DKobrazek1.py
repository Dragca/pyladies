#program vykresli dav smajliku, 
from turtle import forward, back, right, left, setpos, up, down, circle, exitonclick, color, pencolor, fillcolor, pensize, begin_fill, end_fill, speed
from random import randrange
y = -400
speed = 0

def oko(): # funkce pro vykresleni oka
    down()
    fillcolor('black')
    begin_fill()
    circle(6) 
    end_fill()
    up()


for _ in range(7): # 7 rad obliceju nad sebou
    x = randrange(-450, -420, 10) # nahodný začátek každé řady z intervalu možných hodnot pro X
    up()
    setpos(x, y)
    down()

    for _ in range(9):
        vzdalenost = randrange(80, 150, 10) #nahodná vdálenost z intervalu pro vykresleni dalšího obličeje
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
        forward(vzdalenost)
        down()
    
    posun_y = randrange(105, 135, 5) # velikost posunu další řady je náhodná z intervalu hodnot
    y = y + posun_y

exitonclick()