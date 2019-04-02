# program vypise jmena domacich zvirat, ktera jsou kratsi nez 5 pismen
domaci_zvirata = ['pes', 'kocka', 'kralik', 'had']
kratke = []

for zvire in domaci_zvirata:
    if len(zvire) < 5:
        kratke.append(zvire)

print(kratke)
