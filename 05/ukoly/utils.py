
def tah(herni_pole, cislo_policka, symbol):
    """
    Funkce dostane retezec s hernim polem, cislo policka (0-19), symbol (x nebo o).
    Vrati herni pole (tj retezec) s danym symbolem umistenym na danou pozici.
    """
    pole = list(herni_pole)  # prevedeni retezce herni pole na seznam
    pole[cislo_policka] = symbol  # zapis symbolu 
    return ''.join(pole) 
