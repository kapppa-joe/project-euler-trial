from typing import Optional, Tuple
from util import all_primes_below, fib_generator, is_palindromic_num, is_prime, lcm, nth_prime, product, str_to_digits


def q001(a: int, b: int, limit: int) -> int:
    # If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    # Find the sum of all the multiples of 3 or 5 below 1000.

    if (a <= 0 or b <= 0 or limit <= 0):
        return 0
    return sum(i for i in range(limit) if i % a == 0 or i % b == 0)


def q002(limit: int) -> int:
    # Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
    # 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    # By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

    return sum(num for num in fib_generator(limit) if num % 2 == 0)


def q003(n: int) -> int:
    # The prime factors of 13195 are 5, 7, 13 and 29.
    # What is the largest prime factor of the number 600851475143 ?
    square_root = round(n ** 0.5)
    largest_candidate_below_sqrt_n = None
    for i in range(2, square_root + 1):
        if n % i == 0:
            factor_above_sqrt_n = n // i
            if is_prime(factor_above_sqrt_n):
                return factor_above_sqrt_n
            if is_prime(i):
                largest_candidate_below_sqrt_n = i
    return largest_candidate_below_sqrt_n


def q004(digits: int) -> int:
    # A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
    # Find the largest palindrome made from the product of two 3-digit numbers.
    upperLimit = 10 ** digits
    lowerLimit = 10 ** (digits - 1)
    return max(x * y for x in range(lowerLimit, upperLimit) for y in range(lowerLimit, upperLimit) if is_palindromic_num(x * y))


def q005(limit: int) -> int:
    # 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    # What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    acc = 1
    for i in range(2, limit + 1):
        acc = lcm(acc, i)
    return acc


def q006(n: int) -> int:
    # Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
    sqaure_of_sum = sum(i for i in range(1, n + 1)) ** 2
    sum_of_square = sum(i ** 2 for i in range(1, n + 1))
    return abs(sqaure_of_sum - sum_of_square)


def q007(n: int) -> int:
    # What is the 10 001st prime number?
    return nth_prime(n)


Q008_constant = """
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
""".replace('\n', '')


def q008(string: str, digits: int) -> int:
    # The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
    # Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
    substrings = string.split('0')
    adj_digits_strings = []

    for substr in substrings:
        if len(substr) < digits:
            continue
        adj_digits_strings += [substr[i:i+digits]
                               for i in range(0, len(substr) - digits + 1)]
    if not adj_digits_strings:
        return 0
    return max(product(str_to_digits(digits_string)) for digits_string in adj_digits_strings)


def find_triplet(triplet_sum: int) -> Optional[list[Tuple[int, int, int]]]:
    def c(a: int, b: int) -> int:
        return triplet_sum - a - b

    candidates_for_a_b = ((a, b)
                          for b in range(1, triplet_sum // 2)
                          for a in range(1, b + 1)
                          if (a ** 2 + b ** 2 == c(a, b) ** 2))
    if candidates_for_a_b:
        triplets = [(a, b, c(a, b)) for (a, b) in candidates_for_a_b]
        return triplets
    else:
        return None


def q009(triplet_sum: int) -> Optional[int]:
    # A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
    # For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
    # There exists exactly one Pythagorean triplet for which a + b + c = 1000.  Find the product abc.

    triplets = find_triplet(triplet_sum)
    if triplets and len(triplets) == 1:
        (a, b, c) = triplets[0]
        return a * b * c
    else:
        return None


def q010(limit: int) -> int:
    # The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    # Find the sum of all the primes below two million.
    return sum(all_primes_below(limit))
