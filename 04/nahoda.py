from random import shuffle, choice

balicek = []

for pismeno in 'A', 'B', 'C', 'D':
    for hodnota in range(2, 11):
        balicek.append(str(hodnota) + pismeno)

print(balicek)
tah = choice(balicek)
print(tah)