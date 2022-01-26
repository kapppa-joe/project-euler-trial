from p071_080.p071 import median_fraction, p071


def test_median_fraction():
    assert median_fraction(0, 1, 1, 1) == (1, 2)
    assert median_fraction(0, 1, 1, 2) == (1, 3)
    assert median_fraction(1, 2, 1, 1) == (2, 3)
    assert median_fraction(1, 4, 2, 3) == (3, 7)


def test_p071():
    assert p071(target_d=8) == (2, 5)
    assert p071(2, 3, 8) == (5, 8)
    assert p071(5, 6, 7) == (4, 5)
    assert p071(target_d=1_000_000) == (428570, 999997)
