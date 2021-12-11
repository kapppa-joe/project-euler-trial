import functools
import itertools
import math
from typing import Generator
from combinatory import gen_permutation
from constant_inputs.q022_names import Q022_names
from sort import quicksort
from util import all_divisors, count_digits, fib_generator, nth


@functools.cache
def sum_of_divisors(n: int) -> int:
    return sum(d for d in all_divisors(n) if d != n)


def have_amicable_pair(a: int) -> bool:
    b = sum_of_divisors(a)
    return a != b and sum_of_divisors(b) == a


def q021(limit: int) -> int:
    # Evaluate the sum of all the amicable numbers under 10000.
    return sum(i for i in range(limit) if have_amicable_pair(i))


def name_score(name: str, order: int = 0) -> int:
    score = sum(ord(char) - 96 for char in name.lower())
    return score * (order + 1)


def q022(names: list[str] = Q022_names) -> int:
    # Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
    # For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
    # What is the total of all the name scores in the file?
    sorted_names = quicksort(names)

    return sum(name_score(name, i) for (i, name) in enumerate(sorted_names))


def is_abundant_number(n: int) -> bool:
    proper_divisors = (d for d in all_divisors(n) if d != n)
    return sum(proper_divisors) > n


def gen_abundant_number(limit: int) -> Generator[int, None, None]:
    i = 12
    while i < limit:
        if is_abundant_number(i):
            yield i
        i += 1


def is_sum_of_two_elements(n: int, num_list: list[int]) -> bool:
    # input number n and a sorted list
    # traverse all nums below n / 2 and check if it can be written as sum of two elements
    for a in num_list:
        if (n - a) in num_list:
            return True
        elif 2 * a > n:
            return False
    return False


def q023(limit: int = 28123) -> int:
    """
    Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
    ( it is given that the greatest number that cannot be expressed as the sum of two abundant numbers is less than 28123. )
    """

    is_sum_of_two_abundant_nums = [False for i in range(limit)]
    abundant_nums = list(itertools.takewhile(
        lambda x: x < limit, gen_abundant_number(limit)))

    # traverse all abundant nums a, b and mark a + b as True
    for i in range(len(abundant_nums)):
        if abundant_nums[i] * 2 > limit:
            break  # return early when the smaller num is over half of upper limit
        for j in range(i, len(abundant_nums)):
            a, b = abundant_nums[i], abundant_nums[j]
            if a + b < limit:
                is_sum_of_two_abundant_nums[a + b] = True
    return sum(i for i in range(limit) if not is_sum_of_two_abundant_nums[i])


def q024(input: list[int], n: int) -> str:
    # What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
    g = gen_permutation(input)
    nth_permutation = nth(g, n)
    if nth_permutation:
        return ''.join(str(i) for i in nth_permutation)
    else:
        return ''


def q025(digit_limit: int = 1000) -> int:
    # What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

    index = 1
    fib = 1

    # use start = 2 because this generator defines f0 and f1 to be 1
    fibs_with_index = enumerate(fib_generator(math.inf), start=2)
    while count_digits(fib) < digit_limit:
        (index, fib) = next(fibs_with_index)

    return index
