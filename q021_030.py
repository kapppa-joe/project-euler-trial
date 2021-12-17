from util import int_to_digits, is_prime as check_is_prime, all_primes_below
import functools
import itertools
import math
from typing import Generator, Tuple, Dict
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
            elif max_nums_of_prime_so_far > 1:
                # case of n == largest consec primes so far.
                # if this pair of a, b cannot make a prime with current highest n,
                # than no need to check the cases of x = 1 .. n - 1.
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


def q028(size: int) -> int:
    '''Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13
    It can be verified that the sum of the numbers on the diagonals is 101.
    What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
    '''

    def spiral_diagonal_num_generator():
        # generate a seq of the numbers on the diagonals of the number spiral
        x = 1
        count = 0
        step = 2
        while True:
            yield x
            x += step
            count += 1
            if count % 4 == 0:
                step += 2

    if size < 1 or size % 2 == 0:
        raise ValueError(
            'the question s not well defined for negative size or even size')

    final_number = size ** 2
    numbers_on_diagonals = itertools.takewhile(
        lambda x: x <= final_number, spiral_diagonal_num_generator())

    return sum(numbers_on_diagonals)


def q029(a_limit, b_limit: int) -> int:
    # How many distinct terms are in the sequence generated by ab for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?
    """
    could be done by a one-liner: len(set(a ** b for a in range(2, a_limit + 1) for b in range(2, b_limit +1))). Below is an alternative solution that should work in languages without `long` type.
    """

    # record a number as a power of smaller num, e.g. 4 => (2, 2), 8 => (2, 4)
    power_of_smaller_num: Dict[int, Tuple[int, int]] = {}

    for a in range(2, a_limit + 1):
        for b in range(2, b_limit + 1):
            if a ** b <= a_limit and not a in power_of_smaller_num:
                power_of_smaller_num[a ** b] = (a, b)
            else:
                break

    # use sets to count the representation a^b, where a are not power of smaller nums.
    count_powers = {a: set(range(2, b_limit + 1))
                    for a in range(2, a_limit + 1)
                    if a not in power_of_smaller_num}

    for (a0, b0) in power_of_smaller_num.values():
        for b in range(2, b_limit + 1):
            # for a^b where a can be written as a0^b0, save them as a0^(b0*b).
            # use set to count distinct terms
            count_powers[a0].add(b0 * b)

    return sum(len(powers) for powers in count_powers.values())


def digit_n_power_sum(number: int, n: int) -> int:
    return sum(digit ** n for digit in int_to_digits(number))


def q030(power: int) -> int:
    # Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

    if power < 2:
        return 0

    # compute a upper limit of number that can possibly be made by summing n power of digits
    # for example, 9**4 * 6 is smaller than the smallest 6 digit num 100000,
    # so we can know that any candidate number for the case of power = 4 must be less than 6 digits
    digits_upper_limit = 0
    while 9 ** power * (digits_upper_limit + 1) > 10 ** digits_upper_limit:
        digits_upper_limit += 1

    return sum(num for num in range(10, 10 ** digits_upper_limit) if digit_n_power_sum(num, power) == num)
