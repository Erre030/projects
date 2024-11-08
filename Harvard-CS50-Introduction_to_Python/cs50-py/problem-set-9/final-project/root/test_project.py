
from project import Expense, name_check, pick_option

import pytest

#test correct functionality of class
def test_class():
    expense = Expense(amount="10", category="fitness studio", description="membership", regularity="monthly")
    expected_str = "Expense with amount=10, category=fitness studio, description=membership, regularity=monthly created.\n"
    assert str(expense) == expected_str

#test valid names
def test_name_check():
    assert name_check("Max / Mustermann") == ("Max","Mustermann")

    with pytest.raises(ValueError):
        name_check("Max Mustermann")
    with pytest.raises(ValueError):
        name_check("Max Must3rmann")
    with pytest.raises(ValueError):
        name_check("Max Mustermann.")

#test correct functionality of option choice
def test_pick_option():
    assert pick_option("1") == 1
    assert pick_option("2") == 2
    assert pick_option("3") == 3










