"""
Time complexity for this algorithm ->  0(n^2) worst case scenario
                                   ->  O(nlog(n)) average case
"""


def quick_sort(_array: list, reverse=False):
    order = 1 if not reverse else -1

    def _sorting(_array, left: int, right: int):
        if left < right:
            pivot = right
            left_wall = left
            for i in range(left, right):
                if order*_array[i] < order*_array[pivot]:
                    _array[i], _array[left_wall] = _array[left_wall], _array[i]
                    left_wall += 1
            _array[pivot], _array[left_wall] = _array[left_wall], _array[pivot]
            _sorting(_array, left, left_wall - 1)
            _sorting(_array, left_wall + 1, right)
    _sorting(_array, 0, len(_array)-1)


_array = [9, 9, 8, 10, 10, 0, 0, 1, 1]
quick_sort(_array, False)
print(_array)
