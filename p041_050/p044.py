import itertools
from polygonal_numbers import pentagonal_number


def p044():
    """ Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:
    1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
    It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.
    Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj| is minimised; what is the value of D?
    """
    penta_nums = set()

    for i in itertools.count(1):
        p = pentagonal_number(i)
        for pj in penta_nums:
            if (p - pj) < pj and (p - pj) in penta_nums:
                pk = p - pj
                if (pj - pk) in penta_nums:
                    return pj - pk

        penta_nums.add(p)