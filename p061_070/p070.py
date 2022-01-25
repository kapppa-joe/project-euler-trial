import itertools
from math import sqrt
from util import is_permutation_of_num, all_primes_below


def p070(upper_limit: int = 10_000_000):
    primes_search_upper_limit = upper_limit if upper_limit < 10 ** 6 else upper_limit // 1009

    primes = list(all_primes_below(primes_search_upper_limit))
    smaller_prime = list(itertools.takewhile(
        lambda p: p < sqrt(upper_limit), primes))
    prime_pairs = ((a, b)
                   for a in smaller_prime
                   for b in primes
                   if a < b
                   and (a * b) < upper_limit)

    candidate = None
    curr_minimum = float('inf')

    for (a, b) in prime_pairs:
        n = a * b
        totient_n = (a-1) * (b-1)
        ratio = n / totient_n
        if ratio >= curr_minimum:
            continue

        if is_permutation_of_num(n, totient_n):
            candidate = n
            curr_minimum = ratio

    return candidate
