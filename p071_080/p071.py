from util import gcd, reduce_fraction
from farey_seq import farey_sequence_start_from_between, median_fraction, search_left_neighbour


# def median_fraction(n1: int, d1: int, n2: int, d2: int) -> tuple[int, int]:
#     n = n1 + n2
#     d = d1 + d2
#     reduce_by = gcd(n, d)
#     return (n // reduce_by, d // reduce_by)


# def are_neighbours(a: int, b: int, c: int, d: int) -> bool:
#     return b * c - a * d == 1


# def less_than(a: int, b: int, c: int, d: int) -> bool:
#     return a * d - b * c < 0


# def less_than_or_equal(a: int, b: int, c: int, d: int) -> bool:
#     return a * d - b * c <= 0


def p071(numer: int = 3, denom: int = 7, target_d: int = 1_000_000) -> tuple[int, int]:
    return search_left_neighbour(numer, denom, target_d)


# def p071(numer: int = 3, denom: int = 7, target_d: int = 8) -> tuple[int, int]:
#     n, d = (0, 1)

#     while d + denom <= target_d:
#         n, d = median_fraction(n, d, numer, denom)

#     while not are_neighbours(n, d, numer, denom):
#         n, d = median_fraction(n, d, numer, denom)

#     return (n, d)


# def p071_another(numer: int = 3, denom: int = 7, target_d: int = 8) -> tuple[int, int]:
#     a, b = reduce_fraction(numer * target_d // denom - 1, target_d)
#     c, d = median_fraction(a, b, numer, denom)
#     while True:
#         c1, d1 = median_fraction(a, b, c, d)
#         if d1 > denom and are_neighbours(a, b, c, d):
#             break
#         else:
#             c, d = c1, d1

#     seq = farey_sequence_start_from_between(target_d, a, b, c, d)
#     prev_n, prev_d = 0, 0
#     for (n, d) in seq:
#         if (n, d) == (numer, denom):
#             return (prev_n, prev_d)
#         else:
#             (prev_n, prev_d) = (n, d)

#     raise RuntimeError
