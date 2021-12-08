import functools
from constant_inputs.q022_names import Q022_names
from sort import quicksort
from util import all_divisors


@functools.cache
def sum_of_divisors(n: int) -> int:
    return sum(d for d in all_divisors(n) if d != n)


def have_amicable_pair(a: int) -> bool:
    b = sum_of_divisors(a)
    return a != b and sum_of_divisors(b) == a


def q021(limit: int) -> int:
    # Evaluate the sum of all the amicable numbers under 10000.
    return sum(i for i in range(limit) if have_amicable_pair(i))


def name_score(name: str, order: int = 0) -> int:
    score = sum(ord(char) - 96 for char in name.lower())
    return score * (order + 1)


def q022(names: list[str] = Q022_names) -> int:
    # Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
    # For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
    # What is the total of all the name scores in the file?
    sorted_names = quicksort(names)

    return sum(name_score(name, i) for (i, name) in enumerate(sorted_names))
