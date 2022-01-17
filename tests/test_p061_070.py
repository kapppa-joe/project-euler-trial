import random
import pytest

from p061_070.p061 import first_two_digits, last_two_digits,  make_polygonal_number_dicts, p061, p061_recur, p061_start_recur
from p061_070.p062 import p062

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
