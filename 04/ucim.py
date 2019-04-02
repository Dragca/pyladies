zaznamy = ['pepa novak', 'Jiri Sladek', 'Ivo navratil', 'jan Polednik']
spravne = []
nespravne = []
opravene = []

for zaznam in zaznamy:
    jmeno, prijmeni = zaznam.split()
    if not jmeno[0].islower() and not prijmeni[0].islower():
        spravne.append(zaznam)
    else:
        nespravne.append(zaznam)

print(spravne)
print(nespravne)

for zaznam in zaznamy:
    jmeno, prijmeni = zaznam.split()
    opravene.append(jmeno.capitalize() +' '+  prijmeni.capitalize())

print(opravene)