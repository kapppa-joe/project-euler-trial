from constant_inputs.q022_names import Q022_names
from q021_030 import have_amicable_pair, name_score, q021, q022, sum_of_divisors


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
