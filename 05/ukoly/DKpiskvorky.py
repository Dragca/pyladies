# 1D piskvorky bez strategie

from random import randrange

HLASKA_UVOD = 'Pojd si zahrat 1D piskvorky! Hrajeme na radku s dvaceti policky. '

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

def konej_podle_stavu(stav_herniho_pole):
    """
    Funkce dostane jednoradkovy retezec o aktualnim stavu herniho pole.
    Podle podminek vytiskne hlasku.
    Vraci False pokud hra konci, jinak True
    """
    if stav_herniho_pole == 'x':
        print('Vyhral hrac se znakem x')
        return False 
    elif stav_herniho_pole == 'o':
        print('Vyhral hrac se znakem o')
        return False 
    elif stav_herniho_pole == '!':
        print('Remiza!')
        return False
    else:
        return True

def tah(herni_pole, cislo_policka, symbol):
    """
    Funkce dostane retezec s hernim polem, cislo policka (0-19), symbol (x nebo o).
    Vrati herni pole (tj retezec) s danym symbolem umistenym na danou pozici.
    """
    pole = list(herni_pole)  # prevedeni retezce herni pole na seznam
    pole[cislo_policka] = symbol  # zapis symbolu 
    return ''.join(pole) 


def tah_hrace(herni_pole, symbol_hrace):
    """
    Funkce dostane retezec s hernim polem, symbol hrace, zepta se hrace, na kterou pozici chce hrat.
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
            print('Hrajes na obsazene policko, ')
        else:
            break

    return tah(herni_pole, pozice, symbol_hrace)


def tah_pocitace(herni_pole, symbol_pocitace):
    """
    Funkce dostane retezec s hernim polem, symbol pocitace, vybere pozici, na kterou hrat.
    Vrati herni pole se zaznamenanym tahem pocitace.
    """
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
        for tahne, symbol in ((tah_hrace, symbol_hrace),(tah_pocitace, symbol_pocitace)):
            herni_pole = tahne(herni_pole, symbol)
            print('{}. kolo: {}'.format(kolo, herni_pole))
            stav = vyhodnot(herni_pole)  # promenna, kde je ulozeno aktualni vyhodnoceni herniho pole
            if not konej_podle_stavu(stav):
                return
            kolo += 1


piskvorky1D()
