from random import randrange
cislo = randrange(3)

tah_cloveka = input('kámen, nůžky, nebo papír?')
moznosti = ['kámen', 'nůžky', 'papír']
tah_pocitace = moznosti[cislo]
print(tah_cloveka)
print(tah_pocitace)

if tah_cloveka == 'kámen':
    if tah_pocitace == 'kámen':
        print('Plichta.')
    elif tah_pocitace == 'nůžky':
        print('Vyhrál jsi!')
    elif tah_pocitace == 'papír':
        print('Počítač vyhrál.')
elif tah_cloveka == 'nůžky':
    if tah_pocitace == 'kámen':
        print('Počítač vyhrál')
    elif tah_pocitace == 'nůžky':
        print('Plichta.')
    elif tah_pocitace == 'papír':
        print('Vyhrál jsi!')
elif tah_cloveka == 'papír':
    if tah_pocitace == 'kámen':
        print('Vyhrál jsi!')
    elif tah_pocitace == 'nůžky':
        print('Počítač vyhrál')
    elif tah_pocitace == 'papír':
        print('Plichta')
else:
    print('Nerozumím')