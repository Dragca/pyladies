# funkce ano_ne, tak, aby se dalo pouzit "ano" i "a",
# "ne" i "n", aby se nebral ohled na velikost pismen  a mezery pred/za odpovedi.

def ano_nebo_ne(otazka):
    # vrati True nebo False, podle odpovedi uzivatele.
    while True:
        odpoved = input(otazka).lower().strip()
        if odpoved in ('ano', 'a'):
            return True
        elif odpoved in ('ne', 'n'):
            return False
        else:
            print('Nerozumim! Odpovez "ano" nebo "ne".')

if ano_nebo_ne('Chces si zahrat hru?'):
    print('OK! Ale napred si ji musis naprogramovat.')
else:
    print('Skoda.')
