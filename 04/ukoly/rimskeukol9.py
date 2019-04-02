# Program prevede rimske cislice na cislo (int).
print('Tento program prevede rimske cislo na ciselnou hodnotu.')

# trojice : rimska cislice, hodnota, maximalni mozny pocet opakovani
rimske_cislice = {'M' : 1000, 'D' : 500, 'C' : 100, 'L' : 50, 'X' : 10, 'V' : 5, 'I' : 1}
hodnota = 0

# M, C, X, I se muzou vyskytnout maxialne 3x v kladne hodnote- napravo 
# a C, X, I - maximalne 1x vlevo v zaporne hodnote

rimske_cislo = input('Zadej cislo v rimskych cislovkach: ')
# pokud nic nezada, exit
if len(rimske_cislo) == 0:
    print('Nic jsi nezadal, nemuzu slouzit.')
    exit()
# cyklem prochazi jednotlive cislice, pokud nejde o rim cislo- exit
for i in rimske_cislo:
    if i not in rimske_cislice:
        print('Toto neni rimska cislice')
        exit()
        # pomoci enumerate() se priradi ke kazde iteraci hodnota klice pro danou rimskou cislici
for i, c in enumerate(rimske_cislo):
    # jestlize jde o posledni iteraci (iterace je 0,1,2-porovnavam s delkou retezce 3.)
    if (i + 1) == len(rimske_cislo) or rimske_cislice[c] >= rimske_cislice[rimske_cislo[i + 1]]:
        hodnota = hodnota + rimske_cislice[c]
    else:
        hodnota = hodnota - rimske_cislice[c]

print(hodnota)