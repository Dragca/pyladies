#n-uhelnik

from turtle import forward, left, right, exitonclick, speed

pocet_uhlu = int(input('Zadej pocet uhlu tveho n-uhelniku'))

if pocet_uhlu <= 0:
    print('Zadej kladne cislo')
    exit()

delka_strany = 200/pocet_uhlu
vnitrni_uhel = 180 * (1 - 2/pocet_uhlu)
uhel_zelvy = 180 - vnitrni_uhel
speed(pocet_uhlu)

for _ in range(pocet_uhlu):
    forward(delka_strany)
    left(uhel_zelvy)

exitonclick()

