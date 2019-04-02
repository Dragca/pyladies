# Na vstupu této úlohy mají být dva seznamy zvířat, několik z nich by mělo být v obou seznamech. 
# na zacatku dva seznamy jmen zvirat a program vypise a vratu tri seznamy.
# a) zvirata, ktera jsou v obou seznamech stejna( sjednoceni mnozin prvni u druha)
# b) zvirata, ktera jsou jen v prvnim seznamu (rozdil mnozin: prvni - druha)
# c) zvirata, ktera jsou jen ve druhem seznamu(rozdil mnozin: druha - prvni)

seznam1 = ['pes', 'kocka', 'kralik', 'had']
seznam2 = ['pes', 'lemur', 'kralik', 'lenochod']
spolecne = []
jenv1 = []
jenv2 = []
for zvire in seznam1:
    if zvire in seznam2:
        spolecne.append(zvire)
    else:
        jenv1.append(zvire)
for zvire in seznam2:
    if zvire not in spolecne:
        jenv2.append(zvire)

print(spolecne)
print(jenv1)
print(jenv2)
