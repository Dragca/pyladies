# Tento program píše různé hlášky na uživatelem zadané hodnoty

rychlost = int(input('Zadej rychlost svojí chůze do práce v km/hod. '))
if rychlost >= 300:
    print('Ty máš tryskáč?')
elif rychlost >= 150:
    print('Čím to jezdíš? Pendolinem?')
elif rychlost >= 50:
    print ('Dneska autem?')
elif rychlost >= 20:
    print('Nespěchej, vrátnej ještě spí')
elif rychlost >= 5:
    print('Tys začal běhat?')
elif rychlost >= 3:
    print('Pospěš, ať odpoledne stihneš pivo!')
elif rychlost >= 1:
    print ('Takhe to nestihneš ani na desátou.')
elif rychlost == 0: 
    print('Nestůj.')
else:
    print('Záporná rychlost? Snažíš se dohnat včerejšek?')