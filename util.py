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


def prime_generator(limit) -> int:
    i = 2
    while i < limit:
        if is_prime(i):
            yield i
        i += 1
