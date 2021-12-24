from math import log10, floor
from itertools import cycle
import functools
from typing import Callable, Generator

from util import is_prime


def join_nums(*num_list: int) -> int:
    return int(''.join(str(num) for num in num_list))


def build_ltr(prime_checker: Callable[[int], bool]) -> Generator[int, None, None]:
    # build primes which are truncatable left to right
    # here, it does NOT care if the number is truncatable right to left or not
    seeds = [7, 5, 3, 2]
    next_round_seeds = []
    digits_to_add = [1, 3, 7, 9]

    while seeds or next_round_seeds:
        if not seeds:
            seeds = list(reversed(next_round_seeds))
            next_round_seeds = []

        seed = seeds.pop()
        for digit in digits_to_add:
            next_candidate = join_nums(seed, digit)
            if prime_checker(next_candidate):
                next_round_seeds.append(next_candidate)
                yield next_candidate


def build_rtl(prime_checker: Callable[[int], bool]) -> Generator[int, None, None]:
    # build primes which are truncatable right to left
    seeds = [3, 7]
    next_round_seeds = []
    digits_to_add = [1, 2, 3, 5, 7, 9]

    while seeds:
        for digit in digits_to_add:
            for seed in seeds:
                next_candidate = join_nums(digit, seed)
                if prime_checker(next_candidate):
                    next_round_seeds.append(next_candidate)
                    yield next_candidate
        seeds = next_round_seeds
        next_round_seeds = []


def build_both_sides_truncatable_primes(count: int = 11) -> list[int]:
    # build truncatable primes from left to right and vice versa,
    # and then return the intersection of both sets

    @functools.cache
    def prime_checker(num):
        return is_prime(num)

    generators = [build_ltr(prime_checker), build_rtl(prime_checker)]
    prev_nums = [next(generators[0]), next(generators[1])]
    sets = [set([prev_nums[0]]), set([prev_nums[1]])]

    while True:
        generator_to_pop = 0 if prev_nums[0] < prev_nums[1] else 1
        prev_nums[generator_to_pop] = next(
            generators[generator_to_pop])
        sets[generator_to_pop].add(prev_nums[generator_to_pop])

        result = sets[0].intersection(sets[1])

        if len(result) >= count:
            return sorted(result)


def p037():
    '''
    The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
    Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
    '''

    return sum(build_both_sides_truncatable_primes(count=11))


#################################################
# below are utility functions to be used in test.


def trunc_left(num: int) -> int:
    if num < 10:
        raise ValueError('cannot truncate single digit')
    else:
        ten_power = floor(log10(num))
        return num % 10 ** ten_power


def trunc_right(num: int) -> int:
    if num < 10:
        raise ValueError('cannot truncate single digit')
    else:
        return num // 10


def is_truncatable(num: int, direction: str = 'ltr') -> bool:
    if num < 10 or not is_prime(num):
        return False

    if direction == 'ltr':
        truncated_num = trunc_left(num)
    else:
        truncated_num = trunc_right(num)

    if num < 100:
        return is_prime(truncated_num)
    else:
        return is_truncatable(truncated_num, direction)


def is_both_sides_truncatable_prime(num: int) -> bool:
    if num < 10 or not is_prime(num):
        return False
    else:
        return is_truncatable(num, 'ltr') and is_truncatable(num, 'rtl')
