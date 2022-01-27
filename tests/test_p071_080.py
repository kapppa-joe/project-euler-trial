from p071_080.p071 import median_fraction, p071, p071_another
from p071_080.p072 import p072


def test_median_fraction():
    assert median_fraction(0, 1, 1, 1) == (1, 2)
    assert median_fraction(0, 1, 1, 2) == (1, 3)
    assert median_fraction(1, 2, 1, 1) == (2, 3)
    assert median_fraction(1, 4, 2, 3) == (3, 7)


def test_p071():
    assert p071(target_d=8) == (2, 5)
    assert p071(2, 3, 8) == (5, 8)
    assert p071(5, 6, 7) == (4, 5)
    assert p071(target_d=10000) == (4283, 9994)
    assert p071(target_d=1_000_000) == (428570, 999997)


def test_p071_another():
    assert p071_another(target_d=8) == (2, 5)
    assert p071_another(2, 3, 8) == (5, 8)
    assert p071_another(5, 6, 7) == (4, 5)
    assert p071_another(123, 4567, 10000) == (269, 9988)
    assert p071_another(target_d=10000) == (4283, 9994)
    assert p071_another(target_d=1_000_000) == (428570, 999997)


def test_p072():
    assert p072(8) == 21
