from util import count_digits, is_pandigital, join_nums
import itertools


def concatenated_product(num: int, req_digits: int = 9) -> int:
    """Returns the concatenated product of num and (1,2,...,n) when it reaches req_digits
    e.g. concatenated_product(192, 9) => 192384576  
    (joins 192 (=192 * 1), 384 (=192 * 2), 576 (=192 * 3)... until it reaches 9 digits)
    e.g. concatenated_product(1, 9) => 123456789
    """
    products = (num * i for i in range(1, req_digits + 1))
    concat_products = itertools.accumulate(products, func=join_nums)
    return next(filter(lambda p: count_digits(p) >= req_digits, concat_products), 0)


def p038():
    """What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
    """
    # as n > 1, so the number must not be larger than 9999, otherwise joining n = 2 will exceed 9 digits
    concatenated_products_iter = (concatenated_product(i)
                                  for i in range(10000))
    return max(p for p in concatenated_products_iter if is_pandigital(p))
