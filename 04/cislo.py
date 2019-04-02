klic = input('Zadej cislo: ')

cisla = '1234567890'

for cislo in klic:
    if cislo not in cisla:
        print('toto neni kladne cele cislo')
        exit()

if int(klic) > 0:
    print('Spravne, muzeme pokracovat')
        
