from functools import cache
from util import reverse_digits

MaxIteration = 50


def p055(limit: int = 10000):
    seeds = (num for num in range(limit))

    lychrel, non_lychrel = set(), set()
    for seed in seeds:
        if check_lychrel(seed, lychrel_memo=lychrel, non_lychrel_memo=non_lychrel):
            lychrel.add(seed)
        else:
            non_lychrel.add(seed)

    return sum(1 for num in lychrel if num < limit)


def check_lychrel(seed: int, lychrel_memo: set[int] = set(), non_lychrel_memo: set[int] = set()) -> bool:
    if seed in lychrel_memo:
        return True
    elif seed in non_lychrel_memo:
        return False

    stack = set()
    curr = seed
    while len(stack) < MaxIteration:
        stack.add(curr)
        curr = reverse_add(curr)

        if is_palindromic(curr) or curr in non_lychrel_memo:
            # arrived at a palindromic num, so we know all precursors are non-lychrel
            non_lychrel_memo.update(stack)
            return False
        elif curr in lychrel_memo:
            lychrel_memo.update(stack)
            return True
    # when the stack was filled with 50 precursors, return it as lychrel.
    return True


@cache
def reverse(num: int) -> int:
    return reverse_digits(num)


def reverse_add(num: int) -> int:
    return num + reverse(num)


def is_palindromic(num: int) -> int:
    return num == reverse(num)
