import itertools

from farey_seq import farey_sequence, farey_sequence_start_from_between


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
