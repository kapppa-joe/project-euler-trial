import random
import pytest
import itertools

from p061_070.p061 import first_two_digits, last_two_digits,  make_polygonal_number_dicts, p061, p061_recur, p061_start_recur
from p061_070.p062 import p062
from p061_070.p064 import count_period, p064
from p061_070.p065 import e_a_terms, p065, sqrt_2_a_terms, expand_inf_fraction

from polygonal_numbers import polygonal_number_generator


def test_p061_first_two_digits_and_last_two_digits():
    for _ in range(100):
        num = random.randint(1000, 9999)
        num_str = str(num)
        assert first_two_digits(num) == int(num_str[:2])
        assert last_two_digits(num) == int(num_str[2:])


P061_polygon_num_range = {
    # the range where polygon number Pn,i lies in 1000~9999
    3: range(45, 141),
    4: range(32, 100),
    5: range(26, 82),
    6: range(23, 71),
    7: range(21, 64),
    8: range(19, 59)
}


@pytest.mark.parametrize("n", range(3, 9))
def test_p061_make_polygonal_number_dicts(n):
    number_dict = make_polygonal_number_dicts(n)
    for i in P061_polygon_num_range[n]:
        num = next(polygonal_number_generator(n, i))
        first_half = int(str(num)[:2])
        latter_half = int(str(num)[2:])
        if first_half >= 10 and latter_half >= 10:
            assert latter_half in number_dict[first_half]


def test_p061_recur():
    # simple test case
    test_case_dict = {3: {30: {40, 41, 42}},
                      4: {40: {50, 51, 52}},
                      5: {50: {30, 31, 32}}}
    starting_solution = {5: 5030}
    starting_key = 30
    test_solution = p061_recur(
        num_dicts=test_case_dict, solution=starting_solution, curr_key=starting_key)
    assert test_solution == {3: 3040, 4: 4050, 5: 5030}

    # actual test case for wanted polygons = 3 to 5
    test_case_dict = {n: make_polygonal_number_dicts(n) for n in range(3, 6)}
    starting_solution = {5: 2882}
    starting_key = 82
    test_solution = p061_recur(
        num_dicts=test_case_dict, solution=starting_solution, curr_key=starting_key)
    assert test_solution == {3: 8128, 4: 8281, 5: 2882}


def test_p061_start_recur():
    # simple test case
    test_case_dict = {3: {30: {40, 41, 42}},
                      4: {40: {50, 51, 52}},
                      5: {50: {30, 31, 32}}}
    assert p061_start_recur(test_case_dict) == {3: 3040, 4: 4050, 5: 5030}

    # actual test case for wanted polygons = 3 to 5
    test_case_dict = {n: make_polygonal_number_dicts(n) for n in range(3, 6)}
    assert p061_start_recur(test_case_dict) == {3: 8128, 4: 8281, 5: 2882}


def test_p061():
    assert p061(range(3, 5)) == sum([2556, 5625])
    assert p061(range(3, 6)) == sum([8128, 8281, 2882])
    assert p061(range(3, 7)) == sum([7021, 2116, 5370, 1653])
    assert p061(range(3, 8)) == sum([2850, 8281, 5017, 1782, 8128])
    assert p061(range(3, 9)) == sum([8256, 5625, 2882, 8128, 2512, 1281])


def test_p062():
    assert p062(3) == 41063625
    assert p062(5) == 127035954683


def test_p064_count_period():
    assert count_period(2) == 1
    assert count_period(3) == 2
    assert count_period(4) == 0
    assert count_period(5) == 1
    assert count_period(6) == 2
    assert count_period(7) == 4
    assert count_period(8) == 2
    assert count_period(9) == 0
    assert count_period(10) == 1
    assert count_period(11) == 2
    assert count_period(12) == 2
    assert count_period(13) == 5


def test_p064():
    assert p064(13) == 4


def test_p065_sqrt_2_a_terms():
    assert list(itertools.islice(sqrt_2_a_terms(), 10)) == [
        1, 2, 2, 2, 2,
        2, 2, 2, 2, 2
    ]


def test_p065_e_a_terms():
    assert list(itertools.islice(e_a_terms(), 20)) == [
        2, 1, 2, 1, 1,
        4, 1, 1, 6, 1,
        1, 8, 1, 1, 10,
        1, 1, 12, 1, 1
    ]


def test_p065_expand_inf_fraction():
    expand_sqrt_2 = expand_inf_fraction(sqrt_2_a_terms())
    assert next(expand_sqrt_2) == (1, 1)
    assert next(expand_sqrt_2) == (3, 2)
    assert next(expand_sqrt_2) == (7, 5)
    assert next(expand_sqrt_2) == (17, 12)
    assert next(expand_sqrt_2) == (41, 29)

    first_10_terms_for_sqrt_2 = itertools.islice(
        expand_inf_fraction(sqrt_2_a_terms()), 10)
    assert list(first_10_terms_for_sqrt_2) == [
        (1, 1), (3, 2), (7, 5), (17, 12), (41, 29),
        (99, 70), (239, 169), (577, 408), (1393, 985), (3363, 2378)]

    expand_e = expand_inf_fraction(e_a_terms())
    first_10_terms_for_e = itertools.islice(expand_e, 10)
    assert list(first_10_terms_for_e) == [
        (2, 1), (3, 1), (8, 3), (11, 4), (19, 7),
        (87, 32), (106, 39), (193, 71), (1264, 465), (1457, 536)
    ]


def test_p065():
    assert p065(10) == 17
    assert p065() == 272
