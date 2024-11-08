

from um import count

def test_count():
    assert count("um that is um yummy") == 2
    assert count("um, ok") == 1
    assert count("that is UM right") == 1
