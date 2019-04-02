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

print(tah_cloveka)  # vypíše tahy člověka a počítače 
print(tah_pocitace)

vyhravas = (tah_cloveka == 'kámen' and tah_pocitace == 'nůžky' or  # promenna vyhravas 
    tah_cloveka == 'nůžky' and tah_pocitace == 'papír' or
    tah_cloveka == 'papír' and tah_pocitace == 'kámen')



if not tah_cloveka in moznosti:  # pokud uživatel zadá nesprávnou možnost, 
    print('Nerozumím.')         # program vypíše "nerozumím" a ukončí se.
    exit()
elif tah_cloveka == tah_pocitace:
    print('Plichta.')
elif vyhravas:
    print('Vyhrál jsi!')
else:
    print('Počítač vyhrál.')    


