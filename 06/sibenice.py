from random import choice

from sibenice_obrazky import seznam_obrazku 


seznam_slov = ['lev', 'pes', 'kanec', 'prase', 'lemur']
JESTLI_VYHRAL = {
    'vyhral': 'Vyhral jsi! Gratuluji!',
    'prohral': 'Prohral jsi. Konec hry.'}


def zadej_pismeno():
    """
    funkce vraci vstup uzivatele - znak.
    """
    vstup = input('Zadej pismeno: ').lower()
    
    if len(vstup) == 0 or len(vstup) > 1:
        raise ValueError
    
    return vstup


def najdi_ve_slove(slovo, znak):
    """
    Funkce ma parametry slovo a znak.
    Vraci -1 pokud znak neni ve slove, jinak vraci pozici znaku.

    """
    return slovo.find(znak)

def zapis_pismeno(pole_slova, pozice, znak):
    """
    Funkce dostane retezec s polem slova, pozici znaku a znak.
    Vrati pole slova (tj retezec) se znakem umistenym na danou pozici.
    """
    return pole_slova[:pozice] + znak + pole_slova[pozice + 1:]
    
    
def vyhodnot(pole_slova, neuspesnych_pokusu):
    """
    Funkce dostane jako parametry pole slova a pocet neuspesnych pokusu.
    Vrati jednoznakovy retezec.
    """
    if '-' not in pole_slova and neuspesnych_pokusu < 10:
        return 'vyhral'
    elif neuspesnych_pokusu >= 10:
        return 'prohral'
    else:
        return '-' # hra pokracuje

 
def hra_sibenice():
    """
    Funkce je samotna hra 'sibenice'.
    """
    slovo = choice(seznam_slov)
    pole_slova = '-' * len(slovo)
    print(pole_slova) 
    neuspesnych_pokusu = 0
    while True:
        try:
            znak = zadej_pismeno()
        except ValueError:
            print('Musis zadat jedno pismeno.')
            continue
        nasel_na_pozici = najdi_ve_slove(slovo, znak)
        if nasel_na_pozici != -1:
            pole_slova = zapis_pismeno(pole_slova, nasel_na_pozici, znak)
        else:
            neuspesnych_pokusu += 1
    
        print("""neuspesnych pokusu: {}\n{}\n{}""".format(
            neuspesnych_pokusu, seznam_obrazku[neuspesnych_pokusu], pole_slova))
        
        stav = vyhodnot(pole_slova, neuspesnych_pokusu)
        if stav == '-':
            continue
        else:
            print(JESTLI_VYHRAL[stav])
            return


if __name__ == "__main__":
    hra_sibenice()