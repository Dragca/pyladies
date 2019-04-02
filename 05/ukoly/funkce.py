CISLA = '1234567890'
HLASKA_DNY = '''Ale podle zadaneho cisla vychazi den narozeni na {}.den v mesici,
zadane cislo nemuze byt rodne cislo.'''


def delitelne(rodne_cislo_bez_lomitka):
    return int(rodne_cislo_bez_lomitka) % 11 == 0
def je_to_cislo(string):
    for cislo in string:
        if cislo not in CISLA:
            print('Neni to cislo')
            return False
            exit()
    return True
#def je_to_cislo(string):
#    for cislo in string:
#        if cislo not in CISLA:
#            return False
#    else:
 #       return True

def spravny_format_RC(rodne_cislo, rodne_cislo_bez_lomitka):
    return len(rodne_cislo) == 11 and \
        rodne_cislo[6] == '/' and \
        je_to_cislo(rodne_cislo_bez_lomitka)
        
def urceni_pohlavi(rodne_cislo):
    mm = int(rodne_cislo[2:4])
    if mm > 50:
        return 'zena'
    else:
        return 'muz'


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
        print(HLASKA_MESICE) # pokud by cislo splnovalo pramatery RC a), b) a presto by to nebylo RC- mesic narozeni by vychazel vice nez 12
        exit()
    # vypocet roku
    if rr <= 53:
        rok = 2000 + rr
    else:
        rok = 1900 + rr

    return ('Drzitel rodneho cisla byl narozen dne {}.{}. roku {}.'.format(den, mesic, rok))

 


        
        
            

rodne_cislo = input('Zadej rodne cislo ve formatu: 6 cislic/4 cislice. ')
rodne_cislo_bez_lomitka = (rodne_cislo[0:6] + rodne_cislo[7:])


#print(urceni_data_narozeni(rodne_cislo))
#print('Drzitel tohoto rodneho cisla je {}.'.format(
 #   urceni_pohlavi(rodne_cislo)))

#print(je_to_cislo(rodne_cislo_bez_lomitka))
# print(delitelne(rodne_cislo_bez_lomitka))
print(spravny_format_RC(rodne_cislo, rodne_cislo_bez_lomitka))