from p051_060.p051 import determine_same_digit_group, same_digit
from p051_060.p052 import are_permutation, has_n_permuted_multiples
from p051_060.p053 import p053


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


def test_p052_are_permutation():
    assert are_permutation(1, 2) == False
    assert are_permutation(12, 21) == True
    assert are_permutation(1223, 1332) == False
    assert are_permutation(1223, 1232) == True
    assert are_permutation(12340, 4321) == False
    assert are_permutation(125874, 251748) == True


def test_p052_has_n_permuted_multiples():
    assert has_n_permuted_multiples(125874, 2) == True


def test_p053():
    assert p053(22) == 0
    assert p053(23) == 4
