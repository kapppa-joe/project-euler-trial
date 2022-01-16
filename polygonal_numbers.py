from math import sqrt
import itertools
from typing import Generator


def triangle_number(n: int) -> int:
    return n * (n+1) // 2


def square_number(n: int) -> int:
    return n * n


def pentagonal_number(n: int) -> int:
    return n * (3 * n - 1) // 2


def hexagonal_number(n: int) -> int:
    return n * (2 * n - 1)


def heptagonal_number(n: int) -> int:
    return n * (5 * n - 3) // 2


def octagonal_number(n: int) -> int:
    return n * (3 * n - 2)


# 3n2 - 2n - k == 0   (2 + sqrt(4 + 12k)) / 6


def polygonal_number_generator(n: int, start: int = 1) -> Generator[int, None, None]:
    func = None
    match n:
        case 3:
            func = triangle_number
        case 4:
            func = square_number
        case 5:
            func = pentagonal_number
        case 6:
            func = hexagonal_number
        case 7:
            func = heptagonal_number
        case 8:
            func = octagonal_number
        case _:
            raise NotImplemented
    yield from (func(i) for i in itertools.count(start))


def is_triangle(k: int) -> bool:
    # determine whether a number is triangle number
    x = (-1 + sqrt(1 + 8 * k)) / 2  # positive root of x^2 + x - 2k = 0
    return x == int(x)


def is_pentagonal(k: int) -> bool:
    # determine whether a number is pentagonal
    x = (1 + sqrt(1 + 24 * k)) / 6  # positive root of 3x^2 - x - 2k == 0
    return x == int(x)


def rev_triangle(k: int) -> float:
    return (-1 + sqrt(1 + 8 * k)) / 2


def rev_square(k: int) -> float:
    return sqrt(k)


def rev_pentagonal(k: int) -> float:
    return (1 + sqrt(1 + 24 * k)) / 6


def rev_hexagonal(k: int) -> float:
    # -b + sqrt(b^2 -4ac)   / 2a
    # 2n^2 - n - k == 0
    return (1 + sqrt(1 + 8 * k)) / 4


def rev_heptagonal(k: int) -> float:
    # 5n^2 - 3n - 2k == 0
    # (3 + sqrt(9 + 40k)) / 10
    return (3 + sqrt(9 + 40 * k)) / 10


def rev_octagonal(k: int) -> float:
    return (2 + sqrt(4 + 12 * k)) / 6
