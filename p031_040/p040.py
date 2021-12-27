from typing import Generator
import itertools

from util import int_to_digits, product


def p040() -> int:
    """ An irrational decimal fraction is created by concatenating the positive integers:
0.123456789101112131415161718192021...
    It can be seen that the 12th digit of the fractional part is 1.
    If dn represents the nth digit of the fractional part, find the value of the following expression.
    d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000 """

    nth_terms_to_collect = [10 ** i for i in range(0, 7)]
    limit = nth_terms_to_collect[-1]
    d_seq = itertools.islice(champernowne_generator(), limit)

    terms_collected = (dn
                       for n, dn in enumerate(d_seq, start=1)
                       if n in nth_terms_to_collect)

    return product(terms_collected)


def champernowne_generator() -> Generator[int, None, None]:
    # generate the digits of champernowne constant's fractional part as a sequence
    next_num = 1
    digits = []
    while True:
        if not digits:
            # break number to a list of digits,
            # then reverse the list and pop the digits one by one
            digits = list(int_to_digits(next_num))[::-1]
            next_num += 1
        yield digits.pop()
