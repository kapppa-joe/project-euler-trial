from p051_060.p051 import determine_same_digit_group, same_digit
from util import all_primes_below


def test_p051_same_digit_group():
    pool = set([1234, 1123, 1334, 4423, 1444, 1554])
    output = determine_same_digit_group(pool)
    assert output == {'**23': {1123, 4423},
                      '1**4': {1334, 1444, 1554},
                      '1***': {1444}}


def test_p051_same_digit():
    assert same_digit(1234) == set()
    assert same_digit(1223) == {'2'}
    assert same_digit(56003) == {'0'}
    assert same_digit(56006) == {'0', '6'}
