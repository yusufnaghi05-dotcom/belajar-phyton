from seasons import convert

def test_seasons():
    assert convert("1999-01-01") == "Fourteen million, six hundred sixty-four thousand, nine hundred sixty minutes"
    assert convert("1999-02-02") == "Fourteen million, six hundred eighteen thousand, eight hundred eighty minutes"
    assert convert("January 1, 1999") == "Invalid date"
    assert convert("1999-12-31") == "Fourteen million, one hundred forty thousand, eight hundred minutes"
    assert convert("") == "Invalid date"
        
    
    