from p031 import CoinChange, DefaultCoinSet, p031
import pytest

from p033 import digit_cancelling_fractions


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
