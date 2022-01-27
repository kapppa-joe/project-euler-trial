import functools
import itertools
import math
from re import A
from typing import Generator, Iterable, Optional

from big_num import BigNum


def is_even(n: int) -> bool:
    return n & 1 == 0


def is_odd(n: int) -> bool:
    return n & 1 == 1


def nth_fib(n: int) -> int:
    # calculate the nth fib number with memoization
    fib_memo = {1: 1, 2: 2}

    def fib(i: int) -> int:
        if i < 1:
            return 0
        elif i in fib_memo:
            return fib_memo[i]
        else:
            result = fib(i - 2) + fib(i - 1)
            fib_memo[i] = result
            return result

    return fib(n)


def fib_generator(limit: float) -> Iterable[int]:
    # generate a fib number seq lower than n
    a = 1
    b = 1
    while b < limit:
        (a, b) = (b, a + b)
        yield a


def all_primes_below(n: int, asc: bool = True) -> Iterable[int]:
    # generate all prime numbers lower than n
    # use the old and simple SOE
    isPrime = [True for _ in range(n)]

    p = 2
    for m in range(p * 2, n, p):
        isPrime[m] = False

    p = 3
    while (p * p < n):
        if isPrime[p]:
            for m in range(p * 2, n, p):
                isPrime[m] = False
        p += 2

    if asc:
        return (i for i in range(2, n) if isPrime[i])
    else:
        return (i for i in range(n - 1, 1, -1) if isPrime[i])


def is_prime(num: int, known_prime: list[int] = []) -> bool:
    # check if a number is prime
    if num == 2:
        return True
    elif num < 2 or is_even(num):
        return False

    square_root = round(num ** 0.5)
    if known_prime:
        factors_to_try = (p for p in known_prime if p <= square_root)
    else:
        factors_to_try = range(3, square_root + 1, 2)

    for i in factors_to_try:
        if num % i == 0:
            return False
    return True


def prime_generator(start: int = 2, limit: int | float = float('inf'), prime_checker=None) -> Generator[int, None, None]:
    # generate all prime numbers below the limit
    if start == 2:
        yield 2
    i = start if start % 2 == 1 else start + 1
    prime_checker = prime_checker or is_prime

    while i < limit:
        if is_prime(i):
            yield i
        i += 2


def nth_prime(n: int) -> Optional[int]:
    if n < 1:
        return None
    elif n == 1:
        return 2
    else:
        p = 3
        while n > 1:
            if is_prime(p):
                n -= 1
                if n == 1:
                    return p
            p += 2


def is_palindromic(string: str) -> bool:
    if len(string) <= 1:
        return True
    else:
        return (string[0] == string[-1]) and is_palindromic(string[1:-1])


# def is_palindromic_num(input: int) -> bool:
    # return is_palindromic(str(input))


def is_palindromic_bin(input: int) -> bool:
    # check whether a number is palindromic in its binary representation
    return is_palindromic(bin(input)[2:])


def gcd(a: int, b: int) -> int:
    # compute the greatest common divisor of two ints
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a: int, b: int) -> int:
    # compute the least common factor of two ints
    return int(a * b / gcd(a, b))


def product(iter: Iterable[int]) -> int:
    # take an iterable of integers and return the product
    return functools.reduce(lambda acc, i: acc * i, iter, 1)


def str_to_digits(string: str) -> Iterable[int]:
    # take a numeric string and convert to an Iterable of each digit
    return (int(char) for char in string)


def int_to_digits(num: int) -> Iterable[int]:
    # take an integer and convert to an Iterable of each digit
    return str_to_digits(str(num))


def triangle_number_generator() -> Generator[int, None, None]:
    # return a generator for triangle numbers
    t = 1
    k = 1
    while True:
        yield t
        k += 1
        t += k


