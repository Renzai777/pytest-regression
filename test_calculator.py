import pytest

from calculator import Calculator


def test_add():
    calc = Calculator()
    result = calc.add(5, 3)
    assert result == 8, "Expected 5 + 3 to be 8"


@pytest.mark.parametrize("a, b", [(10, 4), (20, 5), (8, 2)])
def test_subtract(a, b):
    calc = Calculator()
    result = calc.subtract(a, b)
    print(f"Testing subtraction of {a} - {b}")
    print(f"Result: {result}")
    assert result == a - b, f"Expected {a} - {b} to be {a - b}"


def test_multiply():
    calc = Calculator()
    result = calc.multiply(2, 3)
    assert result == 6, "Expected 2 * 3 to be 6"
