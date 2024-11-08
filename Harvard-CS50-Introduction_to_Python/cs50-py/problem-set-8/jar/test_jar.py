
#First import class, then perform tests on the specific functions of the class by creating specific scenarios

import pytest

from jar import Jar


def test_init():
    with pytest.raises(ValueError):
        jar = Jar(-1)
    with pytest.raises(ValueError):
        jar = Jar("cat")


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(12)
    with pytest.raises(ValueError):
        jar.deposit(14)



def test_withdraw():
    jar = Jar(10)
    jar.deposit(7)
    with pytest.raises(ValueError):
        jar.withdraw(9)

