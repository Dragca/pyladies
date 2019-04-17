
class Kocka:
    def __init__(self):
        self.pocet_zivotu = 9

    def zamnoukej(self):
        print('Mnauuuuu!')

    def je_ziva(self):
        return self.pocet_zivotu > 0

    def uber_zivot(self):
        if self.je_ziva():
            self.pocet_zivotu -= 1

    def snez(self, jidlo):
        if not self.je_ziva():
            print('Nemuzes krmit mrtvou kocku.')
        elif jidlo == 'ryba' and self.pocet_zivotu < 9:
            self.pocet_zivotu += 1
            print('Kocka snedla rybu a ma jeden zivot navic')
        else:
            print('Kocka se krmi')


kocka = Kocka()
print(kocka.pocet_zivotu)
print(kocka.je_ziva())
kocka.snez('chleba')
kocka.uber_zivot()
kocka.snez('ryba')

    
