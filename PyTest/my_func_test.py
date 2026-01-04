import pytest
import my_func

def test_add():
    res = my_func.add(2,3)
    assert res == 5

def test_divide():
    res = my_func.divide(6,3)
    assert res==2

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        my_func.divide(2,0)

def test_add_strings():
    res = my_func.add("I like ", "burgers.")
    assert res == "I like burgers."