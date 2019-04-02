# tyto programy maji na vstupu retezec s rodnym cislem a zanalyzuji ho:
# a) zda je ve spravnem formatu : 6 cislic, lomitko, 4 cislice? - vypise True/ False
# b) zda je dělitelne 11 - vypise True/False
# c) jake datum narozeni je v cisle zakodovano? (vypise trojici cisel - den, mesic, rok )
# d) jake pohlavi je v cisle zakodovano? (vypise 'muz'/'zena)

rodne_cislo = '736028/5163'
rodne_cislo_bez_lomitka = (rodne_cislo[0:6] + rodne_cislo[7:])
cislice = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# a)
pred_lomitkem = rodne_cislo[0:6]
za_lomitkem = rodne_cislo[7:]

print(pred_lomitkem.isnumeric())
print(rodne_cislo[6] == '/')
# spravne = len(rodne_cislo) == 11 and rodne_cislo[6] == '/' and 

