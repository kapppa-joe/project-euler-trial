import functools
from typing import Iterable


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


def fib_generator(limit: int) -> int:
    # generate a fib number seq lower than n
    a = 1
    b = 1
    while b < limit:
        (a, b) = (b, a + b)
        yield a


def all_primes_below(n: int, asc: bool = True) -> int:
    # generate all prime numbers lower than n
    # uses the old and simple SOE
    isPrime = [True for i in range(n)]
    p = 2
    while (p * p < n):
        if isPrime[p]:
            for m in range(p * 2, n, p):
                isPrime[m] = False
        p += 1
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


def prime_generator(limit: int) -> int:
    yield 2
    i = 3
    while i < limit:
        if is_prime(i):
            yield i
        i += 2


def nth_prime(n: int) -> int:
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
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a: int, b: int) -> int:
    return a * b / gcd(a, b)


def product(iter: Iterable[int]) -> int:
    # take an iterable of integers and return the product
    return functools.reduce(lambda acc, i: acc * i, iter, 1)


def str_to_digits(string: str) -> Iterable[int]:
    # take a numeric string and convert to an Iterable of each digit
    return (int(char) for char in string)
