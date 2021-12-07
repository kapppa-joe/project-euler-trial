import functools
from util import all_divisors


@functools.cache
def sum_of_divisors(n: int) -> int:
    return sum(d for d in all_divisors(n) if d != n)


def have_amicable_pair(a: int) -> bool:
    b = sum_of_divisors(a)
    return a != b and sum_of_divisors(b) == a


def q021(limit: int) -> int:
    # Evaluate the sum of all the amicable numbers under 10000.
    return sum(i for i in range(limit) if have_amicable_pair(i))
