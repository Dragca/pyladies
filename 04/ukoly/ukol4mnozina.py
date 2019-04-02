# Na vstupu této úlohy mají být dva seznamy zvířat, několik z nich by mělo být v obou seznamech. 
# na zacatku dva seznamy jmen zvirat a program vypise a vratu tri seznamy.
# a) zvirata, ktera jsou v obou seznamech stejna( sjednoceni mnozin prvni u druha)
# b) zvirata, ktera jsou jen v prvnim seznamu (rozdil mnozin: prvni - druha)
# c) zvirata, ktera jsou jen ve druhem seznamu(rozdil mnozin: druha - prvni)
seznam1 = set(['pes', 'kocka', 'kralik', 'had'])
seznam2 = set(['pes', 'lemur', 'kralik', 'lenochod'])
spolecne = set([seznam1&seznam2])
jenv1 = set([seznam1-seznam2])
jenv2 = set([seznam2-seznam1])

print(spolecne)
print(jenv1)
print(jenv2)