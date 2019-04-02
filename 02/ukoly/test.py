# Tento program je hra kámen, nůžky, papír. Uživatel zadá svůj tah, tah počítače je náhodně zvolen.
# Pro zvolení náhodného tahu počítače by šla ještě použít funkce choice
# z modulu random která vybírá náhodný prvek ze seznamu. Kód pro tah počítače by tak vypadal:
# from random import choicet
# moznosti = ['kámen', 'nůžky', 'papír']
# tah_pocitace = choice(moznosti) 

from random import randrange
cislo = randrange(3) #  náhodně zvolí číslo 0-2, 
                    #  tato proměnná bude určovat pozici prvku v seznamu možností tahu počítače

print('Pojď si zahrát "kámen, nůžky, papír", třeba se ti podaří nad počítačem vyhrát!')
tah_cloveka = input('kámen, nůžky nebo papír? ')
moznosti = ['kámen', 'nůžky', 'papír']
tah_pocitace = moznosti[cislo]

print(tah_cloveka)
print(tah_pocitace)


#if tah_cloveka == 'kámen':
 #  vyhrava = tah_pocitace == 'nůžky'
#elif tah_cloveka == 'nůžky':
#    vyhrava = tah_pocitace == 'papír'
#elif tah_cloveka == 'papír':
 #   vyhrava = tah_pocitace == 'kámen'
#else:
#    print('Nerozumím')
#    exit()

vyhravas = (tah_pocitace == 'kámen' and tah_cloveka == 'papír' 
or tah_pocitace == 'nůžky' and tah_cloveka == 'kámen'
or tah_pocitace == 'papír' and tah_cloveka == 'nůžky')

if not tah_cloveka in ('kámen', 'nůžky', 'papír'):
    print('Nerozumím')
    exit()
if tah_cloveka == tah_pocitace:
    print('Plichta.')
elif vyhravas:
    print('Vyhrál jsi!')
else:
    print('Počítač vyhrál.')    



