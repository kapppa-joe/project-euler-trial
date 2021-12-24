from typing import Iterable


DefaultCoinSet = {1, 2, 5, 10, 20, 50, 100, 200}


class CoinChange:
    """
    A custom class to implement a generic solution for problem 31 (coin sums)
    Initialize with the value of coins that can be used
    """

    def __init__(self, coin_set: Iterable[int] = DefaultCoinSet):
        self.coin_set = sorted(coin_set, reverse=True)
        self.coin_types = len(self.coin_set)

    def coin_value(self, idx: int) -> int:
        return self.coin_set[idx]

    def count_ways_to_make_change(self, amount: int, current_coin_idx=0) -> int:
        if amount == 0:
            return 1
        if current_coin_idx >= self.coin_types or amount < 0:
            return 0

        count_solutions = 0
        for i in range(current_coin_idx, self.coin_types):
            if amount >= self.coin_value(i):
                recur_solutions = self.count_ways_to_make_change(
                    amount - self.coin_value(i), i)
                count_solutions += recur_solutions

        return count_solutions

    def list_ways_to_make_change(self, amount: int, current_coin_idx=0, acc: list[int] = []) -> list[list[int]]:
        if amount == 0:
            return [acc.copy()]
        if current_coin_idx >= self.coin_types or amount < 0:
            return []

        solutions = []
        for i in range(current_coin_idx, self.coin_types):
            if amount >= self.coin_value(i):
                acc.append(self.coin_value(i))
                recur_solutions = self.list_ways_to_make_change(
                    amount - self.coin_value(i), i, acc)
                solutions += recur_solutions
                acc.pop()

        return solutions


def p031(amount: int = 200) -> int:
    """ In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:
    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
    It is possible to make £2 in the following way:
        1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
    How many different ways can £2 be made using any number of coins?
    """
    ukCoins = CoinChange(DefaultCoinSet)
    return ukCoins.count_ways_to_make_change(amount)
