from typing import Generator


def farey_sequence(n: int) -> Generator[tuple[int, int], None, None]:
    (a, b, c, d) = (0, 1, 1, n)
    yield (a, b)
    while c <= n:
        k = (n + b) // d
        (a, b, c, d) = (c, d, k * c - a, k * d - b)
        yield (a, b)


def farey_sequence_start_from_between(n: int, a: int, b: int, c: int, d: int) -> Generator[tuple[int, int], None, None]:
    yield (a, b)
    while c <= n:
        k = (n + b) // d
        (a, b, c, d) = (c, d, k * c - a, k * d - b)
        yield (a, b)
