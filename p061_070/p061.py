from typing import Iterable, TypeAlias

from polygonal_numbers import polygonal_number_generator

NumDictType: TypeAlias = dict[int, set[int]]


def p061(wanted_range: range = range(3, 9)) -> int | None:
    num_dicts = {n: make_polygonal_number_dicts(n) for n in wanted_range}

    recur_solution = p061_start_recur(num_dicts)
    if recur_solution:
        solution_sum = sum(recur_solution.values())
        print(
            f'found solution set: {recur_solution}, the sum is {solution_sum}')
        return solution_sum
    else:
        return None


def p061_start_recur(num_dicts: dict[int, NumDictType]) -> dict[int, int] | None:
    solution = {}
    # start with the largest polygon to reduce branches
    start_polygon = max(num_dicts.keys())
    first_halves_to_try = num_dicts[start_polygon].keys()

    for first_half in first_halves_to_try:
        next_nodes = num_dicts[start_polygon][first_half]
        for latter_half in next_nodes:
            solution[start_polygon] = first_half * 100 + latter_half
            recur_solution = p061_recur(
                num_dicts=num_dicts, solution=solution, curr_key=latter_half)
            if recur_solution:
                return recur_solution
    return None


def p061_recur(num_dicts: dict[int, NumDictType], solution: dict[int, int], curr_key: int) -> dict[int, int] | None:
    remaining_polygons = set(num_dicts.keys()) - set(solution)

    for next_polygon in sorted(remaining_polygons, reverse=True):
        next_nodes = find_next_nodes(
            solution, curr_key, num_dicts[next_polygon])
        if len(remaining_polygons) == 1:
            # if it is the last polygon to fill, check that the last node connects to first node
            first_half_of_first_node = first_two_digits(
                list(solution.values())[0])
            next_nodes = list(next_nodes)
            if first_half_of_first_node in next_nodes:
                solution[next_polygon] = curr_key * \
                    100 + first_half_of_first_node
                return solution
            else:
                return None

        else:
            for next_node in next_nodes:
                solution[next_polygon] = curr_key * 100 + next_node
                recur_solution = p061_recur(
                    num_dicts=num_dicts, solution=solution, curr_key=next_node)
                if recur_solution:
                    return recur_solution
                else:
                    solution.pop(next_polygon)


def find_next_nodes(solution: dict[int, int], curr_key: int, candidates: NumDictType) -> Iterable[int]:
    numbers_used = solution.values()
    return (node for node in candidates.get(curr_key, []) if not (curr_key * 100 + node) in numbers_used)


def first_two_digits(num: int) -> int:
    return num // 100


def last_two_digits(num: int) -> int:
    return num % 100


def make_polygonal_number_dicts(sides_number: int) -> NumDictType:
    # stort all n-polygonal numbers in a special dict.
    # for example, for number 8128 and 8129, store it as {81: set(28, 29)}
    # this dict is used for effective finding next polygon to connect to.

    d = {}
    for num in polygonal_number_generator(n=sides_number):
        if num < 1000:
            continue
        elif num > 9999:
            break

        key = first_two_digits(num)
        val = last_two_digits(num)
        if key < 10 or val < 10:
            continue

        if not key in d:
            d[key] = set()
        d[key].add(val)

    return d
