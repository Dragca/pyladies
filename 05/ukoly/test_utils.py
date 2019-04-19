import utils

def test_tah_na_prazdne():
    assert utils.tah('--------------------', 0, 'x') == 'x-------------------'
    assert utils.tah('--------------------', 5, 'x') == '-----x--------------'
    assert utils.tah('--------------------', 10, 'o') == '----------o---------'
    assert utils.tah('--------------------', 19, 'o') == '-------------------o'
    assert utils.tah('--------------------', 19, 'x') == '-------------------x'

def test_tah():
    assert utils.tah('ox---oxx--oxox------', 2, 'x') == 'oxx--oxx--oxox------'
    assert utils.tah('ox---oxx--oxox------', 16, 'o') == 'ox---oxx--oxox--o---'


