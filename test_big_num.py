from big_num import BigNum
import random
import pytest


def test_big_num():
    n1 = BigNum('0')
    assert str(n1) == '0'

    n2 = BigNum('1')
    assert str(n2) == '1'

    n3 = BigNum('001')
    assert str(n3) == '1'

    n4 = BigNum('10001')
    assert str(n4) == '10001'

    n5 = BigNum('09876543210')
    assert str(n5) == '9876543210'

    n6 = BigNum('      12345     ')
    assert str(n6) == '12345'

    # random test
    for _ in range(1000):
        n = random.randint(1, 10 ** 10)
        big_num_n = BigNum(str(n))
        assert str(big_num_n) == str(n)


def test_big_num_handle_invalid_input():
    test_inputs = [
        '1.234',
        '',
        'foo bar'
        'Hello world',
        '$12345',
        'lEE7'
    ]
    for input in test_inputs:
        with pytest.raises(ValueError) as e_info:
            n = BigNum(input)
        assert 'cannot interpret input string' in str(e_info.value)


def test_big_num_addition():
    n0 = BigNum('12345')
    n1 = BigNum('298765')
    assert isinstance(n0 + n1, BigNum)
    assert str(n0 + n1) == str(12345 + 298765)
    assert str(n0) == '12345'   # origin ref not mutated by addition operation
    assert str(n1) == '298765'

    n2 = BigNum('0021') + BigNum('488586738390')
    assert isinstance(n2, BigNum)
    assert str(n2) == str(21 + 488586738390)

    n3 = BigNum('8476739468001') + BigNum('1009')
    assert isinstance(n3, BigNum)
    assert str(n3) == str(8476739468001 + 1009)

    # random test
    for _ in range(1000):
        n1 = random.randint(1, 10 ** 10)
        n2 = random.randint(1, 10 ** 10)
        sum = n1 + n2
        assert str(BigNum(str(n1)) + BigNum(str(n2))) == str(sum)


def test_big_num_equal():
    n1 = BigNum('12345')
    n2 = BigNum('12345')
    assert n1 == n2

    n3 = BigNum('0012345')
    assert n1 == n3
    assert n3 == n1

    # random test
    for _ in range(1000):
        n0 = random.randint(1, 10 ** 10)
        n1 = n0
        if random.random() > 0.3:
            n1 += random.randint(-10, 10)
        bignum0 = BigNum(str(n0))
        bignum1 = BigNum(str(n1))
        assert (bignum0 == bignum1) == (n0 == n1)
