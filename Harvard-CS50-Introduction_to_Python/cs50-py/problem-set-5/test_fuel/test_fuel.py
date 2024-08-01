

#description: test if fuel.py behaves like intended

import pytest
from fuel import convert, gauge

def test_convert():
  assert convert("1/3") == 33
  assert convert("1/1") == 100
  assert convert("0/1") == 0

  with pytest.raises(ZeroDivisionError):
    convert("1/0")
  with pytest.raises(ValueError):
    convert("2/1")
  with pytest.raises(ValueError):
    convert("1/-1")
  with pytest.raises(ValueError):
    convert("one/one")

def test_gauge():
  assert gauge(0) == "E"
  assert gauge(1) == "E"
  assert gauge(50) == "50%"
  assert gauge(99) == "F"
  assert gauge(100) == "F"


