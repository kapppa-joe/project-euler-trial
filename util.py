import functools
import itertools
import math
from typing import Generator, Iterable, Optional

from big_num import BigNum


def is_even(n: int) -> bool:
    return n & 1 == 0


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


def is_prime(num: int) -> bool:
    # check if a number is prime
    if num == 2:
        return True
    elif num < 2 or is_even(num):
        return False

    square_root = round(num ** 0.5)
    for i in range(3, square_root + 1, 2):
        if num % i == 0:
            return False
    return True


def prime_generator(limit: int) -> Generator[int, None, None]:
    # generate all prime numbers below the limit
    yield 2
    i = 3
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


def is_palindromic_num(input: int) -> bool:
    return is_palindromic(str(input))


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


def factorial(n: BigNum) -> BigNum:
    if n == BigNum('0'):
        return BigNum('1')
    else:
        return n * factorial(n - BigNum('1'))


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
