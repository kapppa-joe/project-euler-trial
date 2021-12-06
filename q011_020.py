import functools
from typing import Iterable, Optional
from big_num import BigNum
from calendar_date import CalendarDate
from constant_inputs.q011_input import Q011_grid_raw
from constant_inputs.q013_input import Q013_input_string
from constant_inputs.q018_input import Q018_triangle_raw_input
from number_in_words import count_letters, number_in_words
from number_triangle import NumberTriangle
from util import all_divisors, factorial, is_even, product, triangle_number_generator


def q011(input_grid: str = Q011_grid_raw, n: int = 4) -> int:
    # What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?
    # (here I use n to denote the number of adj nums to multiply)
    if (not input_grid or n <= 0):
        return 0

    numbers_grid = [[int(num_string) for num_string in row.split(' ')]
                    for row in input_grid.split('\n')]
    flatten_grid = [num for row in numbers_grid for num in row]
    height = len(numbers_grid)
    width = len(numbers_grid[0])

    def value(x: int, y: int) -> int:
        return flatten_grid[y * width + x]

    def left_to_right(x0: int, y0: int) -> Iterable[int]:
        if x0 + n > width:
            return []
        return (value(x0 + i, y0) for i in range(n))

    def top_to_down(x0: int, y0: int) -> Iterable[int]:
        if y0 + n > height:
            return []
        return (value(x0, y0 + i) for i in range(n))

    def diagonal_SE(x0: int, y0: int) -> Iterable[int]:
        if x0 + n > width or y0 + n > height:
            return []
        return (value(x0 + i, y0 + i) for i in range(n))

    def diagonal_SW(x0: int, y0: int) -> Iterable[int]:
        if x0 - n + 1 < 0 or y0 + n > height:
            return []
        return (value(x0 - i, y0 + i) for i in range(n))

    def all_four_directions(x0: int, y0: int) -> Iterable[Iterable[int]]:
        return (left_to_right(x0, y0), top_to_down(x0, y0), diagonal_SE(x0, y0), diagonal_SW(x0, y0))

    return max(product(adj_nums)
               for x0 in range(width)
               for y0 in range(height)
               for adj_nums in all_four_directions(x0, y0))


def q012(number_of_divisors: int) -> Optional[int]:
    # What is the value of the first triangle number to have over five hundred divisors?
    for t in triangle_number_generator():
        if len(all_divisors(t)) > number_of_divisors:
            return t


def q013(input_str: str = Q013_input_string, digits: int = 10) -> str:
    # Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
    big_nums = (BigNum(num_string) for num_string in input_str.split('\n'))
    total_sum = functools.reduce(lambda acc, i: acc + i, big_nums)
    return str(total_sum)[:digits]


def collatz_next(n: int) -> int:
    if is_even(n):
        return n // 2
    else:
        return 3 * n + 1


@functools.cache
def collatz_chain(starting_num: int) -> int:
    if starting_num < 1:
        return 0
    elif starting_num == 1:
        return 1
    else:
        return 1 + collatz_chain(collatz_next(starting_num))


def q014(upper_limit: int) -> int:
    # Which starting number, under one million, produces the longest Collatz sequence chain?
    candidate = 0
    longest_chain = 0
    for i in range(1, upper_limit):
        chain_length = collatz_chain(i)
        if chain_length > longest_chain:
            candidate = i
            longest_chain = chain_length
    return candidate


def q015(width: int, height: int) -> int:
    # Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
    # How many such routes are there through a 20×20 grid?
    return q015_recur(width, height)


@functools.cache
def q015_recur(width: int, height: int) -> int:
    if width == 0 or height == 0:
        return 1
    else:
        return q015_recur(width - 1, height) + q015_recur(width, height - 1)


def q016(power: int) -> int:
    # 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
    # What is the sum of the digits of the number 2^1000?

    if power == 0:
        return 1

    acc = BigNum('2')
    k = BigNum('1')
    while power > 1:
        if is_even(power):
            acc = acc * acc
            power = power // 2
        else:
            k *= acc
            power = power - 1
    acc *= k

    sum_of_digits = 0
    pointer = acc.head
    while pointer:
        sum_of_digits += pointer.digit
        pointer = pointer.next
    return sum_of_digits


def q017(upper_limit: int) -> int:
    # If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
    # If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
    def f(number):
        return count_letters(number_in_words(number))

    return sum(f(i) for i in range(1, upper_limit + 1))


def q018(triangle_str: str = Q018_triangle_raw_input) -> int:
    # By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
    # Find the maximum total from top to bottom of the triangle below:
    triangle = NumberTriangle(triangle_str)
    return triangle.max_value(0, 0)


def q019() -> int:
    # How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
    dates_to_check = ((1, month, year)
                      for month in range(1, 12 + 1)
                      for year in range(1901, 2000 + 1))

    count_sundays = 0
    for (day, month, year) in dates_to_check:
        if CalendarDate(day, month, year).day_of_week() == 0:
            count_sundays += 1

    return count_sundays


def q020(n: int) -> int:
    # Find the sum of the digits in the number 100! (factorial of 100)
    fac = factorial(BigNum(str(n)))
    sum_of_digits = 0
    pointer = fac.head
    while pointer:
        sum_of_digits += pointer.digit
        pointer = pointer.next

    return sum_of_digits
