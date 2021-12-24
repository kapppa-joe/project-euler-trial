import pytest
import itertools

from p031_040.p031 import CoinChange, DefaultCoinSet, p031
from p031_040.p033 import digit_cancelling_fractions
from p031_040.p034 import digit_factorials_sum
from p031_040.p035 import is_circular_prime, p035
from p031_040.p036 import p036
from p031_040.p037 import build_both_sides_truncatable_primes, build_ltr, build_rtl, is_both_sides_truncatable_prime, trunc_left, trunc_right
from util import is_prime


@pytest.fixture
def coins():
    return CoinChange(DefaultCoinSet)


def test_p031_count_ways_to_make_change(coins):
    assert coins.count_ways_to_make_change(0) == 1
    assert coins.count_ways_to_make_change(1) == 1
    assert coins.count_ways_to_make_change(2) == 2  # 1p * 2, 2p
    assert coins.count_ways_to_make_change(3) == 2  # 1p * 3, 2p + 1p
    assert coins.count_ways_to_make_change(
        4) == 3  # 1p * 4, 2p + 1p * 2, 2p * 2
    assert coins.count_ways_to_make_change(10) == 11


def test_p031_list_ways_to_make_change(coins):
    assert coins.list_ways_to_make_change(0) == [[]]
    assert coins.list_ways_to_make_change(1) == [[1]]
    assert coins.list_ways_to_make_change(2) == [[2], [1, 1]]
    assert coins.list_ways_to_make_change(3) == [[2, 1], [1, 1, 1]]
    assert coins.list_ways_to_make_change(10) == [[10], [5, 5], [5, 2, 2, 1], [5, 2, 1, 1, 1], [
        5]+[1]*5, [2]*5, [2]*4 + [1] * 2, [2] * 3 + [1] * 4, [2] * 2 + [1] * 6, [2] + [1] * 8, [1] * 10]


def test_p031():
    assert p031(200) == 73682


def test_p033_digit_cancelling_fractions():
    assert digit_cancelling_fractions(1, 1) == False
    assert digit_cancelling_fractions(1, 2) == False
    assert digit_cancelling_fractions(8, 9) == False
    assert digit_cancelling_fractions(4, 8) == True  # 49 / 98
    assert digit_cancelling_fractions(1, 4) == True  # 16 / 64
    assert digit_cancelling_fractions(1, 5) == True  # 19 / 95
    assert digit_cancelling_fractions(2, 5) == True  # 26 / 65


def test_p034_digit_factorials_sum():
    assert digit_factorials_sum(1) == 1
    assert digit_factorials_sum(10) == 2  # 1 + 1
    assert digit_factorials_sum(12) == 3  # 1 + 2
    assert digit_factorials_sum(34) == 30  # 6 + 24
    assert digit_factorials_sum(134) == 31
    assert digit_factorials_sum(9999) == 362880 * 4


test_cases_p035_is_circular_prime = [(2, True), (3, True), (5, True), (7, True), (11, True), (13, True), (17, True), (19, False), (23, False), (
    29, False), (31, True), (37, True), (41, False), (43, False), (47, False), (53, False), (59, False), (79, True), (97, True), (197, True), (1193, True), (99371, True), (999331, True)]


@pytest.mark.parametrize("prime, expectedOutput", test_cases_p035_is_circular_prime)
def test_p035_is_circular_prime(prime, expectedOutput):
    assert is_circular_prime(prime) == expectedOutput


def test_p035():
    assert p035(2) == 0
    assert p035(10) == 4
    assert p035(100) == 13
    assert p035(1_000_000) == 55


def test_p036():
    assert p036(1) == 0
    assert p036(2) == 1  # 0b1
    assert p036(3) == 1  # 0b10 is not binary palindromic
    assert p036(4) == 4  # ob01 + 0b11
    assert p036(6) == 9
    assert p036(8) == 16
    assert p036(10) == 25
    assert p036(34) == 58  # bin(33) == 0b100001
    assert p036(1_000_000) == 872187


def test_p037_build_ltr():
    g = build_ltr(prime_checker=is_prime)
    outputs = itertools.takewhile(lambda x: x < 2500, g)
    assert list(outputs) == [23, 29, 31, 37, 53, 59, 71, 73, 79,
                             233, 239, 293, 311, 313, 317, 373, 379, 593, 599, 719, 733, 739, 797,
                             2333, 2339, 2393, 2399]


def test_p037_build_rtl():
    g = build_rtl(prime_checker=is_prime)
    outputs = itertools.takewhile(lambda x: x < 2500, g)
    assert list(outputs) == [13, 17, 23, 37, 53, 73, 97,
                             113, 137, 173, 197, 223, 313, 317, 337, 353, 373, 397, 523, 773, 797, 937, 953, 997,
                             1223, 1373, 1523, 1997, 2113, 2137]


def test_p037_trunc_left():
    assert trunc_left(10) == 0
    assert trunc_left(11) == 1
    assert trunc_left(17) == 7
    assert trunc_left(173) == 73
    assert trunc_left(1573) == 573
    assert trunc_left(1000) == 0
    assert trunc_left(1010) == 10


def test_p037_trunc_right():
    assert trunc_right(10) == 1
    assert trunc_right(11) == 1
    assert trunc_right(71) == 7
    assert trunc_right(173) == 17
    assert trunc_right(1573) == 157
    assert trunc_right(1000) == 100
    assert trunc_right(1010) == 101


def test_p037_is_both_sides_truncatable_prime():
    assert is_both_sides_truncatable_prime(11) == False  # 1 is not prime
    assert is_both_sides_truncatable_prime(23) == True  # 2 and 3 are primes
    assert is_both_sides_truncatable_prime(223) == False

    assert is_both_sides_truncatable_prime(27) == False
    assert is_both_sides_truncatable_prime(33) == False
    assert is_both_sides_truncatable_prime(37) == True
    assert is_both_sides_truncatable_prime(373) == True

    assert is_both_sides_truncatable_prime(53) == True
    assert is_both_sides_truncatable_prime(353) == False

    assert is_both_sides_truncatable_prime(3797) == True


def test_p037_build_both_sides_truncatable_primes():
    result = build_both_sides_truncatable_primes(count=11)
    for num in result:
        assert is_both_sides_truncatable_prime(num)
