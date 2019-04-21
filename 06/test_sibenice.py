import pytest

import sibenice

def test_je_ve_slove():
    assert sibenice.je_ve_slove('pes', 'p') == 0
    assert sibenice.je_ve_slove('pes', 'h') == -1
    assert sibenice.je_ve_slove('pes', 's') == 2
    # assert sibenice.je_ve_slove('pes', '') == -1


def test_zapis_pismeno():
    assert sibenice.zapis_pismeno('---', 2, 's') == '--s'
    assert sibenice.zapis_pismeno('-----', 0, 'l') == 'l----'
    assert sibenice.zapis_pismeno('-----', 3, 'c') == '---c-'


def test_vyhodnot():
    assert sibenice.vyhodnot('pes', 8) == 'vyhral'
    assert sibenice.vyhodnot('pes', 10) == 'prohral'
    assert sibenice.vyhodnot('pe-', 10) == 'prohral'
    assert sibenice.vyhodnot('pe-', 8) == '-'



    

