from math import sqrt, floor
from typing import Generator
import itertools

from p061_070.p065 import expand_inf_fraction


SquaresBelow10000 = set((i ** 2 for i in range(101)))


def p066(upper_limit: int = 1000) -> int:
    square_numbers = set(
        (i ** 2 for i in range(1, floor(sqrt(upper_limit) + 2))))

    return max((D for D in range(1, upper_limit + 1) if not D in square_numbers),
               key=pells_equation_minimal_x)


def sqrt_continued_fraction(x: int) -> Generator[int, None, None]:
    a0 = floor(sqrt(x))
    if a0 * a0 == x:  # perfect square
        yield a0
        return

    numer = 0
    denom = 1
    a = a0
    repeat_part = []

    yield a0

    while a != 2 * a0:
        numer = denom * a - numer
        denom = (x - numer ** 2) // denom
        a = floor((a0 + numer) / denom)
        repeat_part.append(a)

    yield from itertools.cycle(repeat_part)


def pells_equation_minimal_x(D: int) -> int:
    cont_frac_for_sqrt_D = expand_inf_fraction(sqrt_continued_fraction(D))
    for numer, denom in cont_frac_for_sqrt_D:
        if is_pells_equation_solution_triplet(D, numer, denom):
            return numer

    raise RuntimeError


def is_pells_equation_solution_triplet(D, x, y):
    return x * x - D * y * y == 1
