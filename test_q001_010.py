from q001_010 import q001, q002, q003
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
