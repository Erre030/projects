
#description: test expected outputs for different greetings on bank.py

#pytest only needs to be imported if it is used actively in the file, not if it is only used in the cmd-line
#(tests have to start with test_*.py and have to be collected in a file/folder called test_*.py or *_test.py)
from bank import value


def test_value_returns_0():
    assert value("hello") == 0
    assert value("Hello") == 0

def test_value_returns_20():
    assert value("hey there") == 20
    assert value("How are you doing") == 20

def test_value_returns_100():
    assert value("good morning") == 100
    assert value("Greetings") == 100

#correct data type of return (int) is already implicitly tested by the test functions above


