from itertools import permutations
from typing import Optional

from util import is_prime, join_nums


def find_largest_pandigital_prime(digit: int) -> Optional[int]:
    # return the largest pandigital prime made from number 1 to `digit`
    all_pandigital_nums = permutations(range(digit, 0, -1), digit)
    possible_last_digits = [d for d in (1, 3, 7, 9) if d <= digit]
    candidates = filter(
        lambda num_tuples: num_tuples[-1] in possible_last_digits, all_pandigital_nums)
    candidate_numbers = (join_nums(*num_tuples) for num_tuples in candidates)

    return next((num for num in candidate_numbers if is_prime(num)), None)


def p041():
    """ We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
    What is the largest n-digit pandigital prime that exists?  """
    candidates = (find_largest_pandigital_prime(digit)
                  for digit in range(9, 0, -1))
    return next(p for p in candidates if p != None)
