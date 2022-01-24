from functools import cache
from util import all_primes_below


UpperLimit = 1_000_000

Primes = {p: None for p in all_primes_below(UpperLimit + 1)}


def p069(upper_limit: int = UpperLimit):
    return max(range(2, upper_limit + 1), key=n_over_totient_n)


def n_over_totient_n(n: int) -> float:
    if n in Primes:
        return n / (n-1)
    else:
        product = 1
        for pf in prime_factors(n):
            product *= n_over_totient_n(pf)
        return product


def totient(n: int) -> int:
    if n in Primes:
        return n - 1
    else:
        product = n
        for pf in prime_factors(n):
            product *= (1 - 1/pf)
        return int(product)


@cache
def prime_factors(n: int) -> set[int]:
    if n in Primes or n == 1:
        return set()

    for p in Primes:
        if n % p == 0:
            while n % p == 0:
                n = n // p
            if n in Primes:
                return {n, p}
            else:
                return prime_factors(n) | {p}

    raise RuntimeError
