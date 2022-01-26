# from functools import cache
# from util import all_primes_below
from totient import Totients


def p069(upper_limit: int = 1_000_001):
    t = Totients(upper_limit)
    return max(range(2, upper_limit), key=t.n_over_totient_n)


# class Totient:
#     def __init__(self, upper_limit=1_000_000) -> None:
#         self.upper_limit = upper_limit
#         self.Primes = {p: None for p in all_primes_below(upper_limit + 1)}

#     def n_over_totient_n(self, n: int) -> float:
#         if n in self.Primes:
#             return n / (n-1)
#         else:
#             product = 1
#             for pf in self.prime_factors(n):
#                 product *= self.n_over_totient_n(pf)
#             return product

#     def totient(self, n: int) -> int:
#         if n in self.Primes:
#             return n - 1
#         else:
#             product = n
#             for pf in self.prime_factors(n):
#                 product *= (1 - 1/pf)
#             return int(product)

#     @cache
#     def prime_factors(self, n: int) -> set[int]:
#         if n in self.Primes or n == 1:
#             return set()

#         for p in self.Primes:
#             if n % p == 0:
#                 while n % p == 0:
#                     n = n // p
#                 if n in self.Primes:
#                     return {n, p}
#                 else:
#                     return self.prime_factors(n) | {p}

#         raise RuntimeError
