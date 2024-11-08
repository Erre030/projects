import pytest


from seasons import age_minutes


def test_age_minutes():
    assert age_minutes("2000-04-20") == ("Twelve million, nine hundred twelve thousand, four hundred eighty minutes")

def test_error_age_minutes():
    with pytest.raises(ValueError):         #is produced automatically by date class
        age_minutes("3132-56-01")
    with pytest.raises(ValueError):         #is produced automatically by date class
        age_minutes("2000-09-31")
    with pytest.raises(ValueError):         #is cateched by used re-pattern
        age_minutes("999-09-31")
