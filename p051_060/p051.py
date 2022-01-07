from typing import Iterable
from util import all_primes_below


def p051():
    Primes = set(all_primes_below(1_000_000))
    prime_value_families = determine_same_digit_group(Primes)
    eight_prime_value_families = [
        family for family in prime_value_families.values() if len(family) == 8]

    return min(prime for family in eight_prime_value_families for prime in family)


def same_digit(num: int) -> Iterable[str]:
    # return a iterable of digits which appears more than once in the number
    num_str = str(num)
    return {d for d in num_str if num_str.count(d) > 1}


def determine_same_digit_group(pool: set[int]) -> dict[str, set[int]]:
    """traverse a set of numbers, and group the numbers in families which can be made by replacing part of the number with the same digit
    example:
    input: set([1234, 1123, 1334, 4423, 1444, 1554])
    output: {'**23': {1123, 4423}, '1**4': {1334, 1444, 1554}, '1***': {1444}}
    """
    same_digit_groups = {}

    for num in pool:
        for digit in same_digit(num):
            group_key = str(num).replace(digit, '*')
            if group_key in same_digit_groups:
                continue
            else:
                same_digit_groups[group_key] = set([num])

            for digit_to_replace in '0123456789':
                if digit == digit_to_replace:
                    continue
                else:
                    replaced_num_str = str(num).replace(
                        digit, digit_to_replace)
                    if replaced_num_str[0] == '0':
                        continue
                    elif int(replaced_num_str) in pool:
                        same_digit_groups[group_key].add(int(replaced_num_str))

    return same_digit_groups
