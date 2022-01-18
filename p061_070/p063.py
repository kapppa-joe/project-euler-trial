import itertools
from util import count_digits


def p063():
    # considering power a^b
    # as any num a >= 10 will give a number more than b digits, so we know a < 10
    # also, we can deduce that the upper limit of b is reached when 9^b < 10^(b-1).

    upper_limit_of_power = next(b
                                for b in itertools.count(1)
                                if 9 ** b < 10 ** (b - 1))

    return sum(count_digits(a ** b) == b
               for a in range(1, 10)
               for b in range(1, upper_limit_of_power + 1))
