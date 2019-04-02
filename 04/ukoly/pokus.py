print('''Vita te program "Cesarova sifra". Program dokaze podle zadaneho
klice (cislo, o kolik se zasifrovany znak posune v abecede) zasifrovat text
bez diakritiky.''')


while True:
    klic = input('''Zadej tajne cislo, bude to klic, podle ktereho se bude text sifrovat.
Musi to byt kladne cele cislo. ''') 
    spravny_klic = klic.isdecimal() and int(klic) >= 0

    print(spravny_klic)