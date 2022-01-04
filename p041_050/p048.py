def p048(upper_limit: int = 1000, digits_to_keep: int = 10) -> int:
    """
    The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.
    Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.
    """
    sum_of_powers = sum(power_last_digits(i, i, digits_to_keep=digits_to_keep)
                        for i in range(1, upper_limit + 1))
    return sum_of_powers % 10 ** digits_to_keep


def power_last_digits(num: int, power: int, acc: int = 1, digits_to_keep: int = 10) -> int:
    # power function which only keeps the last n digits
    if power == 1:
        return multiply_keep_last_digits(num, acc, digits_to_keep)
    elif power % 2 == 0:
        new_num = multiply_keep_last_digits(num, num, digits_to_keep)
        return power_last_digits(new_num, power // 2, acc, digits_to_keep)
    else:
        new_acc = multiply_keep_last_digits(num, acc, digits_to_keep)
        return power_last_digits(num, power - 1, new_acc, digits_to_keep)


def multiply_keep_last_digits(a: int, b: int, digits_to_keep: int = 10) -> int:
    sieve = 10 ** digits_to_keep
    a = a % sieve
    b = b % sieve
    return a * b % sieve
