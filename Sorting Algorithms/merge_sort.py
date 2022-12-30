
def merge_sort(_array: list, reverse=False):
    order = 1 if not reverse else -1
    if len(_array) == 1:
        return _array
    else:
        _array_sorted = []
        left = merge_sort(_array[:len(_array)//2], reverse)
        right = merge_sort(_array[len(_array)//2:], reverse)
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if order*left[i] <= order*right[j]:
                _array_sorted.append(left[i])
                i += 1
            else:
                _array_sorted.append(right[j])
                j += 1
        if i == len(left):
            _array_sorted.extend(right[j:])
        else:
            _array_sorted.extend(left[i:])
        return _array_sorted


print(merge_sort([1, 1, 3, 0, -1, -1], True))
