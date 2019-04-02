#tento program vypočítá obvod a obsah kruhu

from math import pi

polomer = float(input('Zadej poloměr kruhu'))
polomer_je_kladny = polomer > 0

if polomer_je_kladny:
    print('Obvod kruhu o polomeru', polomer, ' cm je', 2* pi * polomer, 'cm')
    print('Obsah kruhu o polomeru', polomer, 'cm je', pi * polomer ** 2, 'cm2')
else:
    print('Poloměr nemůže být záporný')