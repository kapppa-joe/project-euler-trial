from q001_010 import q001, q002, q003, q004, q005, q006, q007
from test_util import all_primes_below


def test_q001():
    assert q001(0, 0, 1) == 0
    assert q001(3, 5, 10) == 23
    assert q001(2, 3, 10) == 32
    assert q001(3, 5, 1000) == 233168


def test_q002():
    assert q002(2) == 0
    assert q002(3) == 2
    assert q002(10) == 10
    assert q002(100) == 44
    assert q002(1000) == 798
    assert q002(4_000_000) == 4613732


def test_q003():
    assert q003(10) == 5
    assert q003(82) == 41
    assert q003(1986) == 331
    assert q003(13195) == 29
    assert q003(600851475143) == 6857

    all_primes_below_10000_desc = list(all_primes_below(10000, asc=False))
    for test_num in range(4, 10000):
        if test_num in all_primes_below_10000_desc:
            continue
        largest_factor = next(
            i for i in all_primes_below_10000_desc if test_num % i == 0)
        assert largest_factor == q003(test_num)


def test_q004():
    assert q004(1) == 9
    assert q004(2) == 9009
    assert q004(3) == 906609


def test_q005():
    assert q005(1) == 1
    assert q005(2) == 2
    assert q005(3) == 6
    assert q005(4) == 12
    assert q005(5) == 60
    assert q005(6) == 60
    assert q005(10) == 2520
    assert q005(20) == 232792560


def test_q006():
    assert q006(1) == 0
    assert q006(2) == 4
    assert q006(3) == 22
    assert q006(10) == 2640
    assert q006(100) == 25164150


def test_q007():
    all_primes_below_1000 = all_primes_below(1000)
    for (index, prime) in enumerate(all_primes_below_1000):
        assert q007(index + 1) == prime
    assert q007(10001) == 104743
