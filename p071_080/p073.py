from farey_seq import farey_sequence_start_from_between
from p071_080.p071 import median_fraction, are_neighbours, less_than_or_equal


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


def p073(a: int, b: int, c: int, d: int, n: int) -> int:
    c0, d0 = search_right_neighbour(a, b, n)
    seq = farey_sequence_start_from_between(n, a, b, c0, d0)

    next(seq)  # remove the starting (a, b)
    count = 0

    for numer, denom in seq:
        if (numer, denom) == (c, d):
            return count
        count += 1

    raise RuntimeError
