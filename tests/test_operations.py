import pytest
from calculator.operations import add, subtract, multiply, divide


def test_add():
    assert add.compute(2, 3) == 5


def test_subtract():
    assert subtract.compute(5, 2) == 3


def test_multiply():
    assert multiply.compute(4, 3) == 12


def test_divide():
    assert divide.compute(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide.compute(10, 0)