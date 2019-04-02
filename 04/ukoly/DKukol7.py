# tyto programy maji na vstupu retezec s rodnym cislem a zanalyzuji ho:
# a) zda je ve spravnem formatu : 6 cislic, lomitko, 4 cislice? - vypise True/ False
# b) zda je dělitelne 11 - vypise True/False
# c) jake datum narozeni je v cisle zakodovano? (vypise trojici cisel - den, mesic, rok )
# d) jake pohlavi je v cisle zakodovano? (vypise 'muz'/'zena)

rodne_cislo = '736028/5163'
rodne_cislo_bez_lomitka = (rodne_cislo[0:6] + rodne_cislo[7:])

# a) kontrola, zda jde o spravny format rodneho cisla : 6 cislic, lomitko, 4 cislice

spravne = (len(rodne_cislo) == 11 and rodne_cislo[6] == '/' and
        rodne_cislo_bez_lomitka.isdecimal())
print(spravne)

# b) kontrola, zda je dělitelne 11 
delitelne = int(rodne_cislo_bez_lomitka) % 11 == 0
print(delitelne)

# c) urceni, jake datum narozeni je v cisle zakodovano (tzn. den, mesic, rok )
# ziskani jednotlivych udaju data z rodneho cisla
rr = int(rodne_cislo_bez_lomitka[0:2]) 
mm = int(rodne_cislo_bez_lomitka[2:4])
den = int(rodne_cislo_bez_lomitka[4:6])

# pokud by cislo splnovalo pramatery RC a), b) a presto by to nebylo RC- den narozeni by vychazel vice nez 31
if den > 31:
    print('V mesici je maximalne 31 dni, zadane cislo nemuze byt rodne cislo. ')
    exit()
# vypocet mesice
if 51 <= mm <= 62:
    mesic = mm - 50
elif 1 <= mm <= 12:
    mesic = mm
else:
    print('je jen 12 mesicu, zadane cislo nemuze byt rodne cislo.') # pokud by cislo splnovalo pramatery RC a), b) a presto by to nebylo RC- mesic narozeni by vychazel vice nez 12
    exit()
# vypocet roku
if rr <= 53:
    rok = 2000 + rr
else:
    rok = 1900 + rr

print('{},{},{}'.format(den, mesic, rok))

# d) urceni, jake pohlavi je v cisle zakodovano (vypise 'muz'/'zena)
if mm > 50:
    print('zena')
else:
    print('muz')