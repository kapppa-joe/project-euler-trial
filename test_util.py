from util import nth_fib, all_primes_below, is_prime, nth_prime, prime_generator, is_palindromic, is_palindromic_num, gcd, lcm, product, str_to_digits


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


def test_prime_generator():
    assert list(prime_generator(1000)) == primes_until_1000


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
