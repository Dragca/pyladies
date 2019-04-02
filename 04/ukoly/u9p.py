# Program prevede rimske cislice na cislo (int).
print('Tento program prevede rimske cislo na ciselnou hodnotu.')

# trojice : rimska cislice, hodnota, maximalni mozny pocet opakovani
rimske_cislice = {'M' : 1000, 'D' : 500, 'C' : 100, 'L' : 50, 'X' : 10, 'V' : 5, 'I' : 1}
hodnota = 0
# M, C, X, I se muzou vyskytnout maxialne 3x v kladne hodnote- napravo 
# a C, X, I - maximalne 1x vlevo v zaporne hodnote

rimske_cislo = input('Zadej cislo v rimskych cislovkach: ')
hodnota_list = []
if len(rimske_cislo) == 0:
    print('Nic jsi nezadal, nemuzu slouzit.')
    exit()
for i in rimske_cislo:
    if i not in rimske_cislice:
        print('Toto neni rimske cislo.')
        exit()
    else:
        hodnota_list.append(rimske_cislice[i])

print(hodnota_list)

for i in range(len(hodnota_list) - 1):
    if hodnota_list[i] < hodnota_list[i + 1]:
        hodnota_list[i] = - hodnota_list[i]

print(hodnota_list)
hodnota = sum(hodnota_list)
print(hodnota)