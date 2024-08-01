
#description: checking requirements given for plates by checking function is_valid() of file plates.py

from plates import is_valid

def test_is_valid_two_letters():
    assert is_valid("HELLO") == True
    assert is_valid("H1EllO") == False
    assert is_valid("1ELLO") == False

def test_is_valid_length():
    assert is_valid("A") == False
    assert is_valid("AA12345") == False

def test_is_valid_numbers():
    assert is_valid("AAA22") == True
    assert is_valid("AAA22A") == False
    assert is_valid("AAA2A2") == False
    assert is_valid("AAA02") == False

def test_is_valid_punctuation():
    assert is_valid("HE.LLO") == False
    assert is_valid("HE!LLO") == False
    assert is_valid("HE?LLO") == False
    assert is_valid("HE LLO") == False

def test_is_valid_non_alphabetical():
    assert is_valid("12345") == False


