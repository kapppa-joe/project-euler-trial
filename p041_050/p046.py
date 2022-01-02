from typing import Generator
from util import make_prime_checker
from math import ceil


is_prime = make_prime_checker()


def square_nums(upper_limit: int) -> Generator[int, None, None]:
    upper_limit_i = ceil(upper_limit ** 0.5)
    return (i ** 2 for i in range(1, upper_limit_i))


def odd_composite_nums(is_prime=is_prime) -> Generator[int, None, None]:
    num = 9
    while True:
        if not is_prime(num):
            yield num
        num += 2


def is_sum_of_prime_and_twice_a_square(num: int) -> bool:
    possible_square_nums = square_nums(num // 2)
    return any(is_prime(num - sq_num * 2)
               for sq_num in possible_square_nums)


def p046():
    """
    What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
    """
    return next(num
                for num in odd_composite_nums()
                if not is_sum_of_prime_and_twice_a_square(num))
