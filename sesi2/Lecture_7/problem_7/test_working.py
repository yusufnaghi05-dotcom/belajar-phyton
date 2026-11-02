from working import convert
import pytest
def test_working():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:30 PM") == "09:00 to 17:30"
def test_invalid_number():
    with pytest.raises(ValueError):
        convert("13 AM to 5:00 PM")
def test_str():
    with pytest.raises(ValueError):
        convert("cat")