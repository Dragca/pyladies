#tento program po zadání správného hesla 
#vypíše tajnou informaci

heslo = input('Jaká je odpověď na základní otázku života, vesmíru a vůbec je? ')
if heslo == '42':
    print('Správně! Povím ti tajemství: všechno řídí myši!')
else:
    print(3 * 'Pozor! ', 'Vetřelec!', 3 * 'ALARM! ')
