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

for zaznam in zaznamy:
    jmeno, prijmeni = zaznam.split()
    jmeno.capitalize() and prijmeni.capitalize()
    opravene.append(jmeno.capitalize() + ' ' + prijmeni.capitalize())

print(spravne)
print(nespravne)
print(opravene)