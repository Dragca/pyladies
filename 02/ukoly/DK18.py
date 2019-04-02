# Tento program rozdává naivní rady do života.
print('Odpovídej "ano" nebo "ne".')
stastna = input('Jsi šťastná? ')
bohata = input('Jsi bohatá? ')

if stastna == 'ano':
    if bohata == 'ano':  # Je bohatá a zároveň šťastná, ta se má. 
        print('Gratuluju') 
    elif bohata == 'ne':  # Je šťastná, ale není bohatá.
        print('Zkus míň utrácet nebo začni víc vydělávat.') 
    else: 
         print('Nerozumím! Tvoje odpověď měla být ano nebo ne.')  # Nesprávná odpověď na bohatá.
elif stastna == 'ne':
    if bohata == 'ano':  # Není šťastná :-(, ale je bohatá.
        print('Zkus se víc usmívat :-).')
    elif bohata == 'ne':  # Není ani bohatá ani šťastná :-(.
        print('To je mi líto, určitě bude brzy líp!')
    else:
        print('Nerozumím! Tvoje odpověď měla být ano nebo ne.')
else:
    print('Nerozumím! Tvoje odpověď měla být ano nebo ne.')  # nesprávná odpověď na šťastná
