from math import sqrt, floor
from util import is_odd


def p064(limit: int = 10000):
    return sum(is_odd(count_period(i)) for i in range(2, limit + 1))


def count_period(x: int) -> int:
    a0 = floor(sqrt(x))
    if a0 * a0 == x:  # perfect square
        return 0

    numer = 0
    denom = 1
    a = a0
    period = 0

    while a != 2 * a0:
        numer = denom * a - numer
        denom = (x - numer ** 2) // denom
        a = floor((a0 + numer) / denom)
        period += 1

    return period
