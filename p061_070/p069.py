from functools import cache
from util import all_primes_below


UpperLimit = 1_000_000

PrimeList = list(all_primes_below(UpperLimit + 1))
PrimeSet = set(PrimeList)


def p069(upper_limit: int = UpperLimit):
    return max(range(2, upper_limit + 1), key=lambda n: n / totient(n))


def totient(n: int) -> int:
    if n in PrimeSet:
        return n - 1
    else:
        product = n
        for pf in prime_factors(n):
            product *= (1 - 1/pf)
        return int(product)


@cache
def prime_factors(n: int) -> set[int]:
    if n in PrimeSet or n == 1:
        return set()

    for p in PrimeList:
        if n % p == 0:
            while n % p == 0:
                n = n // p
            if n in PrimeSet:
                return {n, p}
            else:
                return prime_factors(n) | {p}

    raise RuntimeError
