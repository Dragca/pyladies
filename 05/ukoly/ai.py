from random import randrange
from utils import tah

def tah_pocitace(herni_pole, symbol_pocitace, symbol_hrace):
    """
    Funkce dostane retezec s hernim polem, symbol pocitace, symbol hrace, vybere pozici, na kterou hrat.
    Vrati herni pole se zaznamenanym tahem pocitace.
    """
    if '-' not in herni_pole:
        raise ValueError('herni pole je plne')

    strategie = [
        # kdyz jsou vedle sebe 2 * symbol_pocitace a vedle nich volno, nebo volno mezi nimi- tah pocitace na toto volne policko
        ('-' + 2 * symbol_pocitace), (2 * symbol_pocitace + '-'), (symbol_pocitace + '-' + symbol_pocitace),
        # kdyz symbol_hrace/-/symbol_hrace, tah PC na pole uprostred
        (symbol_hrace + '-' + symbol_hrace),
        # kdyz je volne policko pred nebo za 2 * symbol_hrace, tah PC vedle nich na toto volne misto
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
