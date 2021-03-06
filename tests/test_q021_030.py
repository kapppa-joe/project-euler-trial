from constant_inputs.q022_names import Q022_names
from q021_030 import count_consecutive_primes, decimal_unit_fraction, digit_n_power_sum, gen_abundant_number, have_amicable_pair, is_abundant_number, is_prime, name_score, q021, q022, q023, q024, q025, q026, q027, q028, q029, q030, recur_cycle_length, sum_of_divisors


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


def test_q025():
    assert q025(1) == 1
    assert q025(2) == 7
    assert q025(3) == 12
    assert q025(4) == 17
    assert q025(5) == 21
    assert q025(6) == 26
    assert q025(7) == 31
    assert q025(8) == 36
    assert q025(9) == 40
    assert q025(10) == 45

    assert q025(1000) == 4782


def test_decimal_unit_fraction():
    assert decimal_unit_fraction(2) == ('5', '')
    assert decimal_unit_fraction(3) == ('3', '3')
    assert decimal_unit_fraction(4) == ('25', '')
    assert decimal_unit_fraction(5) == ('2', '')
    assert decimal_unit_fraction(6) == ('16', '6')
    assert decimal_unit_fraction(7) == ('142857', '142857')
    assert decimal_unit_fraction(13) == ('076923', '076923')
    assert decimal_unit_fraction(17) == (
        '0588235294117647', '0588235294117647')


def test_recur_cycle_length():
    assert recur_cycle_length(2) == 0
    assert recur_cycle_length(4) == 0
    assert recur_cycle_length(3) == 1
    assert recur_cycle_length(6) == 1
    assert recur_cycle_length(7) == 6
    assert recur_cycle_length(13) == 6
    assert recur_cycle_length(17) == 16


def test_q026():
    assert q026(5) == 3
    assert q026(10) == 7
    assert q026(20) == 19
    assert q026(1000) == 983


def test_is_prime():
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(101) == True
    assert is_prime(999983) == True
    assert is_prime(999987) == False
    assert is_prime(1000003) == True
    assert is_prime(1000033) == True
    assert is_prime(1000007) == False


def test_count_consecutive_primes():
    assert count_consecutive_primes(a=1, b=-1) == 0
    assert count_consecutive_primes(a=1, b=3) == 2
    assert count_consecutive_primes(a=1, b=41) == 40
    assert count_consecutive_primes(a=-79, b=1601) == 80


def test_q027():
    assert q027(1, 1) == 0
    assert q027(2, 4) == -1 * 3
    assert q027(2, 42) == -1 * 41
    assert q027(1000, 1001) == -61 * 971


def test_q028():
    assert q028(1) == 1
    assert q028(3) == 1 + 3 + 5 + 7 + 9
    assert q028(5) == 101
    assert q028(7) == 101 + 31 + 37 + 43 + 49
    assert q028(1001) == 669171001


def test_q029():
    assert q029(2, 2) == 1
    assert q029(4, 4) == 8
    assert q029(5, 5) == 15
    assert q029(6, 6) == 23  # 2^4 == 4^2, 2^6 == 4^3, so it is 25 - 2
    # 69 computed by len(set(a ** b for a in range(2, 11) for b in range(2, 11)))
    assert q029(10, 10) == 69

    assert q029(100, 100) == 9183


def test_digit_n_power_sum():
    assert digit_n_power_sum(1, 1) == 1
    assert digit_n_power_sum(2, 2) == 4
    assert digit_n_power_sum(12, 2) == 5
    assert digit_n_power_sum(22, 2) == 8
    assert digit_n_power_sum(1634, 4) == 1634
    assert digit_n_power_sum(8208, 4) == 8208
    assert digit_n_power_sum(9474, 4) == 9474


def test_q030():
    assert q030(2) == 0
    assert q030(3) == 153 + 370 + 371 + 407
    assert q030(4) == 19316
    assert q030(5) == 443839  # 4150 + 4151 + 54748 + 92727 + 93084 + 194979
