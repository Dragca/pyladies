# program vypise jmena domacich zvirat, ktera zacinaji pismenem k
domaci_zvirata = ['pes', 'kocka', 'kralik', 'had']
zacinaji_k = []

for zvire in domaci_zvirata:
    if zvire[0] == 'k':
        zacinaji_k.append(zvire)
print(zacinaji_k)
