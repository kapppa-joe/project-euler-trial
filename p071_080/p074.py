from util import factorial, int_to_digits

FactorialMemo = {}

LengthMemo = {
    1: 1,
    2: 1,
    145: 1,
    169: 3,
    363601: 3,
    1454: 3,
    871: 2,
    45361: 2,
    872: 2,
    45362: 2,
    40585: 1
}


def p074(upper_limit: int = 1_000_000, req_terms: int = 60) -> int:
    memo = LengthMemo.copy()
    for i in range(upper_limit):
        chain_length(i, memo)
    return sum(1 for key, value in memo.items()
               if value == req_terms and key < upper_limit)


def fac(n: int) -> int:
    return factorial(n, FactorialMemo)


def fac_of_digits(num: int) -> int:
    return sum(fac(digit) for digit in int_to_digits(num))


def chain_length(num: int, memo: dict[int, int] = LengthMemo) -> int:
    if num in memo:
        return memo[num]
    else:
        res = chain_length(fac_of_digits(num)) + 1
        memo[num] = res
        return res
