import ai


def test_tah_na_prazdne_pole():
    pole = ai.tah_pocitace('--------------------', 'x', 'o')
    assert len(pole) == 20
    assert pole.count('x') == 1
    assert pole.count('-') == 19


def test_musi_vyhrat():
    pole = ai.tah_pocitace('o-xx--------------o-', 'x', 'o')
    assert pole[1] == 'x' or pole[4] == 'x'
    assert ai.tah_pocitace('o-x-x-------------o-', 'x', 'o').find('xxx') == 2

    for pole in (
        'o-x--x-----x-x----o-',
        'o-xx--------------o-',
        'o-x-x-x--x-x---xx-----o-',
        'o-ox-x-----x-x----o-',
        ):
        assert ai.tah_pocitace(pole, 'x', 'o').find('xxx') != -1

def test_brani_mezi_dva_symboly():
    assert ai.tah_pocitace('o-ox-------x-o----o-', 'x', 'o').find('oxox') != -1

def test_brani_vedle_dvou_symbolu():
    assert ai.tah_pocitace('--oo-------x-o----o-', 'x', 'o').find('xoo') != -1
    assert ai.tah_pocitace('--oox------x-o----o-', 'x', 'o').find('xoo') != -1
    assert ai.tah_pocitace('-xoo-------x-o----o-', 'x', 'o').find('oox') != -1

def test_blokuje_jeden_symbol():
    assert ai.tah_pocitace('---o-------x-o----o-', 'x', 'o').find('xo') != -1

def test_tah_na_prazdne_s_jinou_delkou_pole():
    pole = ai.tah_pocitace('------------------------------', 'x', 'o')
    assert len(pole) == 30
    assert pole.count('x') == 1
    assert pole.count('-') == 29

def test_tah_s_jinou_delkou_pole():
    pole = ai.tah_pocitace('xoxo--------------------------', 'x', 'o')
    assert len(pole) == 30
    assert pole.count('x') == 3
    assert pole.count('o') == 2
