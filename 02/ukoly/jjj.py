print('Odpovidej ano nebo ne')
stastna = input ('Jsi stastna?')

if stastna == "ano":
    stastna = True
elif stastna == "ne":
    stastna = False
else:
    print('Nerozumim')
    exit()

bohata = input ('Jsi bohata?')
if bohata == "ano":
    bohata = True
elif bohata == "ne":
    bohata = False
else:
    print('Nerozumim')
    exit()

if stastna and bohata:
    print('Gratuluji')
elif bohata:
    print('úsměv')
elif stastna:
    print('šetři')
else:
    print('to je mi lito')