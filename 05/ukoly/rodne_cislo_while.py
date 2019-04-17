# Tento program se uzivatele zepta na rodne cislo a vypise, zda jej zadal spravne

HLASKA_UVOD = '''Tento program kontroluje spravnost rodneho cisla
 a vypise udaje, ktere jsou v rodnem cisle obsazeny,
 tj. datum narozeni a pohlavi.'''
# pokud by cislo splnovalo pramatery RC a), b) a presto by to nebylo RC- mesic narozeni by vychazel vice nez 12
HLASKA_MESICE = '''Ale podle zadaneho cisla vychazi mesic narozeni vyssi nez 12, 
zadane cislo nemuze byt rodne cislo.'''
HLASKA_DNY = '''Ale podle zadaneho cisla vychazi den narozeni na {}.den v mesici,
zadane cislo nemuze byt rodne cislo.'''


# a) funkce pro spravny format, zjisti, ze je 6 cislic, lomitko, 4 cislice
def spravny_format_RC(rodne_cislo, rodne_cislo_bez_lomitka):
    """
    funkce vyhazuje vyjimku ValueError, pokud neni RC ve spravnem formatu
    """
    if len(rodne_cislo) != 11 or \
        rodne_cislo[6] != '/':
        raise ValueError
    # funkce int overi, ze jde retezec prevest na cislo, tzn je z cislic
    # a vyhodi vyjimku, kdyz to neni cislo
    int(rodne_cislo_bez_lomitka)

# b) funkce pro delitelnost 11:
def delitelne_11(string):
    """
    Funkce vyhazuje vyjimku, pokud cislo neni delitelne 11
    """
    if int(string) % 11 != 0:
        raise ValueError

# funke pro vypocet data narozeni
def urceni_data_narozeni(rodne_cislo):
    rr = int(rodne_cislo[0:2]) 
    mm = int(rodne_cislo[2:4])
    den = int(rodne_cislo[4:6])
    # pokud by cislo splnovalo pramatery RC a), b) a presto by to nebylo RC- den narozeni by vychazel vice nez 31
    if den > 31:
        raise ValueError(HLASKA_DNY.format(den))
    # vypocet mesice
    if 51 <= mm <= 62:
        mesic = mm - 50
    elif 1 <= mm <= 12:
        mesic = mm
    else:
        raise ValueError(HLASKA_MESICE) 
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


while True:
    rodne_cislo = input('Zadej rodne cislo ve formatu: 6 cislic/4 cislice. ')

    rodne_cislo_bez_lomitka = (rodne_cislo[0:6] + rodne_cislo[7:])

    try:
        spravny_format_RC(rodne_cislo, rodne_cislo_bez_lomitka)
    except ValueError:
        print('Toto neni rodne cislo.')
        continue
    else:
        print('Zadane cislo je ve formatu rodneho cisla.')

    try:
        delitelne_11(rodne_cislo_bez_lomitka)
    except ValueError:
        print('Cislo neni delitelne 11, neni to RC.')
        continue
    else:
        print('Zadane cislo je delitelne 11.')

    try:
        den, mesic, rok = urceni_data_narozeni(rodne_cislo)
    except ValueError as vyjimka:
        print(vyjimka)
        continue
    break

print('Drzitel rodneho cisla byl narozen dne {}.{}. roku {}.'.format(den, mesic, rok))

print('Drzitel tohoto rodneho cisla je {}.'.format(urceni_pohlavi(rodne_cislo)))

