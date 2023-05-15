import pytest
from calculate import calculate_factorial, is_palindrome, Calculator


def test_factorial_positive_numbers():
    assert calculate_factorial(0) == 1
    assert calculate_factorial(1) == 1
    assert calculate_factorial(5) == 120
    assert calculate_factorial(10) == 3628800


def test_factorial_negative_number():
    with pytest.raises(ValueError):
        calculate_factorial(-5)


def test_palindrome():
    assert is_palindrome("radar")
    assert is_palindrome("level")
    assert not is_palindrome("hello")


def test_calculator():
    calculator = Calculator()
    calculator.add(5, 3)
    assert calculator.result == 8

    calculator.subtract(10, 2)
    assert calculator.result == 8

    calculator.multiply(4, 3)
    assert calculator.result == 12

    calculator.divide(15, 3)
    assert calculator.result == 5

    with pytest.raises(ValueError):
        calculator.divide(10, 0)
