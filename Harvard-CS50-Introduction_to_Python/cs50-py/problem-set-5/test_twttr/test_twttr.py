
#description: unit tests for twttr.py to test if file functions properly (vowel replacement, no omitting of numbers and punctuation, raises Type Error if input is int or float).

import pytest
from twttr import shorten


def test_shorten_replace():
    assert shorten("HELLO") == "HLL"
    assert shorten("hello") == "hll"
    assert shorten("HEllo") == "Hll"

def test_shorten_numbers():
    assert shorten("Hello1") == "Hll1"

def test_shorten_punctuation():
    assert shorten("Hello.") == "Hll."

def test_shorten_type():
    with pytest.raises(TypeError):
        shorten(1)
    with pytest.raises(TypeError):
        shorten(1.1)
