from util import is_prime as check_is_prime, all_primes_below
import functools
import itertools
import math
from typing import Callable, Generator
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

    # set start = 2 because my generator starts with f1 = 1 and f2 = 2, while the question define f2 = 1 and f3 = 2
    fibs_with_index = enumerate(fib_generator(math.inf), start=2)
    while count_digits(fib) < digit_limit:
        (index, fib) = next(fibs_with_index)

    return index


def decimal_unit_fraction(deno: int) -> tuple[str, str]:
    # compute the decimal representation of a unit fraction
    # return the fraction part and recurring cycle part in tuple

    if deno <= 1:
        return ('', '')

    fraction_part = []
    numerators_seen = []
    n = 10   # n: numerator

    while n != 0 and n not in numerators_seen:
        numerators_seen.append(n)
        f = n // deno
        fraction_part.append(f)
        n = (n % deno) * 10
    recur_part = []

    if n != 0:
        start_of_recur_part = numerators_seen.index(n)
        recur_part = fraction_part[start_of_recur_part:]
    return (''.join(str(i) for i in fraction_part), ''.join(str(i) for i in recur_part))


@functools.cache
def recur_cycle_length(deno: int):
    # get the length of recur cycle part and memoize it
    fraction_part, recur_part = decimal_unit_fraction(deno)
    return len(recur_part)


def q026(limit: int) -> int:
    # Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
    return max(range(2, limit), key=recur_cycle_length)


primes = list(all_primes_below(1_000_000))


@functools.cache
def is_prime(num: int) -> bool:
    # return whether a number is prime. use primes sieve and memoization to improve efficiency
    if num in primes:
        return True
    elif num < primes[-1]:
        return False
    else:
        return check_is_prime(num)


def count_consecutive_primes(a: int, b: int) -> int:
    # count the numbers of primes generated by formula (n^2 + an + b)
    x = 0
    num = b
    while is_prime(num):
        x += 1
        num = (x ** 2 + a * x + b)

    return x


def q027(a_limit: int = 1000, b_limit: int = 1001) -> int:
    # Considering quadratics of the form:
    # n^2 + an + b, where |a| < 1000 and |b| <= 1000
    # Find the product of the coefficients, a and b , for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n == 0.

    max_nums_of_prime_so_far = 0
    best_pair_so_far = (0, 0)
    # consider case of n == 0, b must be a prime itself.
    b_candidates = list(all_primes_below(b_limit))

    for a in range(- a_limit + 1, a_limit):
        for b in b_candidates:
            # screen out candidates with some simple tests:
            if not is_prime(1 + a + b):  # case of n == 1
                continue
            elif max_nums_of_prime_so_far > 1:  # case of n == best candidate so far
                n = max_nums_of_prime_so_far
                if not is_prime(n ** 2 + a * n + b):
                    continue

            nums_of_primes = count_consecutive_primes(a, b)
            if nums_of_primes > max_nums_of_prime_so_far:
                max_nums_of_prime_so_far = nums_of_primes
                best_pair_so_far = (a, b)

    a, b = best_pair_so_far
    print(
        f"best pair: {best_pair_so_far} produces {max_nums_of_prime_so_far} primes")
    return a * b
# -61, 971 with 71 primes
