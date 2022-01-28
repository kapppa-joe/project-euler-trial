from typing import Generator
from util import gcd


def farey_sequence(n: int) -> Generator[tuple[int, int], None, None]:
    (a, b, c, d) = (0, 1, 1, n)
    yield (a, b)
    while c <= n:
        k = (n + b) // d
        (a, b, c, d) = (c, d, k * c - a, k * d - b)
        yield (a, b)


def farey_sequence_start_from_between(n: int, a: int, b: int, c: int, d: int) -> Generator[tuple[int, int], None, None]:
    yield (a, b)
    while c <= n:
        k = (n + b) // d
        (a, b, c, d) = (c, d, k * c - a, k * d - b)
        yield (a, b)


def median_fraction(n1: int, d1: int, n2: int, d2: int) -> tuple[int, int]:
    n = n1 + n2
    d = d1 + d2
    reduce_by = gcd(n, d)
    return (n // reduce_by, d // reduce_by)


def are_neighbours(a: int, b: int, c: int, d: int) -> bool:
    return b * c - a * d == 1


def less_than(a: int, b: int, c: int, d: int) -> bool:
    return a * d - b * c < 0


def less_than_or_equal(a: int, b: int, c: int, d: int) -> bool:
    return a * d - b * c <= 0


def search_right_neighbour(a0: int, b0: int, n: int) -> tuple[int, int]:
    a, b, c, d = (0, 1, 1, 1)

    while True:
        numer, denom = median_fraction(a, b, c, d)
        if less_than_or_equal(numer, denom, a0, b0):
            a, b, = numer, denom
        else:
            c, d = numer, denom

        if (a, b) == (a0, b0) and are_neighbours(a, b, c, d):
            break

    while True:
        numer, denom = median_fraction(a, b, c, d)
        if denom > n:
            return c, d
        else:
            c, d = numer, denom


def search_left_neighbour(c0: int, d0: int, n: int) -> tuple[int, int]:
    a, b, c, d = (0, 1, 1, 1)

    while True:
        numer, denom = median_fraction(a, b, c, d)
        if less_than(numer, denom, c0, d0):
            a, b, = numer, denom
        else:
            c, d = numer, denom

        if (c, d) == (c0, d0) and are_neighbours(a, b, c, d):
            break

    while True:
        numer, denom = median_fraction(a, b, c, d)
        if denom > n:
            return a, b
        else:
            a, b = numer, denom
