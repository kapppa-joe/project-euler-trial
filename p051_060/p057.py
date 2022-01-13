import functools

from util import count_digits


@functools.lru_cache
def fraction_seq(n: int) -> tuple[int, int]:
    # return the numerator and denominator of the nth iteration for sqrt(2)
    if n == 0:
        return (1, 1)
    else:
        (numer, denom) = fraction_seq(n - 1)
        return (denom * 2 + numer, numer + denom)


def p057(limit: int = 1000) -> int:
    fraction_expansions = (fraction_seq(i) for i in range(1, limit + 1))
    return sum(count_digits(numer) > count_digits(denom) for (numer, denom) in fraction_expansions)
