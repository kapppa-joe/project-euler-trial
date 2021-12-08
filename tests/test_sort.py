from sort import quicksort
import random


def test_quicksort():
    array = [1]
    assert quicksort(array) == [1]

    array = [2, 1]
    assert quicksort(array) == [1, 2]

    array = [1, 2, 1, 2]
    assert quicksort(array) == [1, 1, 2, 2]

    array = [3, 2, 1, 5, 4, 3, 2]
    assert quicksort(array) == [1, 2, 2, 3, 3, 4, 5]

    array = ['cat', 'car', 'dog', 'rat', 'bat', 'care']
    assert quicksort(array) == ['bat', 'car', 'care', 'cat', 'dog', 'rat']

    # random test
    for _ in range(100):
        array = [random.randint(-1000, 1000) for _ in range(100)]
        sortedArray = sorted(array)
        assert quicksort(array) == sortedArray
