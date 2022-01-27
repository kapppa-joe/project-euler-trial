import pytest
import itertools
from totient import Totients, phi, farey_sequence, farey_sequence_start_from_between

Totient_function_testcases = [
    # (n, phi(n))
    (2, 1),
    (3, 2),
    (4, 2),
    (5, 4),
    (6, 2),
    (7, 6),
    (8, 4),
    (9, 6),
    (10, 4),
    (4321, 4144),
    (5432, 2304),
    (123456, 41088)
]

T = Totients(1_000_000)


@pytest.mark.parametrize("n, expected_output", Totient_function_testcases)
def test_Totient(n, expected_output):
    assert T.totient(n) == expected_output


N_over_totient_function_testcases = [
    # (n, phi(n))
    (2, 2),
    (3, 1.5),
    (4, 2),
    (5, 1.25),
    (6, 3),
    (7, 7/6),
    (8, 2),
    (9, 1.5),
    (10, 2.5),
    (123456, 123456 / 41088)
]


@pytest.mark.parametrize("n, expected_output", N_over_totient_function_testcases)
def test_n_over_totient_function(n, expected_output):
    assert T.n_over_totient_n(n) == expected_output


@pytest.mark.parametrize("n, expected_output", Totient_function_testcases)
def test_phi(n, expected_output):
    assert phi(n) == expected_output


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
