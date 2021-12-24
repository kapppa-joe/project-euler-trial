from util import is_palindromic_bin, is_palindromic_num


def p036(limit: int = 1_000_000) -> int:
    # Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
    return sum(num for num in range(limit) if is_palindromic_num(num) and is_palindromic_bin(num))
