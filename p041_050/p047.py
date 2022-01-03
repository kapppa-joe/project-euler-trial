from typing import Generator
from util import make_prime_checker
from functools import lru_cache


is_prime = make_prime_checker(1_000_000)
Primes = [i for i in range(1_000_000) if is_prime(i)]


def to_prime_factors(num: int) -> Generator[int, None, None]:
    prime_idx = 0
    test_self_is_prime = True  # test whether the number itself is prime

    while num > 1:
        if test_self_is_prime and is_prime(num):
            yield num
            return
        else:
            test_self_is_prime = False
            p = Primes[prime_idx]
            while num % p == 0:
                yield p
                num = num // p
                test_self_is_prime = True
            else:
                prime_idx += 1

    return


@lru_cache
def count_distinct_prime_factors(num: int) -> int:
    return len(set(to_prime_factors(num)))


def p047(consecutive_nums: int = 4, distinct_prime_factors: int = 4) -> int:
    """
    The first two consecutive numbers to have two distinct prime factors are:
        14 = 2 × 7
        15 = 3 × 5
    The first three consecutive numbers to have three distinct prime factors are:
        644 = 2² × 7 × 23
        645 = 3 × 5 × 43
        646 = 2 × 17 × 19.
    Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
    """
    start = 2
    while True:
        candidate = find_consecutive_non_prime(
            consecutive_nums=consecutive_nums, start=start)
        if all(count_distinct_prime_factors(candidate + i) == distinct_prime_factors
               for i in range(consecutive_nums)):
            return candidate
        else:
            start = candidate + 1


def find_consecutive_non_prime(consecutive_nums: int, start: int = 2) -> int:
    while True:
        last_prime_seen = 0
        for i in range(consecutive_nums):
            if is_prime(start + i):
                last_prime_seen = start + i
        if last_prime_seen == 0:
            return start
        else:
            start = last_prime_seen + 1
