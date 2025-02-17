import pytest

from Week11.calculator import add, divide, multiply, power, prime, subtract


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 5) == 5


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)


def test_prime():
    assert prime(-1) is False
    assert prime(1) is False
    assert prime(2) is True
    assert prime(10) is False


def test_power():
    assert power(1, 0) == 1
    assert power(2, 2) == 4
    assert power(2, -2) == 1 / 4
    assert power(2, 3) == 8
