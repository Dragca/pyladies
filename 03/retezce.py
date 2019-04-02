retezec = input('Zadej retezec:')
pozice = int(input('Zadej pozici, na ktere provedeme zmenu: '))
znak = input('Zadej novy znak, ktery na pozici dosadime')

print('Takto to po vymene vypada')
print(retezec[:pozice] + znak + retezec[pozice + 1:])