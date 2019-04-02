from random import randrange
cislo = randrange(3)

tah_cloveka = input('kámen, nůžky, nebo papír?')
tah_pocitace = ['kámen', 'nůžky', 'papír'][cislo]
print(tah_cloveka)
print(tah_pocitace)