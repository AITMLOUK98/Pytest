import pytest

import calculate
from calculate import calculate_factorial, is_palindrome, Calculator


def test_factorial_positive_numbers():
    assert calculate_factorial(0) == 1
    assert calculate_factorial(1) == 1
    assert calculate_factorial(5) == 120
    assert calculate_factorial(10) == 3628800


def test_factorial_negative_number():
    with pytest.raises(ValueError):
        calculate_factorial(-5)


@pytest.mark.strings  # us this command line  to run this test pytest test_function.py -v -m strings (you can us any
# name here can be anything ) "-m for mark and -v to show more details and -x mean exist when he get the fail  test"
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


# test using parameterize
@pytest.mark.parametrize('num1, num2, result',
                         [
                             (7, 3, 10),
                             ('hello', ' world', 'hello world'),
                             (5.5, 3, 8.5)
                         ])
def test_parameterize_add(num1, num2, result):
    assert calculate.add(num1, num2) == result
