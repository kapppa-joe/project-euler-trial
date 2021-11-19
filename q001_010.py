def q001(a: int, b: int, limit: int) -> int:
    if (a <= 0 or b <= 0 or limit <= 0):
        return 0
    return sum(i for i in range(limit) if i % a == 0 or i % b == 0)


def nth_fib(n: int) -> int:
    # util function to calculate nth fib number with memoization
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
    # util function for generating fib number seq lower than n
    a = 1
    b = 1
    while b < limit:
        (a, b) = (b, a + b)
        yield a


def q002(limit: int) -> int:
    return sum(num for num in fib_generator(limit) if num % 2 == 0)
