from typing import Iterable, Tuple
from functools import cache


class NumberTriangle():
    """
    A class to handle number triangle in problem 18 and problem 67
    """

    def __init__(self, input_triangle: str):
        self.triangle = [[int(number_str) for number_str in row.split(' ')]
                         for row in input_triangle.split("\n")]
        self.height = len(self.triangle)

        # workout the max_value of each cell in a bottom-top approach.
        for row in range(self.height):
            for col in range(row):
                self.max_value(row, col)

    def get(self, row: int, col: int) -> int:
        """
        return the value at a cell in the triangle.
        row/col starts with 0, with rows from top to bottom and cols from left to right. 
        """
        if col > row:
            raise ValueError(f"cannot get col {col} in row {row}")
        if row >= self.height:
            raise ValueError(
                f"max row of this triangle is row {self.height - 1}")

        return self.triangle[row][col]

    def next_cells(self, row: int, col: int) -> Iterable[Tuple[int, int]]:
        """
        return the coord of reachable cells in next row
        """
        if row >= self.height - 1:
            return iter([])
        else:
            return (cell for cell in ((row + 1, col), (row + 1, col + 1)))

    @cache
    def max_value(self, row: int, col: int) -> int:
        """
        return the max value that can be attained starting from a cell to the bottom of triangle 
        """
        self_value = self.get(row, col)
        if row == self.height - 1:
            return self_value
        else:
            return self_value + max(self.max_value(*next_cell) for next_cell in self.next_cells(row, col))
