from random import randint
from p071_080.p071 import p071
from p071_080.p072 import p072
from p071_080.p073 import p073

from farey_seq import farey_sequence


def test_p071():
    assert p071(target_d=8) == (2, 5)
    assert p071(2, 3, 8) == (5, 8)
    assert p071(5, 6, 7) == (4, 5)
    assert p071(123, 4567, 10000) == (269, 9988)
    assert p071(target_d=10000) == (4283, 9994)
    assert p071(target_d=1_000_000) == (428570, 999997)


def test_p072():
    assert p072(8) == 21


def test_p073():
    assert p073(1, 3, 1, 2, 8) == 3

    # random test
    for _ in range(5):
        n = randint(10, 100)
        seq = list(farey_sequence(n))
        for _ in range(10):
            (start, stop) = sorted(
                (randint(0, len(seq) - 1), randint(0, len(seq) - 1)))
            a, b = seq[start]
            c, d = seq[stop]
            assert p073(a, b, c, d, n) == stop - start - 1
