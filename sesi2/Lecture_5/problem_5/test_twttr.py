from twttr import shorten

def test_twttr():
    assert shorten('Twitter') == 'Twttr'
    assert shorten('Hello, World') == 'Hll, Wrld'
    assert shorten('AEIOU') == ''
    assert shorten('') == ''
    assert shorten('1') == '1'