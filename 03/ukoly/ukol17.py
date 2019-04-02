#tento program se uzivatele 5x zepta na cislo a nejmensi zadane cislo vypise
#porovna je podle velikosti a vypise cislo nejblizsi nule

seznam_cisel = [] #vytvoreny prazdny seznam

for i in range(5):
    cislo = int(input('Zadej cislo: '))
    seznam_cisel.append(cislo) # v kazdem cyklu prida zadane cislo do seznamu cisle

seznam_cisel.sort() # seradi vzestupne seznam cisle
print('Nejmensi cislo ze zadanych cisel je:', seznam_cisel[0])
