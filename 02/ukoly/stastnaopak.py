print('Odpovidej ano nebo ne')
stastna = input ('Jsi stastna? ')
bohata = input ('Jsi bohata? ')

if not stastna in ('ano', 'ne') or not bohata in ('ano', 'ne'):
    print('Nerozumim')
elif stastna == 'ano' and bohata == 'ano':
    print('gratuluju')
elif stastna == 'ano':
    print('šetři')
elif bohata == 'ano':
    print('úsměv')
else:
    print('to je mi lito')