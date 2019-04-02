domaci_zvirata = ['pes', 'kocka', 'kralik', 'krkavec', 'had', 'andulka']
klic_hodnota = []
serazena_zvirata = []


# do zeznamu klic_hodnota uklada n-tice (klic,hodnota)
for zvire in domaci_zvirata:
    ostatni = zvire[1:]
    klic_hodnota.append((ostatni, zvire))

klic_hodnota.sort()
print(klic_hodnota)

#for i in range(len(klic_hodnota):
#    zvire = klic_hodnota[i][1]
#    print(zvire)

# ze serazeneho seznamu klic hodnota uklada postupne zvirata do seznamu serazena_zvirata
for dvojice in klic_hodnota:
    zvire = dvojice[1]
    serazena_zvirata.append(zvire)
print(serazena_zvirata)

