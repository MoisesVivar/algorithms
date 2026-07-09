

def max_sum_subarray(arr: list, k: int) -> int :
    left = 0
    cur_sum = 0
    max_sum = 0
    for right in range(len(arr)):
        cur_sum += arr[right]
        if right - left + 1 > k:
            cur_sum -= arr[left]
            left += 1
        if right - left + 1 == k:
            max_sum = max(cur_sum, max_sum)
    return max_sum

print(max_sum_subarray([2, 1, 5, 1, 3, 2], 3))

