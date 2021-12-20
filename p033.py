from util import gcd, product


def digit_cancelling_fractions(a, b) -> bool:
    """
    check whether the fraction a / b can be written as digit cancelling fraction.
    """
    if (a >= b):
        return False

    for c in range(1, 10):
        for numer in (a * 10 + c, c * 10 + a):
            for denom in (b * 10 + c, c * 10 + b):
                if numer / denom == a / b:
                    return True

    return False


def p033():
    """ The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
    We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
    There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
    If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
    """

    numers = []
    denoms = []
    for (a, b) in ((a, b) for a in range(1, 10) for b in range(a + 1, 10)):
        if digit_cancelling_fractions(a, b):
            numers.append(a)
            denoms.append(b)

    numer, denom = product(numers), product(denoms)
    cancelling_factor = gcd(numer, denom)
    return denom // cancelling_factor
