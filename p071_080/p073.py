from farey_seq import farey_sequence_start_from_between, search_right_neighbour


def p073(a: int, b: int, c: int, d: int, n: int) -> int:
    c0, d0 = search_right_neighbour(a, b, n)
    seq = farey_sequence_start_from_between(n, a, b, c0, d0)

    next(seq)  # remove the starting (a, b)
    count = 0

    for numer, denom in seq:
        if (numer, denom) == (c, d):
            return count
        count += 1

    raise RuntimeError
