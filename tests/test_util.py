import random
from big_num import BigNum
from util import all_divisors, count_digits, factorial, first_true, has_even_digit, int_to_digits, is_palindromic_bin, is_pandigital, join_nums, make_prime_checker, nth, nth_fib, all_primes_below, is_prime, nth_prime, pandigital_generator, prime_generator, is_palindromic, is_palindromic_num, gcd, lcm, product, reverse_digits, rotate_digits, rotate_digits_iter, str_to_digits, triangle_number_generator, bignum_factorial, is_sum_of_two_elements


def test_nth_fib():
    assert nth_fib(1) == 1
    assert nth_fib(2) == 2
    for (i, fibNumber) in enumerate([1, 2, 3, 5, 8, 13, 21, 34, 55, 89]):
        assert nth_fib(i + 1) == fibNumber


primes_until_1000 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439,
                     443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]


def test_all_primes_below():
    assert list(all_primes_below(1000)) == primes_until_1000


def test_is_prime():
    for i in range(1000):
        assert (i in primes_until_1000) == is_prime(i)

    prime_memo = [p for p in primes_until_1000 if p <= 100]
    primes_below_10000 = list(all_primes_below(10000))
    for i in range(10_000):
        assert (i in primes_below_10000) == is_prime(i, known_prime=prime_memo)


def test_prime_generator():
    assert list(prime_generator(limit=1000)) == primes_until_1000
    primes_30_to_2000 = [p for p in all_primes_below(2000) if p >= 30]
    assert list(prime_generator(start=30, limit=2000)) == primes_30_to_2000


def test_nth_prime():
    for (index, prime) in enumerate(primes_until_1000):
        assert nth_prime(index + 1) == prime


def test_is_palindromic():
    assert is_palindromic('') == True
    assert is_palindromic('A') == True
    assert is_palindromic('AA') == True
    assert is_palindromic('AB') == False
    assert is_palindromic('ABA') == True
    assert is_palindromic('ABC') == False
    assert is_palindromic('ABBA') == True
    assert is_palindromic('ABBC') == False
    assert is_palindromic('tattarrattat') == True


def test_is_palinromic_num():
    assert is_palindromic_num(1) == True
    assert is_palindromic_num(2) == True
    assert is_palindromic_num(10) == False
    assert is_palindromic_num(11) == True
    assert is_palindromic_num(12) == False
    assert is_palindromic_num(343) == True
    assert is_palindromic_num(345) == False
    assert is_palindromic_num(3443) == True
    assert is_palindromic_num(34542) == False
    assert is_palindromic_num(34543) == True


def test_is_palindromic_bin():
    assert is_palindromic_bin(0b0000) == True
    assert is_palindromic_bin(0b0001) == True
    assert is_palindromic_bin(0b0010) == False
    assert is_palindromic_bin(0b0011) == True
    assert is_palindromic_bin(0b0100) == False
    assert is_palindromic_bin(0b0101) == True
    assert is_palindromic_bin(0b0110) == False
    assert is_palindromic_bin(0b0111) == True
    assert is_palindromic_bin(0b1000) == False


def test_gcd():
    assert gcd(1, 1) == 1
    assert gcd(3, 5) == 1
    assert gcd(2, 6) == 2
    assert gcd(12, 15) == 3
    assert gcd(60, 144) == 12


def test_lcm():
    assert lcm(1, 1) == 1
    assert lcm(20, 1) == 20
    assert lcm(2, 5) == 10
    assert lcm(12, 15) == 60
    assert lcm(14, 18) == 126


def test_product():
    assert product(range(5)) == 0
    assert product(range(1, 5)) == 24
    assert product([1, 2, 3, 0, 4]) == 0
    assert product([-1, -2, -3, 4]) == -24


def test_str_to_digits():
    assert list(str_to_digits("1")) == [1]
    assert list(str_to_digits("12345")) == [1, 2, 3, 4, 5]


def test_int_to_digits():
    assert list(int_to_digits(1)) == [1]
    assert list(int_to_digits(12)) == [1, 2]
    assert list(int_to_digits(12345)) == [1, 2, 3, 4, 5]
    assert list(int_to_digits(90000000)) == [9, 0, 0, 0, 0, 0, 0, 0]


def test_triangle_number_generator():
    t_gen = triangle_number_generator()
    for k in [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]:
        assert next(t_gen) == k


def test_all_divisors():
    assert all_divisors(1) == [1]
    assert all_divisors(2) == [1, 2]
    assert all_divisors(3) == [1, 3]
    assert all_divisors(4) == [1, 2, 4]
    assert all_divisors(6) == [1, 2, 3, 6]
    assert all_divisors(8) == [1, 2, 4, 8]
    assert all_divisors(36) == [1, 2, 3, 4, 6, 9, 12, 18, 36]
    assert all_divisors(60) == [1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60]


def test_bignum_factorial():
    assert bignum_factorial(BigNum('1')) == BigNum('1')
    assert bignum_factorial(BigNum('2')) == BigNum('2')
    assert bignum_factorial(BigNum('3')) == BigNum('6')
    assert bignum_factorial(BigNum('4')) == BigNum('24')
    assert bignum_factorial(BigNum('5')) == BigNum('120')


