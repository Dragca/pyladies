#program aby se do noveho slovniku shnile ovoce ulozily puvodni klice s novou hodnotou
#kdy barva bude vzdy zacinat 'hnedo-, tzn hnedo-cervene, 

kosik = {'jablko': 'cervene', 'hruska': 'zelena', 'broskev':'oranzova', 'banan':'zluty'}
shnily_kosik = {}

for ovoce, barva in kosik.items():
    shnily_kosik[ovoce] = 'hnedo-{}'.format(barva)

print(shnily_kosik)