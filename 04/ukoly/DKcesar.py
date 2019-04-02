# Program 'Cesarova sifra'- program dokaze podle zadaneho klice zasifrovat text 
# psany bez diakritiky a slozeny ze znaku ASCII

print('''Vita te program "Cesarova sifra". Program dokaze podle zadaneho
klice (cislo, o kolik se zasifrovany znak posune v abecede) zasifrovat text
bez diakritiky.''')

# cyklus vyzve uzivatele, aby zadal klic, bude jej vyzyvat opakovane, dokud nezada spravny klic, tj. kladne cele cislo.
while True:
    klic = input('''Zadej tajne cislo, bude to klic, podle ktereho se bude text sifrovat.
Musi to byt kladne cele cislo. ''') 
    spravny_klic = klic.isdecimal() and int(klic) >= 0
    if spravny_klic == True:
        print('Klic jsi zadal spravne. Muzeme pokracovat.')
        break
    print('Tohle neni kladne cele cislo. Zkus to znovu. ')
# posun v abecede
posun = int(klic) 

# upozorneni, pokud bude klic 0 a nasobky 26, bude sifrovany text shodny s puvodnim
if posun % 26 == 0:
    print('''Upozornuji te, ze jsi zadal klic, podle ktereho je zasifrovany text shodny s puvodnim textem,
aby byl text opravdu zasifrovany, nesmis jako klic zvolit 0, 26 a jeji nasobky.''')

# nacteni textu, ktery chce uzivatel sifrovat
plaintext = input('Nyni zadej text, ktery chces zasifrovat. ')
ciphertext_list = []

# cyklus pro prevedeni znaku z plaintext na novy znak v ciphertext a ulozi do seznamu
for znak in plaintext:
    if 65 <= ord(znak) <= 90: # pro velka pismena
        zasifrovany_znak = ((ord(znak)-65 + posun) % 26) + 65
        ciphertext_list.append(chr(zasifrovany_znak))
    elif 97 <= ord(znak) <= 122: # pro mala pismena
        zasifrovany_znak = ((ord(znak)-97 + posun) % 26) + 97
        ciphertext_list.append(chr(zasifrovany_znak))
    else: # jine znaky nez mala a velka pismena zustanou nezmenena
        ciphertext_list.append(znak)

ciphertext = ''.join(ciphertext_list) # spojeni jednotlivych znaku ze seznamu opet na slova
print('Zasifrovany text je: {}'.format(ciphertext))

