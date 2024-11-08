
import pytest

from working import convert


def test_convert():
    assert convert("12:00 AM to 12:00 PM") == ("00:00 to 12:00")
    assert convert("9 AM to 5 PM") == ("09:00 to 17:00")

def test_convert_errors():
    with pytest.raises(ValueError):
        convert("8 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("13:40 AM to 12:30 PM")
    with pytest.raises(ValueError):
        convert("11:40 AM to 12:60 PM")


