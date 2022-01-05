from util import all_primes_below


def p049(digits: int = 4) -> list[tuple[int, ...]]:
    """ The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
    There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
    What 12-digit number do you form by concatenating the three terms in this sequence?
    """

    n_digit_primes = [p for p in all_primes_below(10 ** digits)
                      if p > 10 ** (digits - 1)]

    permutation_groups = {}
    for p in n_digit_primes:
        root = ''.join(sorted(str(p)))
        if root not in permutation_groups:
            permutation_groups[root] = []
        permutation_groups[root].append(p)

    results = []

    for prime_permutations in permutation_groups.values():
        for i in range(len(prime_permutations)):
            for j in range(i + 1, len(prime_permutations)):
                prime_i, prime_j = prime_permutations[i], prime_permutations[j]
                diff = prime_j - prime_i
                if (prime_j + diff) in prime_permutations:
                    results.append((prime_i, prime_j, prime_j + diff))

    return results
