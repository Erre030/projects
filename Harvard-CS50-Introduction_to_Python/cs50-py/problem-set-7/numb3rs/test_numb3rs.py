
#description: test corner cases of numb3ers.py

from numb3rs import validate

def test_validate():
  assert validate("123.300.300.300") == False
  assert validate("00123.00222.00023.00134") == False
  assert validate("123.123.123.123.123") == False
