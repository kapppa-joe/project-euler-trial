from util import gcd


def median_fraction(n1: int, d1: int, n2: int, d2: int) -> tuple[int, int]:
    n = n1 + n2
    d = d1 + d2
    reduce_by = gcd(n, d)
    return (n // reduce_by, d // reduce_by)


def are_neighbours(a: int, b: int, c: int, d: int) -> bool:
    return b * c - a * d == 1


def p071(numer: int = 3, denom: int = 7, target_d: int = 8) -> tuple[int, int]:
    n, d = (0, 1)

    while d + denom <= target_d:
        n, d = median_fraction(n, d, numer, denom)

    while not are_neighbours(n, d, numer, denom):
        n, d = median_fraction(n, d, numer, denom)

    return (n, d)
