"""
Time complexity for this algorithm ->  0(n^2) worst case scenario
"""


def insertion_sort(_array: list, reverse=False) -> list:
    l = len(_array)
    order = 1 if not reverse else -1
    for i in range(1, l):
        j = i
        while j > 0 and order*_array[j] < order*_array[j-1]:
            _array[j], _array[j - 1] = _array[j - 1], _array[j]
            j -= 1
    return _array


print(insertion_sort([2, 8, 5, 3, 9, 4, 1], True))
