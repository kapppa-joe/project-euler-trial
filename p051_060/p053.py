from combinatory import nCr


def p053(max_n: int = 100) -> int:
    number_to_test = 1_000_000

    return sum(1
               for n in range(max_n + 1)
               for r in range(n + 1)
               if nCr(n, r) > number_to_test)
