from numb3rs import validate

def test_numb3rs():
    assert validate("192.10.0.2") == True
    assert validate("cat") == False
    assert validate("999.0.0.10") == False
    assert validate("-1.0.20.0") == False
    assert validate("255.255.255.255") == True
    assert validate("1") == False
    assert validate("30.0.-2.0") == False
    assert validate("999.0.0.2002") == False
    assert validate("10.366.0.2") == False
    assert validate("10.20.290.2") == False
    assert validate("10.4.0.499") == False
    assert validate("10.001.0.2") == False