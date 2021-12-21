import itertools
from util import factorial, int_to_digits

fac = {}
factorial(9, fac)  # memoize !0 to !9 in dict


def digit_factorials_sum(num: int) -> int:
    # compute the sum of factorial of digits,
    # e.g. digit_factorials_sum(145) = !1 + !4 + !5 = 145

    return sum(fac[digit] for digit in int_to_digits(num))


def p034():
    """
    145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
    Find the sum of all numbers which are equal to the sum of the factorial of their digits.
    Note: As 1! = 1 and 2! = 2 are not sums they are not included.
    """

    # As 9! * 7 = 2540160 < 9999999, we can infer that any number satifiying the condition must be not more than 7 digits.
    return sum(num for num in range(10, 10**7) if num == digit_factorials_sum(num))
