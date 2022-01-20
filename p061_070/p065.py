from typing import Iterator
import itertools

from util import int_to_digits, nth


def p065(n: int = 100) -> int:
    expand_e_terms = expand_inf_fraction(e_a_terms())
    # input n - 1 as my nth function use 0-base index
    nth_term_of_e_convergence = nth(expand_e_terms, n - 1)

    numer, denom = nth_term_of_e_convergence
    print(f'the {n}th term of convergence for e is {numer}/{denom}')
    numer = nth_term_of_e_convergence[0]
    return sum(digit for digit in int_to_digits(numer))


def sqrt_2_a_terms() -> Iterator[int]:
    # return an iterator of [1, 2, 2, 2, ...]
    yield 1
    yield from itertools.repeat(2)


def e_a_terms() -> Iterator[int]:
    # return an iterator of [1, 2, 1, 4, 1, 1, 6, 1, 1, 8, 1, 1 ...]
    k = 1
    yield from (2, 1)
    while True:
        yield from (2 * k, 1, 1)
        k += 1


def expand_inf_fraction(a_terms: Iterator[int]) -> Iterator[tuple[int, int]]:
    # take an iterator of a terms for a infinite continued fraction,
    # repeatedly yield the next convergence fraction
    prev_numer = 1
    prev_denom = 0

    a = next(a_terms)
    numer = a
    denom = 1
    yield (numer, denom)

    for a in a_terms:
        numer, prev_numer = numer * a + prev_numer, numer
        denom, prev_denom = denom * a + prev_denom, denom
        yield (numer, denom)
