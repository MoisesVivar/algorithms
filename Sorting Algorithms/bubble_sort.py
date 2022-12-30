"""
Time complexity for this algorithm ->  0(n^2)
"""


def bubble_sort(_array: list, reverse=False):
    order = 1 if not reverse else -1
    for i in range(len(_array), 0, -1):
        for j in range(i-1):
            if order*_array[j+1] < order*_array[j]:
                _array[j+1], _array[j] = _array[j], _array[j+1]


_array = [2, 8, 5, 3, 9, 4, 1]
bubble_sort(_array, True)
print(_array)