def test_is_sum_of_two_elements():
    num_list = [1, 3, 5, 7, 9]
    assert is_sum_of_two_elements(1, num_list) == False
    assert is_sum_of_two_elements(2, num_list) == True
    assert is_sum_of_two_elements(4, num_list) == True
    assert is_sum_of_two_elements(5, num_list) == False
    assert is_sum_of_two_elements(6, num_list) == True


def test_nth():
    assert nth([1], 0) == 1
    assert nth([1, 2], 0) == 1
    assert nth([1, 2], 1) == 2
    assert nth([1, 2], 2) == None
    assert nth(range(100), 50) == 50


def test_count_digits():
    assert count_digits(-1) == 1
    assert count_digits(0) == 1
    assert count_digits(1) == 1
    assert count_digits(9) == 1
    assert count_digits(10) == 2
    assert count_digits(17) == 2
    assert count_digits(99) == 2
    assert count_digits(100) == 3
    assert count_digits(144) == 3

    # random test
    for _ in range(100):
        n = random.randint(0, 10**100)
        assert count_digits(n) == len(str(n))


def test_is_pandigital():
    assert is_pandigital(123456789) == True
    assert is_pandigital(987654321) == True
    assert is_pandigital(246813579) == True
    assert is_pandigital(112345679) == False
    assert is_pandigital(23456789) == False
    assert is_pandigital(246813590) == False

    assert is_pandigital(12345, 1, 5) == True
    assert is_pandigital(12346, 1, 5) == False
    assert is_pandigital(123456, 1, 5) == False
    assert is_pandigital(43210, 0, 4) == True


def test_pandigital_generator():
    gen = pandigital_generator()
    assert next(gen) == 123456789
    assert next(gen) == 123456798
    assert next(gen) == 123456879
    assert next(gen) == 123456897
    assert next(gen) == 123456978
    assert next(gen) == 123456987
    *_, last = gen
    assert last == 987654321

    gen2 = pandigital_generator(1, 3)
    assert list(gen2) == [123, 132, 213, 231, 312, 321]


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(-1) == 0
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(5) == 120

    # test for memoization
    memo = {}
    factorial(9, memo)
    assert memo[9] == 362880
    assert memo[8] == 40320


def test_rotate_digits():
    assert rotate_digits(1, 1) == 1
    assert rotate_digits(12, 1) == 21
    assert rotate_digits(12, 2) == 12
    assert rotate_digits(12, 9999999) == 21

    assert rotate_digits(1234567, 3) == 5671234
    assert rotate_digits(1234567, 780) == 5671234

    assert rotate_digits(1234567, -3) == 4567123
    assert rotate_digits(1234567, -500) == 4567123

    assert rotate_digits(100, 1) == 10
    assert rotate_digits(100, 2) == 1
    assert rotate_digits(100, 3) == 100
    assert rotate_digits(1002, 1) == 2100
    assert rotate_digits(1002, 2) == 210
    assert rotate_digits(1002, 3) == 21
    assert rotate_digits(10203, 1) == 31020
    assert rotate_digits(10203, 2) == 3102
    assert rotate_digits(10203, 3) == 20310
    assert rotate_digits(10203, 4) == 2031
    assert rotate_digits(10203, 5) == 10203


def test_rotate_digits_iter():
    assert list(rotate_digits_iter(1)) == []
    assert list(rotate_digits_iter(10)) == [1]
    assert list(rotate_digits_iter(11)) == [11]
    assert list(rotate_digits_iter(12)) == [21]
    assert list(rotate_digits_iter(123)) == [312, 231]
    assert list(rotate_digits_iter(100)) == [10, 1]
    assert list(rotate_digits_iter(1003)) == [3100, 310, 31]
    assert list(rotate_digits_iter(304050)) == [
        30405, 503040, 50304, 405030, 40503]


def test_has_even_digit():
    assert has_even_digit(0) == True
    assert has_even_digit(1) == False
    assert has_even_digit(2) == True
    assert has_even_digit(4) == True
    assert has_even_digit(6) == True
    assert has_even_digit(8) == True
    assert has_even_digit(10) == True
    assert has_even_digit(11) == False
    assert has_even_digit(13) == False
    assert has_even_digit(13579) == False
    assert has_even_digit(135790) == True


def test_join_nums():
    assert join_nums(1, 2, 3, 4) == 1234
    assert join_nums(1, 0, 0, 1) == 1001
    assert join_nums(0, 1, 2, 0, 3, 4) == 12034
    assert join_nums(0, 12, 345, 6, 789) == 123456789


def test_first_true():
    assert first_true([0, [], 1]) == 1
    assert first_true([False, 0, []], default='a') == 'a'
    assert first_true(range(100), pred=lambda x: x > 10) == 11
    assert first_true(range(100), pred=lambda x: x > 100, default=None) == None


def test_make_prime_checker():
    prime_checker = make_prime_checker(1_000_000)
    primes = set(all_primes_below(1_005_000))
    for num in range(2, 1_005_000):
        assert prime_checker(num) == (num in primes)


def test_reverse_digits():
    assert reverse_digits(1) == 1
    assert reverse_digits(10) == 1
    assert reverse_digits(123) == 321
    assert reverse_digits(1000) == 1
    assert reverse_digits(
        576838365960837657684635252) == 252536486756738069563838675

    # test other base
    assert reverse_digits(0b10, 2) == (0b01)
    assert reverse_digits(0b10101110, 2) == (0b01110101)
    assert reverse_digits(0o1237, 8) == (0o7321)
    assert reverse_digits(0x1abf, 16) == (0xfba1)
