from typing import Generator, Iterable

from util import factorial


def gen_permutation(input: Iterable) -> Generator[tuple, None, None]:
    # return a generator of lexicographic permutations
    pool = sorted(input)
    curr = pool[:]

    yield tuple(curr)

    while True:
        pivot = None
        for i in range(len(pool) - 1, 0, -1):
            if curr[i] > curr[i - 1]:
                pivot = i - 1
                break
        if pivot == None:
            # if can't find a pivot, it is the last permutation
            return None
        swap = pivot + 1
        for i in range(pivot + 1, len(pool)):
            if curr[swap] >= curr[i] and curr[i] > curr[pivot]:
                swap = i

        curr[swap], curr[pivot] = curr[pivot], curr[swap]
        curr = curr[:pivot + 1] + sorted(curr[pivot + 1:])
        yield tuple(curr)


factorial_memo = {}


def fac(n: int) -> int:
    return factorial(n, factorial_memo)


def nCr(n: int, r: int) -> int:
    if n < r:
        return 0
    else:
        return fac(n) // (fac(r) * fac(n - r))
