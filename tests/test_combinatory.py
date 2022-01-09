from typing import Iterator
from combinatory import gen_permutation, nCr
import random


def test_gen_permutation():
    assert list(gen_permutation([1])) == [(1,)]
    assert list(gen_permutation([1, 2])) == [(1, 2), (2, 1)]
    assert list(gen_permutation([1, 2, 3])) == [(1, 2, 3), (1, 3, 2), (
        2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
    assert list(gen_permutation(range(1, 5))) == [(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (
        2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)]


def test_nCr():
    assert nCr(5, 3) == 10
    assert nCr(23, 10) == 1144066
