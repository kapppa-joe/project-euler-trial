import pytest

from p041_050.p041 import find_largest_pandigital_prime
from p041_050.p042 import is_triangle_number, word_value
from p041_050.p043 import satisfy_divisible_properties
from p041_050.p045 import p045
from p041_050.p046 import is_sum_of_prime_and_twice_a_square, odd_composite_nums, square_nums
from util import int_to_digits


def test_p041_find_largest_pandigital_prime():
    assert find_largest_pandigital_prime(1) == None
    assert find_largest_pandigital_prime(2) == None
    assert find_largest_pandigital_prime(3) == None
    assert find_largest_pandigital_prime(4) == 4231
    assert find_largest_pandigital_prime(5) == None
    assert find_largest_pandigital_prime(6) == None
    assert find_largest_pandigital_prime(7) == 7652413


test_cases_p042_word_value = [
    ('A', 1),
    ('B', 2),
    ('Z', 26),
    ('AB', 3),
    ('CBA', 6),
    ('AZ', 27),
    ('SKY', 55),
]


@pytest.mark.parametrize("word, expected_output", test_cases_p042_word_value)
def test_p042_word_value(word, expected_output):
    assert word_value(word) == expected_output


triangle_nums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
test_cases_p042_is_triangle_num = [
    (num, num in triangle_nums) for num in range(60)]


@pytest.mark.parametrize("num, expected_output", test_cases_p042_is_triangle_num)
def test_p042_is_triangle_number(num, expected_output):
    assert is_triangle_number(num) == expected_output


def test_p043_satisfy_divisible_properties():
    assert satisfy_divisible_properties((1, 4, 0, 6, 3, 5, 7, 2, 8, 9)) == True
    assert satisfy_divisible_properties(
        (1, 4, 0, 6, 3, 5, 7, 2, 8, 8)) == False
    for num in [1406357289, 1430952867, 1460357289, 4106357289, 4130952867, 4160357289]:
        assert satisfy_divisible_properties(tuple(int_to_digits(num))) == True


def test_p045():
    assert p045(lower_limit=0) == 1
    assert p045(lower_limit=1) == 40755
    assert p045(lower_limit=40755) == 1533776805


def test_p046_odd_composite_nums():
    gen = odd_composite_nums()
    assert next(gen) == 9
    assert next(gen) == 15
    assert next(gen) == 21
    assert next(gen) == 25
    assert next(gen) == 27
    assert next(gen) == 33


def test_p046_square_nums():
    assert list(square_nums(10)) == [1, 4, 9]
    assert list(square_nums(100)) == [1, 4, 9, 16, 25, 36, 49, 64, 81]


def test_p046_is_sum_of_prime_and_twice_a_square():
    for i in [9, 15, 21, 25, 27, 33]:
        assert is_sum_of_prime_and_twice_a_square(i) == True
