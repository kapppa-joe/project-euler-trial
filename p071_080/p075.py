from math import sqrt, ceil, gcd
import numpy as np
from typing import Iterable


def p075(limit_of_L: int = 1_500_000) -> int:
    return len(search_unique_L(limit_of_L))


def search_unique_L(limit_of_L: int):
    # generate primitive triples from (m, n) pairs with Euclid's formula,
    # and then use a numpy array as a count table to keep track of how many triples can be formed for every number of L
    # count_table[L] : number of triangles can be formed with this L

    count_table = np.zeros(limit_of_L, dtype=np.int32)
    m_limit = upper_limit_for_m(limit_of_L)
    for m, n in generate_m_n_pairs(m_limit):
        L = calc_L(m, n)
        count_table[::L] += 1  # add 1 for every multiple of L
    return np.where(count_table == 1)[0]


# def gen_count_table(limit_of_L: int):
#     # just for myself playing around with the nums. not used in actual solution
#     count_table = np.zeros(limit_of_L)
#     m_limit = upper_limit_for_m(limit_of_L)
#     for m, n in generate_m_n_pairs(m_limit):
#         L = calc_L(m, n)
#         count_table[::L] += 1  # add 1 for every multiple of L
#     return {i: int(count_table[i]) for i in np.where(count_table >= 1)[0]}


def generate_m_n_pairs(m_limit: int) -> Iterable[tuple[int, int]]:
    # according to a variant form of Euclid's formula,
    # every primitive Pythaogorean triple can be derive from a pair of odd numbers (m, n),
    # where m & n are coprime.

    return ((m, n) for m in range(3, m_limit, 2)
            for n in range(1, m, 2)
            if gcd(m, n) == 1)


def upper_limit_for_m(limit_of_L: int = 1_500_000) -> int:
    # as we have m^2 + mn = L, and n >= 1, we have m^2 + m <= L
    # solving quadratic formula, we get m = (-1 + sqrt(4L + 1)) / 2
    return ceil((-1 + sqrt(4 * limit_of_L + 1)) / 2)


def calc_L(m: int, n: int) -> int:
    return m * m + m * n


def brute_force_func_for_testing(limit_of_L: int):
    count_table = {}

    for b in range(4, limit_of_L // 2):
        for a in range(3, b):
            c = sqrt(a * a + b * b)
            if (a + b + c) > limit_of_L:
                break
            if int(c) == c:
                L = a + b + int(c)
                if not L in count_table:
                    count_table[L] = 0
                count_table[L] += 1
    return count_table
