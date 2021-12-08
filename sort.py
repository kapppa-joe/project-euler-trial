def quicksort(array: list) -> list:
    # return a sorted list
    if len(array) <= 1:
        return array[:]
    else:
        return _quicksort(array)


def _quicksort(array: list) -> list:
    if len(array) <= 1:
        return array

    pivot = array[0]
    greater = []
    equal = []
    less = []
    for elem in array:
        if elem < pivot:
            less.append(elem)
        elif elem == pivot:
            equal.append(elem)
        elif elem >= pivot:
            greater.append(elem)
    return _quicksort(less) + equal + _quicksort(greater)
