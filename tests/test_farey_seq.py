import itertools
from random import randint

from farey_seq import farey_sequence, farey_sequence_start_from_between, search_left_neighbour, search_right_neighbour, median_fraction


def test_farey_sequence():
    assert list(farey_sequence(2)) == [(0, 1), (1, 2), (1, 1)]
    assert list(farey_sequence(7)) == [(0, 1), (1, 7), (1, 6), (1, 5), (1, 4), (2, 7), (1, 3), (
        2, 5), (3, 7), (1, 2), (4, 7), (3, 5), (2, 3), (5, 7), (3, 4), (4, 5), (5, 6), (6, 7), (1, 1)]

    s = farey_sequence(1_000_000)
    assert list(itertools.islice(s, 3)) == [
        (0, 1), (1, 1_000_000), (1, 999_999)]


def test_farey_sequence_start_from_between():
    assert list(farey_sequence_start_from_between(7, 1, 3, 2, 5)) == [(1, 3), (
        2, 5), (3, 7), (1, 2), (4, 7), (3, 5), (2, 3), (5, 7), (3, 4), (4, 5), (5, 6), (6, 7), (1, 1)]


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


def test_median_fraction():
    assert median_fraction(0, 1, 1, 1) == (1, 2)
    assert median_fraction(0, 1, 1, 2) == (1, 3)
    assert median_fraction(1, 2, 1, 1) == (2, 3)
    assert median_fraction(1, 4, 2, 3) == (3, 7)


def test_search_left_neighbour():
    test_seq = [(0, 1), (1, 7), (1, 6), (1, 5), (1, 4), (2, 7), (1, 3), (
        2, 5), (3, 7), (1, 2), (4, 7), (3, 5), (2, 3), (5, 7), (3, 4), (4, 5), (5, 6), (6, 7), (1, 1)]
    for i in range(1, len(test_seq)):
        c, d = test_seq[i]
        assert search_left_neighbour(c, d, 7) == test_seq[i - 1]

    for _ in range(5):
        n = randint(10, 100)
        seq = list(farey_sequence(n))
        for _ in range(10):
            i = randint(1, len(seq) - 1)
            c, d = seq[i]
            assert search_left_neighbour(c, d, n) == seq[i - 1]
