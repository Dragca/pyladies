import piskvorky


def test_vyhodnot():
    assert piskvorky.vyhodnot('ox---xxx--oxox------') == 'x'
    assert piskvorky.vyhodnot('ox---xxo--ooox------') == 'o'
    assert piskvorky.vyhodnot('oxoxoxoxxooxoxxooxox') == '!'
    assert piskvorky.vyhodnot('oxoxoxox-ooxoxxooxox') == '-'
    assert piskvorky.vyhodnot('--------------------') == '-'
