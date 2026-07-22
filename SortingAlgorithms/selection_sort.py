"""
Time complexity for this algorithm ->  0(n^2)
"""


def selection_sort(_array: list, reverse=False) -> list:
    order = 1 if not reverse else -1
    for i in range(len(_array)):
        cur_min = i
        for j in range(i+1, len(_array)):
            if order*_array[cur_min] > order*_array[j]:
                cur_min = j
        _array[cur_min], _array[i] = _array[i], _array[cur_min]
    return _array


print(selection_sort([2, 8, 5, 3, 9, 4, 1], True))

