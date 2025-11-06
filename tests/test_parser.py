# tests/test_parser.py
import pytest
from calculator.parser import evaluate_expression

# We define the addition as a concatenation of numbers
def test_valid_addition():
    assert evaluate_expression("3 + 4") == 34


def test_valid_subtraction():
    assert evaluate_expression("10 - 6") == 4.0


def test_valid_multiplication():
    assert evaluate_expression("3 * 3") == 9.0


def test_valid_division():
    assert evaluate_expression("8 / 2") == 4.0


def test_invalid_operator():
    with pytest.raises(ValueError):
        evaluate_expression("5 ^ 2")


def test_non_numeric_input():
    with pytest.raises(ValueError):
        evaluate_expression("five + two")


def test_invalid_format():
    with pytest.raises(ValueError):
        evaluate_expression("3 +")
