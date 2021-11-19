from q001_010 import q001, fib, q002


def test_q001():
    assert q001(0, 0, 1) == 0
    assert q001(3, 5, 10) == 23
    assert q001(2, 3, 10) == 32
    assert q001(3, 5, 1000) == 233168


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 2
    for (i, fibNumber) in enumerate([1, 2, 3, 5, 8, 13, 21, 34, 55, 89]):
        assert fib(i + 1) == fibNumber


def test_q002():
    assert q002(2) == 0
    assert q002(3) == 2
    assert q002(10) == 10
    assert q002(100) == 44
    assert q002(1000) == 798
    assert q002(4_000_000) == 4613732
