from p071_080.p071 import median_fraction, p071, p071_another
from p071_080.p072 import p072
from p071_080.p073 import p073, search_right_neighbour
from farey_seq import farey_sequence
from random import randint


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


def test_search_right_neighbour():
    test_seq = [(0, 1), (1, 7), (1, 6), (1, 5), (1, 4), (2, 7), (1, 3), (
        2, 5), (3, 7), (1, 2), (4, 7), (3, 5), (2, 3), (5, 7), (3, 4), (4, 5), (5, 6), (6, 7), (1, 1)]
    for i in range(len(test_seq) - 1):
        a, b = test_seq[i]
        assert search_right_neighbour(a, b, 7) == test_seq[i + 1]

    for _ in range(5):
        n = randint(10, 100)
        seq = list(farey_sequence(n))
        for _ in range(10):
            i = randint(0, len(seq) - 2)
            a, b = seq[i]
            assert search_right_neighbour(a, b, n) == seq[i + 1]


def test_p073():
    assert p073(1, 3, 1, 2, 8) == 3
