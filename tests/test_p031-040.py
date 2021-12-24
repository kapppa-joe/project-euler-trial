from p031_040.p031 import CoinChange, DefaultCoinSet, p031
import pytest

from p031_040.p033 import digit_cancelling_fractions
from p031_040.p034 import digit_factorials_sum
from p031_040.p035 import is_circular_prime, p035
from p031_040.p036 import p036


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
