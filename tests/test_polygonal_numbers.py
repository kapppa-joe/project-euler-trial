from polygonal_numbers import is_pentagonal
from random import choices


def test_is_pentagonal():
    test_cases_true = [1, 5, 12, 22, 35, 51, 70, 92, 117, 145]
    for num in test_cases_true:
        assert is_pentagonal(num) == True

    test_cases_false = [i for i in range(145) if i not in test_cases_true]
    for num in choices(test_cases_false, k=10):
        assert is_pentagonal(num) == False
