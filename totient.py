from util import all_primes_below, gcd
from functools import cache
from typing import Generator


def phi(num: int) -> int:
    if num < 2:
        return 1
    return sum(gcd(num, i) == 1 for i in range(1, num))


class Totients:
    def __init__(self, upper_limit=1_000_000) -> None:
        self.upper_limit = upper_limit
        self.Primes = {p: None for p in all_primes_below(upper_limit + 1)}

    def n_over_totient_n(self, n: int) -> float:
        if n in self.Primes:
            return n / (n-1)
        else:
            product = 1
            for pf in self.prime_factors(n):
                product *= self.n_over_totient_n(pf)
            return product

    def summation_totient(self, n: int) -> int:
        return sum(self.totient(i) for i in range(1, n + 1))

    @cache
    def totient(self, n: int) -> int:
        if n in self.Primes:
            return n - 1
        else:
            product = n
            for pf in self.prime_factors(n):
                product *= (1 - 1/pf)
            return int(product)

    @cache
    def prime_factors(self, n: int) -> set[int]:
        if n in self.Primes or n == 1:
            return set()

        for p in self.Primes:
            if n % p == 0:
                while n % p == 0:
                    n = n // p
                if n in self.Primes:
                    return {n, p}
                else:
                    return self.prime_factors(n) | {p}

        raise RuntimeError


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
