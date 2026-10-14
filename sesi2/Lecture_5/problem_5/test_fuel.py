from fuel import convert, gauge
import pytest

def test_fuel():
    assert convert('1/4') == 25
def test_value_error():
    with pytest.raises(ValueError):
        convert('cat/dog')
    with pytest.raises(ValueError):
        convert('3/2')
    with pytest.raises(ValueError):
        convert('3/-1')
    with pytest.raises(ValueError):
        convert('-1/-1')
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')
def test_gauge():
    assert gauge(1) == 'E'
    assert gauge(50) == '50%'
    assert gauge(99) == 'F'