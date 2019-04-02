# program se uzivatele zepta na rodne cislo a vypise, zda jej zadal spravne

print('''Tento program kontroluje spravnost rodneho cisla
 a vypise udaje, ktere jsou v rodnem cisle obsazeny,
 tj. datum narozeni a pohlavi.''')
rodne_cislo = input('Zadej rodne cislo ve formatu: 6 cislic/4 cislice. ')
rodne_cislo_bez_lomitka = (rodne_cislo[0:6] + rodne_cislo[7:])

# a) kontrola, zda jde o spravny format rodneho cisla : 6 cislic, lomitko, 4 cislice?
spravne = (len(rodne_cislo) == 11 and rodne_cislo[6] == '/' and
        rodne_cislo_bez_lomitka.isdecimal())

# b) kontrola, zda je dělitelne 11
if spravne:
    delitelne = int(rodne_cislo_bez_lomitka) % 11 == 0

if spravne and delitelne:
    print('Zadane cislo je ve spravnem formatu rodneho cisla.')
else:
    print('Zadane cislo neni ve formatu rodneho cisla.')
    exit()

# c) urceni, jake datum narozeni je v cisle zakodovano (tzn. den, mesic, rok )

# ziskani jednotlivych udaju data z rodneho cisla
rr = int(rodne_cislo_bez_lomitka[0:2]) 
mm = int(rodne_cislo_bez_lomitka[2:4])
den = int(rodne_cislo_bez_lomitka[4:6])
# pokud by cislo splnovalo pramatery RC a), b) a presto by to nebylo RC- den narozeni by vychazel vice nez 31
if den > 31:
    print('''Ale podle zadaneho cisla vychazi den narozeni na {}.den v mesici,
zadane cislo nemuze byt rodne cislo.'''.format(den))
    exit()
# vypocet mesice
if 51 <= mm <= 62:
    mesic = mm - 50
elif 1 <= mm <= 12:
    mesic = mm
else:
    print('''Ale podle zadaneho cisla vychazi mesic narozeni vyssi nez 12, 
zadane cislo nemuze byt rodne cislo.''') # pokud by cislo splnovalo pramatery RC a), b) a presto by to nebylo RC- mesic narozeni by vychazel vice nez 12
    exit()
# vypocet roku
if rr <= 53:
    rok = 2000 + rr
else:
    rok = 1900 + rr

print('Drzitel rodneho cisla byl narozen dne {}.{}. roku {}.'.format(den, mesic, rok))

# d) urceni, jake pohlavi je v cisle zakodovano (vypise 'muz'/'zena)
if mm > 50:
    pohlavi = 'zena'
else:
    pohlavi = 'muz'
print('Drzitel tohoto rodneho cisla je {}.'.format(pohlavi))
