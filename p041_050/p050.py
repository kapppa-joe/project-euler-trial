import itertools
from util import all_primes_below


def p050(upper_limit: int = 1_000_000) -> int:
    """ The prime 41, can be written as the sum of six consecutive primes:
        41 = 2 + 3 + 5 + 7 + 11 + 13
    This is the longest sum of consecutive primes that adds to a prime below one-hundred.
    The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
    Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

    primes = list(all_primes_below(upper_limit))

    # sum all the primes from 2 to Nth prime, until the sum reach the upper limit.
    # now N is the longest possible terms that we can possibly have
    longest_possible_sum = itertools.takewhile(
        lambda acc: acc <= upper_limit, itertools.accumulate(primes))
    n = sum(1 for _ in longest_possible_sum)

    # traverse primes seq with sliding window of size n or below, and test if the sum is a prime within limit.
    for length in range(n, 0, -1):
        for start in range(n + 1 - length):
            sum_of_primes = sum(primes[start:start+length])
            if sum_of_primes in primes:
                return sum_of_primes

    # return 0 if no solution can be found.
    return 0
