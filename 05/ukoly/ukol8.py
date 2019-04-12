# simulace hry:
# hazi 1.hrac kostkou dokud mu nepadne sestka, pak hazi dalsi hrac dokud nepadne sestka i jemu, pak treti a pak ctvrty hrac.
# vyhrava ten kdo na hozeni sestky potreboval nejvice hodu.(v pripade shody vyhraje ten kdo hazel driv.)
# program by mel vypisovat vsechny hody a nakonec napsat kdo vyhral.

from random import randint
hraci = ('hrac_1', 'hrac_2', 'hrac_3', 'hrac_4')

def hod():
    """ 
    Funkce vraci nahodne hodonoty 1 az 6, coz simuluje hod kostkou
    """
    return randint(1, 6)


def hrac_hraje():
    """
    Funkce generuje hodnoty jednotlivych hodu a uklada je do seznamu vysledku.
    Vraci seznam vysedku hrace.
    """
    vysledky_hrace = []
    while True:
        vysledky_hrace.append(hod())
        if vysledky_hrace[-1] == 6:
            break
    return vysledky_hrace


def dej_pocet_bodu(ntice):
    return ntice[0]


def hraj():
    """
    Funkce spustí postupne hru pro kazdeho definovane hrace. Vypise hody hracu.
    Vraci kdo vyhral.
    """
    pocet_hodu = []

    for hrac in hraci:
        vysledky = hrac_hraje()
        print(vysledky)
        pocet_hodu.append((len(vysledky), hrac))
    pocet_hodu.sort(reverse=True, key=dej_pocet_bodu)
    print(pocet_hodu)
    print('Vyhral {}.'.format(pocet_hodu[0][1]))

    
        



hraj()
