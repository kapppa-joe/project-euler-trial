from email.generator import Generator


from itertools import count


def p062(wanted_permutation: int = 5) -> int:
    store = {}

    for cube in (i ** 3 for i in count(1)):
        key = ''.join(sorted(str(cube)))
        if not key in store:
            store[key] = []
        store[key].append(cube)

        if len(store[key]) == wanted_permutation:
            print(f'solution found for permutation set: {store[key]}')
            return min(store[key])

    return 0
