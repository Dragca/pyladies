# program dostane slovo a zjisti, jestli je v seznamu domaci_zvirata, 
# zjisti znamena vrati True nebo False
domaci_zvirata = ['pes', 'kocka', 'kralik', 'had']
slovo = input('Zadej slovo, program ti rekne, jeslti je v seznamu domacich zvirat. ')
print(slovo in domaci_zvirata)
    