#Program je hra "Oko bere"

 #   Pocitac v kazdem kole vypise kolik mas bodu, a zeptá se te, jestli chces pokracovat.
 #   Pokud odpovis „ne“, hra konci.
 #   Pokud odpovís „ano“, pocítač „otocí kartu“ (náhodně vybere číslo od 2 do 10), vypíše její hodnotu a přičte ji k bodům.
 #   Pokud máš víc než 21 bodů, prohráváš.
 #   Cílem hry je získat co nejvíc bodů, ideálně 21.
from random import randrange
print('''Vitam te, pojd si zahrat "Oko bere"
abys vyhral, musis ziskat 21 bodu
pokud budes mit vic nez 21 bodu, prohravas. ''')
skore = 0

while True:
    print('mas',skore, 'bodu.')
    odpoved_hrace = input('Chces hrat? Zadej "ano" nebo "ne". ')
    if odpoved_hrace == 'ne':
        print('Konec hry')
        break
    elif odpoved_hrace == 'ano':
        karta = randrange(2,11)
        print('tvoje karta je:', karta)
        skore = skore + karta
        if skore == 21:
            print('Vyhral jsi!')
            exit()
        elif skore >=22:
            print('Prohral jsi')
            exit()

    else:
        print('Nerozumim')


