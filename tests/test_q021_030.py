from constant_inputs.q022_names import Q022_names
from q021_030 import gen_abundant_number, have_amicable_pair, is_abundant_number, is_sum_of_two_elements, name_score, q021, q022, q023, q024, sum_of_divisors


def test_sum_of_divisors():
    assert sum_of_divisors(1) == 0
    assert sum_of_divisors(2) == 1
    assert sum_of_divisors(4) == 1 + 2
    assert sum_of_divisors(10) == 1 + 2 + 5
    assert sum_of_divisors(12) == 1 + 2 + 3 + 4 + 6
    assert sum_of_divisors(220) == 284
    assert sum_of_divisors(284) == 220


def test_have_amicable_pair():
    assert have_amicable_pair(1) == False
    assert have_amicable_pair(6) == False  # cannot pair with itself
    assert have_amicable_pair(220) == True
    assert have_amicable_pair(284) == True
    assert have_amicable_pair(1184) == True
    assert have_amicable_pair(1210) == True


def test_q021():
    assert q021(220) == 0
    assert q021(221) == 220
    assert q021(285) == 220 + 284
    assert q021(1211) == 220 + 284 + 1184 + 1210
    assert q021(10000) == 31626


def test_name_score():
    assert name_score("COLIN", 0) == 53
    assert name_score("cOliN", 0) == 53
    assert name_score("COLIN", 1) == 53 * 2
    assert name_score("COLIN", 937) == 49714


def test_q022():
    names = ["COLIN", "ANNA"]
    assert q022(names) == 30 + 53 * 2  # ANNA is 30, COLINA is 53

    names = ["COLIN", "DAVID"]
    assert q022(names) == 53 + 40 * 2  # DAVID is 40

    names = ["DAVID", "COLIN", "ANNA"]
    assert q022(names) == 30 + 53 * 2 + 40 * 3

    assert q022(names=Q022_names) == 871198282


def test_is_abundant_number():
    for i in range(12):
        assert is_abundant_number(i) == False
    assert is_abundant_number(12) == True
    assert is_abundant_number(17) == False
    assert is_abundant_number(18) == True
    assert is_abundant_number(20) == True
    assert is_abundant_number(24) == True
    assert is_abundant_number(36) == True


def test_gen_abundant_number():
    abundant_numbers_under_100 = list(gen_abundant_number(100))
    assert abundant_numbers_under_100 == [
        12, 18, 20, 24, 30, 36, 40, 42, 48, 54, 56, 60, 66, 70, 72, 78, 80, 84, 88, 90, 96]


def test_q023():
    assert q023(24) == sum(i for i in range(24))
    assert q023(25) == sum(i for i in range(25)) - 24
    assert q023(31) == sum(i for i in range(31)) - 24 - 30
    assert q023(60) == sum(i for i in range(60)) - 24 - 30 - 32 - \
        36 - 38 - 40 - 42 - 44 - 48 - 50 - 52 - 54 - 56 - 58
    assert q023() == 4179871


def test_q024():
    assert q024([0, 1, 2], 0) == '012'
    assert q024([0, 1, 2], 1) == '021'
    assert q024([0, 1, 2], 5) == '210'
    assert q024([0, 1, 2], 6) == ''  # only have 6 permutations
    assert q024(list(range(4)), 0) == '0123'
    assert q024(list(range(4)), 1) == '0132'
    assert q024(list(range(4)), 10) == '1302'
    # one millionth lexicographic permutation of 0..9:
    assert q024(list(range(10)), 1_000_000 - 1) == '2783915460'
