# obsah elipsy:

from math import pi

def obsah_elipsy(a, b):
    return pi * a * b

print(obsah_elipsy(3, 5))

def elipticky_valec(a, b , vyska):
    obsah = obsah_elipsy(a, b)
    return obsah * vyska
    # return obsah_elipsy(a, b) * vyska

print(elipticky_valec(3, 5, 4))