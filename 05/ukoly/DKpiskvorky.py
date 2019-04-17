# 1D piskvorky bez strategie

from random import randrange

HLASKA_UVOD = 'Pojd si zahrat 1D piskvorky! Hrajeme na radku s dvaceti policky. '
KDO_VYHRAL = {
    'x': 'Vyhral hrac se znakem x.',
    'o': 'Vyhral hrac se znakem o.',
    '!': 'Remiza!'}


def vyhodnot(herni_pole):
    """
    Funkce dostane retezec s hernim polem 1-D piskvorek.
    Vrati jednoznakovy retezec podle stavu hry.
    """
    if 'xxx' in herni_pole:  # vyhral hrac s x
        return 'x' 
    elif 'ooo' in herni_pole:  # vyhral hrac s o
        return 'o'
    elif '-' not in herni_pole:  # remiza
        return '!'
    else:
        return '-'  # hra jeste neskoncila


def tah(herni_pole, cislo_policka, symbol):
    """
    Funkce dostane retezec s hernim polem, cislo policka (0-19), symbol (x nebo o).
    Vrati herni pole (tj retezec) s danym symbolem umistenym na danou pozici.
    """
    pole = list(herni_pole)  # prevedeni retezce herni pole na seznam
    pole[cislo_policka] = symbol  # zapis symbolu 
    return ''.join(pole) 


def tah_hrace(herni_pole, symbol_pocitace, symbol_hrace):
    """
    Funkce dostane retezec s hernim polem, symbol, pocitace, symbol hrace, zepta se hrace, na kterou pozici chce hrat.
    Funkce odmitne zaporna a prilis velka cisla(mimo rozsah pole) a tah na obsazena policka.
    Vrati herni pole se zaznamenanym tahem hrace.
    """
    
    while True:
        pozice_string = input('Zadej ciselnou pozici tveho tahu (0-{}) '.format(len(herni_pole) - 1))
        if not pozice_string.isdecimal():  # overeni, ze zadane cislo pozice je cislice
            print('Nezadal jsi cislici.')
            continue

        pozice = int(pozice_string)
        if pozice < 0:
            print('Zadej kladne cislo')
        elif pozice > len(herni_pole) - 1:
            print('Hrajes mimo herni pole, to ma jenom {} pozic!'.format(len(herni_pole)))
        elif herni_pole[pozice] != '-':
            print('Hrajes na obsazene policko. ')
        else:
            break

    return tah(herni_pole, pozice, symbol_hrace)


def tah_pocitace(herni_pole, symbol_pocitace, symbol_hrace):
    """
    Funkce dostane retezec s hernim polem, symbol pocitace, symbol hrace, vybere pozici, na kterou hrat.
    Vrati herni pole se zaznamenanym tahem pocitace.
    """
    strategie = [
        # když jsou vedle sebe 2 * symbol_pocitace a vedle nich volno, nebo volno mezi nimi- tah pocitace na toto volne policko
        ('-' + 2 * symbol_pocitace), (2 * symbol_pocitace + '-'), (symbol_pocitace + '-' + symbol_pocitace),
        # když symbol_hrace/-/symbol_hrace, tah PC na pole uprostřed
        (symbol_hrace + '-' + symbol_hrace),
        # když je volne policko pred nebo za 2 * symbol_hrace, tah PC vedle nich na toto volne misto
        ('-' + 2 * symbol_hrace), (2 * symbol_hrace + '-'),
        # kdyz jsou kolem symbolu_hrace volne pozice, tah hrace na volnou pozici vlevo
        ('-' + symbol_hrace + '-'),
        # kdyz /-/symbol_pocitace/-/, nebo /-/-/symbol_PC nebo  symbol_PC/-/-/ hrat na volen policko
        ('-' + symbol_pocitace + '-'), ('--' + symbol_pocitace), (symbol_pocitace + '--')]

    for kombinace in strategie:
        nasel_na_pozici = herni_pole.find(kombinace)
        if nasel_na_pozici != -1:
            pozice = nasel_na_pozici + kombinace.find('-')
            break

    # jinak nahodna pozice 
    if nasel_na_pozici == -1:
        while True:
            pozice = randrange(len(herni_pole))
            if herni_pole[pozice] == '-':
                break
    
    return tah(herni_pole, pozice, symbol_pocitace)


def piskvorky1D():
    """
    Funkce vytvori retezec s hernim polem a stridave vola funkce tah_hrace a tah_pocitace.
    Po kazdem tahu se vyhodnoti stav hry.
    """
    print(HLASKA_UVOD)
    
    symbol_hrace = input('Vyber si a zadej svuj herni symbol, "x" nebo "o"?: ')  # vyber herniho symbolu hrace
    while symbol_hrace not in ('x', 'o'):
        symbol_hrace = input('Spatne, zadej znovu, "x" nebo "o"?: ')
    
    if symbol_hrace == 'x':  # nastaveni herniho symbolu pocitace
        symbol_pocitace = 'o'
    else:
        symbol_pocitace = 'x'

    herni_pole = 20 * '-'
    print(herni_pole)
        
    kolo = 1
    while True:
        for tahne in (tah_hrace, tah_pocitace):
            herni_pole = tahne(herni_pole, symbol_pocitace, symbol_hrace)
            print('{}. kolo: {}'.format(kolo, herni_pole))
            stav = vyhodnot(herni_pole)  # promenna, kde je ulozeno aktualni vyhodnoceni herniho pole
            if stav in KDO_VYHRAL:
                print(KDO_VYHRAL[stav])
                return
            kolo += 1


piskvorky1D()
