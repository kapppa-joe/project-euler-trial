from typing import Generator
from util import make_prime_checker


def p058(prime_ratio_limit: float = 0.1) -> int:
    is_prime = make_prime_checker()
    spiral_nums = spiral_diagonal_generator()
    next(spiral_nums)  # throw away the initial 1

    count_primes = 0
    count_non_primes = 1  # the initial 1
    side_length = 1

    while True:
        new_primes = sum(is_prime(num) for num in next(spiral_nums))
        count_primes += new_primes
        count_non_primes += 4 - new_primes
        side_length += 2

        prime_ratio = count_primes / (count_primes + count_non_primes)
        if prime_ratio < prime_ratio_limit:
            return side_length


def spiral_diagonal_generator() -> Generator[tuple[int], None, None]:
    # generate the diagonal numbers
    curr = 1
    step = 2
    yield (curr,)  # yield the starting `1`

    while True:
        yield tuple(curr + step * i for i in range(1, 5))
        curr += step * 4
        step += 2
