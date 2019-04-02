# Tento program se uzivatele zepta na rodne cislo a vypise, zda jej zadal spravne

CISLA = '1234567890'
HLASKA_UVOD = '''Tento program kontroluje spravnost rodneho cisla
 a vypise udaje, ktere jsou v rodnem cisle obsazeny,
 tj. datum narozeni a pohlavi.'''
# pokud by cislo splnovalo pramatery RC a), b) a presto by to nebylo RC- mesic narozeni by vychazel vice nez 12
HLASKA_MESICE = '''Ale podle zadaneho cisla vychazi mesic narozeni vyssi nez 12, 
zadane cislo nemuze byt rodne cislo.'''
HLASKA_DNY = '''Ale podle zadaneho cisla vychazi den narozeni na {}.den v mesici,
zadane cislo nemuze byt rodne cislo.'''

# funkce pro zjisteni, ze je cislo pouze z cislic
def je_to_cislo(string):
    for cislo in string:
        if cislo not in CISLA:
            return False
    return True

# a) funkce pro spravny format, zjisti, ze je 6 cislic, lomitko, 4 cislice
def spravny_format_RC(rodne_cislo, rodne_cislo_bez_lomitka):
    return len(rodne_cislo) == 11 and \
        rodne_cislo[6] == '/' and \
        je_to_cislo(rodne_cislo_bez_lomitka)

# b) funkce pro delitelnost 11:
def delitelne_11(string):
    return int(string) % 11 == 0

# funke pro vypocet data narozeni
def urceni_data_narozeni(rodne_cislo):
    rr = int(rodne_cislo[0:2]) 
    mm = int(rodne_cislo[2:4])
    den = int(rodne_cislo[4:6])
    # pokud by cislo splnovalo pramatery RC a), b) a presto by to nebylo RC- den narozeni by vychazel vice nez 31
    if den > 31:
        print(HLASKA_DNY.format(den))
        exit()
    # vypocet mesice
    if 51 <= mm <= 62:
        mesic = mm - 50
    elif 1 <= mm <= 12:
        mesic = mm
    else:
        print(HLASKA_MESICE) 
        exit()
    # vypocet roku
    if rr <= 53:
        rok = 2000 + rr
    else:
        rok = 1900 + rr

    return (den, mesic, rok)
    

# d) funkce pro urceni pohlavi
def urceni_pohlavi(rodne_cislo):
    mm = int(rodne_cislo[2:4])
    if mm > 50:
        return 'zena'
    else:
        return 'muz'


print(HLASKA_UVOD)

rodne_cislo = input('Zadej rodne cislo ve formatu: 6 cislic/4 cislice. ')
rodne_cislo_bez_lomitka = (rodne_cislo[0:6] + rodne_cislo[7:])

if spravny_format_RC(rodne_cislo, rodne_cislo_bez_lomitka):
    print('Zadane cislo je ve formatu rodneho cisla.')
else:
    print('Toto neni rodne cislo.')
    exit()

if delitelne_11(rodne_cislo_bez_lomitka):
    print('Zadane cislo je delitelne 11.')
else:
    print('Cislo neni delitelne 11, neni to RC.')
    exit()

den, mesic, rok = urceni_data_narozeni(rodne_cislo)
print('Drzitel rodneho cisla byl narozen dne {}.{}. roku {}.'.format(den, mesic, rok))

print('Drzitel tohoto rodneho cisla je {}.'.format(urceni_pohlavi(rodne_cislo)))
