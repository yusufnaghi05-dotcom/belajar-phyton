from bank import value

def test_bank():
    assert value('hello') == 0
    assert value('h') == 20
    assert value('b') == 100
    assert value('1') == 100
    assert value('') == 100
    assert value('hello there') == 0
    assert value('HELLO') == 0