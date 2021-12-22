from util import all_primes_below, has_even_digit, rotate_digits_iter, is_prime as prime_checker


def is_circular_prime(num: int, is_prime=prime_checker, memo=[]) -> bool:
    # check whether a prime number is a circular prime.
    # to skip redundant calculation, it does NOT check whether the num itself is prime

    # if any digit in the prime is in 2,4,6,8,0, it will rotate to an even num at some point. the only even prime is 2.
    if num != 2 and has_even_digit(num):
        return False

    for x in rotate_digits_iter(num):
        if not is_prime(x):
            return False
        elif x in memo:
            return True
    return True


def p035(limit: int = 1_000_000) -> int:
    primes = list(all_primes_below(limit))

    def is_prime(n: int):
        return n in primes

    circular_primes = []

    for prime in primes:
        if is_circular_prime(prime, is_prime, memo=circular_primes):
            circular_primes.append(prime)
    return len(circular_primes)