def all_divisors(n: int) -> list[int]:
    sqrt = math.ceil(n ** 0.5)
    first_half = [i for i in range(1, sqrt + 1) if n % i == 0]
    second_half = [n // i for i in first_half[::-1]
                   if n // i not in first_half]
    return first_half + second_half


def bignum_factorial(n: BigNum) -> BigNum:
    if n == BigNum('0'):
        return BigNum('1')
    else:
        return n * bignum_factorial(n - BigNum('1'))


def is_sum_of_two_elements(n: int, num_list: list[int]) -> bool:
    # input number n and a sorted list
    # traverse all nums below n / 2 and check if it can be written as sum of two elements
    for a in num_list:
        if (n - a) in num_list:
            return True
        elif 2 * a > n:
            return False
    return False


def nth(iter: Iterable, n: int, default=None):
    # return the nth elem of an iterable
    return next(itertools.islice(iter, n, None), default)


def count_digits(n: int) -> int:
    # return the number of digits in an integer
    count = 1
    while n >= 10 or n <= -10:
        n = n // 10
        count += 1
    return count


def is_pandigital(num: int, start: int = 1, stop: int = 9) -> bool:
    # determine where a number is a pandigital num
    str_num = str(num)
    if len(str_num) != stop - start + 1:
        return False
    else:
        return all(str(digit) in str_num for digit in range(start, stop + 1))


def pandigital_generator(start_digit: int = 1, stop_digit: int = 9) -> Generator[int, None, None]:
    # return a generator for pandigital numbers in asc order

    if stop_digit < start_digit:
        yield from ()
    else:
        permutations = itertools.permutations(
            range(start_digit, stop_digit + 1))
        for p in permutations:
            num = 0
            for digit in p:
                num = num * 10 + digit
            yield num


def factorial(n: int, memo: dict[int, int] = {}) -> int:
    if n >= 0:
        if n in memo:
            return memo[n]
        elif n == 0:
            memo[0] = 1
            return 1
        else:
            result = n * factorial(n - 1, memo)
            memo[n] = result
            return result
    else:
        return 0


def rotate_digits(num: int, i: int) -> int:
    # rotate the digits of a number to left or right
    num_str = str(num)
    i = i % len(num_str)
    return int(num_str[-i:] + num_str[:-i])


def rotate_digits_iter(num: int) -> Generator[int, None, None]:
    # return a generator of numbers made by digits rotation.
    num_str = str(num)
    for i in range(1, len(num_str)):
        yield int(num_str[-i:] + num_str[:-i])


def has_even_digit(num: int) -> bool:
    # check whether a number contains a even digit (0,2,4,6,8)
    return any(digit in "02468" for digit in str(num))


def join_nums(*num_list: int) -> int:
    """Join the given numbers and return it as a new number 
    """
    # join_nums(1,2,3,4) ==> 1234
    return int(''.join(str(num) for num in num_list))


def first_true(iterable, default=False, pred=None):
    """Returns the first true value in the iterable.
    If no true value is found, returns *default*
    If *pred* is not None, returns the first item
    for which pred(item) is true.
    """
    # first_true([a,b,c], x) --> a or b or c or x
    # first_true([a,b], x, f) --> a if f(a) else b if f(b) else x
    return next(filter(pred, iterable), default)


def make_prime_checker(memo_num: int = 1_000_000):
    # a prime checker with memoization feature and can extend the memo upper limit
    # for over 1_000_000,
    primes = set(all_primes_below(memo_num))
    not_primes = set()
    upper_limit = memo_num

    def prime_checker(num: int) -> bool:
        nonlocal upper_limit
        if num in primes:
            return True
        elif num in not_primes or num < upper_limit:
            return False
        else:
            result = is_prime(num)
            if result:
                primes.add(num)
            else:
                not_primes.add(num)
            return result
    return prime_checker


def reverse_digits(num: int, base: int = 10) -> int:
    result = 0
    while num > 0:
        result = result * base + num % base
        num //= base
    return result


def is_palindromic_num(num, base: int = 10) -> int:
    return num == reverse_digits(num, base=base)


def is_permutation_of_num(a: int, b: int) -> bool:
    return sorted(str(a)) == sorted(str(b))


def reduce_fraction(n: int, d: int) -> tuple[int, int]:
    hcf = gcd(n, d)
    if hcf == 1:
        return (n, d)
    else:
        return (n // hcf, d // hcf)
