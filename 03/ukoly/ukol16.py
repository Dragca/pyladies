#kalkulačka, uživatel zadá oba operandy i operator


from operator import add, sub, mul, truediv

prvni_cislo = float(input('Zadej prvni cislo'))
druhe_cislo = float(input('Zadej druhe cislo'))
operator = input('Zadej znamenko operace, kterou chces\n mezi cisly provest, tj. +, -, *, / ')
ops = {'+': add, '-': sub, '*': mul, '/': truediv}
if operator not in ops:
    print('nespravne znamenko operace')
    exit()

vysledek = ops[operator](prvni_cislo, druhe_cislo) 
print(vysledek)
