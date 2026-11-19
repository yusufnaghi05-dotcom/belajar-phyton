from seasons import convert
import pytest
def test_seasons():
    assert convert("1999-01-01") == "Fourteen million, six hundred sixty-four thousand, nine hundred sixty minutes"
    assert convert("1999-02-02") == "Fourteen million, six hundred eighteen thousand, eight hundred eighty minutes"
    assert convert("1999-12-31") == "Fourteen million, one hundred forty thousand, eight hundred minutes"
    
def test_1():
    with pytest.raises(ValueError):
        convert("January 1, 1999")
        
def test_2():
    with pytest.raises(ValueError):
        convert("February 6th, 1998")

def test_3():
    with pytest.raises(ValueError):
        convert("")
        
def test_4():
    with pytest.raises(ValueError):
        convert("2027-09-09")


    
    