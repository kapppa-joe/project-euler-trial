from typing import Iterable
import itertools
import numpy as np


def p068(side=5) -> str:
    solutions = PolygonRing(side).solve_recur()
    solutions_in_string = [''.join(str(num) for num in solution)
                           for solution in solutions]
    return max(s for s in solutions_in_string if len(s) < 17)


class PolygonRing:
    def __init__(self, side: int) -> None:
        self.side = side
        self.length = side * 3
        self.numbers = list(range(1, side * 2 + 1))
        self.grid = np.zeros((side, 3), np.int32)

    def solve_recur(self) -> Iterable[tuple[int]]:
        if self.grid.all():
            yield tuple(self.grid.flatten())
        else:
            grid = self.grid
            idx_of_row_to_fill = tuple(~grid.any(axis=1)).index(True)
            for row in self.next_row_candidates():
                grid[idx_of_row_to_fill] = row
                yield from self.solve_recur()
                grid[idx_of_row_to_fill] = (0, 0, 0)
        return

    def next_row_candidates(self) -> Iterable[tuple[int, int, int]]:
        if not self.grid.any():
            # if the grid is empty, return all permutation for 3 nums
            return itertools.permutations(self.numbers, 3)

        grid = self.grid
        seed_row = grid[0]
        last_filled_row = grid[grid.any(axis=1)][-1]
        b = last_filled_row[-1]

        if grid.any(axis=1).sum() == self.side - 1:
            # special case when filling in the final row
            c = seed_row[1]
            a = seed_row.sum() - b - c

            if a in self.numbers and not a in grid and a > seed_row[0]:
                return [(a, b, c)]
            else:
                return []
        else:
            candidates = [(a, b, c)
                          for a in self.numbers
                          if a > seed_row[0]
                          and not a in self.grid
                          and not (c := sum(seed_row) - a - b) in self.grid
                          and c in self.numbers
                          and not a == c]
            return candidates
