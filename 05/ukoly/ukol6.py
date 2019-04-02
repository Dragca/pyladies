# progra se zepta na prijmeni a zkusi podle nej uhodnout jeho/jeji pohlavi

def pohlavi_dle_prijmeni(prijmeni):
    male_bez_mezer = prijmeni.lower().strip()
    if male_bez_mezer[-3:] == 'ova':
        return 'zena'
    else:
        return 'muz'


vstup = input('Zadej sve prijmeni.')
print(pohlavi_dle_prijmeni(vstup))
