# aby 'kamen, nuzky, papir' opakoval hru, dokud uzivatel nezadá 'konec'

from random import choice

MOZNOSTI = ['kamen', 'nuzky', 'papir']
HLASKA_UVOD = ''''Pojd si zahrat "kamen, nuzky, papir", treba se ti podari nad pocitacem vyhrat!
Az budes chtit skoncit, napis konec'''


print(HLASKA_UVOD)

while True:
    tah_pocitace = choice(MOZNOSTI) 
    tah_cloveka_vstup = input('kamen, nuzky nebo papir? ')
    tah_cloveka = tah_cloveka_vstup.lower().strip()
    while tah_cloveka not in MOZNOSTI:
        if tah_cloveka == 'konec':
            print('jak si prejes, konec hry')
            exit()
        print('Spatne, zadej znovu.')
        tah_cloveka = input('kamen, nuzky nebo papir? ')
    print('tvuj tah: {}, tah pocitace: {}.'.format(tah_cloveka, tah_pocitace))

    vyhravas = (tah_cloveka == 'kamen' and tah_pocitace == 'nuzky' or  # promenna vyhravas 
        tah_cloveka == 'nuzky' and tah_pocitace == 'papir' or
        tah_cloveka == 'papir' and tah_pocitace == 'kamen')

    if tah_cloveka == tah_pocitace:
        print('Plichta.')
    elif vyhravas:
        print('Vyhral jsi!')
    else:
        print('Pocitac vyhral.')    

