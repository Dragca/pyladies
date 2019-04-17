# nazev tridy se pise velkym pismenem, ve tride pisi METODY ne funkce, ale jsou to funkce

class Kotatko:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def zamnoukej(self):
        print('{}: Mnau!'.format(self.jmeno))

    def snez(self, jidlo):
        print('{}: Mnau mnau! {} mi chutna!'.format(self.jmeno, jidlo))
    


mourek = Kotatko('Mourek')
mourek.zamnoukej()
mourek.snez('ryba')

