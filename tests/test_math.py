import pytest


def test_one_plus_one():
    assert 1 + 1 == 2


def test_one_plus_two():
    a = 1
    b = 2
    c = 3
    assert a + b == c


def test_devide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0

    assert "division by zero" in str(e.value)


products = [
    (3, 6, 18),
    (1, 99, 99),
    (0, 33, 0),
    (4, -9, -36),
    (-8, -2, 16),
    (2.5, 6.7, 16.75)
]

@pytest.mark.parametrize('a,b,p',products)
def test_multiplication(a,b,p):
    assert a * b == p