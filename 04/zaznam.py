zaznamy = ['pepa novak', 'Jiri Sladek', 'Ivo navratil', 'jan Polednik']

spravne = []
nespravne = []

#for zaznam in zaznamy:
#    jmeno, prijmeni = zaznam.split()
#    if not jmeno[0].islower() and not prijmeni[0].islower():
#        spravne.append(zaznam)

#print(spravne)

#for zaznam in zaznamy:
#    jmeno, prijmeni = zaznam.split()
#    if jmeno[0].islower() or prijmeni[0].islower():
#        nespravne.append(zaznam)

#print(nespravne)

for zaznam in zaznamy:
    jmeno, prijmeni = zaznam.split()
    if not jmeno[0].islower() and not prijmeni[0].islower():
        spravne.append(zaznam)
    else:
        nespravne.append(zaznam)

print(spravne)
print(nespravne)
