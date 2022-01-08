def p052(num_of_multiples: int = 6) -> int:
    # It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
    # Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

    lower_bound = 10 ** (num_of_multiples - 1)
    upper_bound = 10 ** num_of_multiples // num_of_multiples

    while lower_bound < 10 ** 100:
        for num in range(lower_bound, upper_bound + 1):
            if has_n_permuted_multiples(num, num_of_multiples):
                return num

        lower_bound *= 10
        upper_bound *= 10

    return 0


def are_permutation(a: int, b: int) -> bool:
    str_a, str_b = str(a), str(b)
    if len(str_a) != len(str_b):
        return False
    return sorted(str_a) == sorted(str_b)


def has_n_permuted_multiples(num: int, n: int) -> bool:
    return all(are_permutation(num, num * i) for i in range(2, n + 1))
