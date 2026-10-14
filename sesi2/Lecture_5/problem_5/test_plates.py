from plates import is_valid

def test_plates():
    assert is_valid('CS50') == True
    assert is_valid('adnadn22') == False
    assert is_valid('2250') == False
    assert is_valid('AA05') == False
    assert is_valid('A0OOP') == False
    assert is_valid('CS5S') == False
    assert is_valid('C.S50') == False
    assert is_valid('CS 50') == False