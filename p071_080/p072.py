from totient import Totients


def p072(d: int) -> int:
    T = Totients(d)
    # the question does not count 0/1 and 1/1, so it is totient summation - 1
    return T.summation_totient(d) - 1
