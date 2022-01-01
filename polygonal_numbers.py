from math import sqrt


def triangle_number(n: int) -> int:
    return n * (n+1) // 2


def pentagonal_number(n: int) -> int:
    return n * (3 * n - 1) // 2


def hexagonal_number(n: int) -> int:
    return n * (2 * n - 1)


def is_triangle(k: int) -> bool:
    # determine whether a number is triangle number
    x = (-1 + sqrt(1 + 8 * k)) / 2  # positive root of x^2 + x - 2k = 0
    return x == int(x)


def is_pentagonal(k: int) -> bool:
    # determine whether a number is pentagonal
    x = (1 + sqrt(1 + 24 * k)) / 6  # positive root of 3x^2 - x - 2k == 0
    return x == int(x)
