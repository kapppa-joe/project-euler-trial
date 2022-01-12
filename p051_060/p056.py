from util import int_to_digits


def digital_sum(a: int, b: int) -> int:
    return sum(int_to_digits(a ** b))


def p056(max_a: int, max_b: int) -> int:
    return max(digital_sum(a, b) for a in range(2, max_a) for b in range(2, max_b))
