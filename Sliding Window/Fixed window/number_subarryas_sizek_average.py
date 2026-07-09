
def num_subarrays_sizek_averaget(arr: list, k: int, t: float) -> int:
    left = 0
    cur_sum = 0
    num_arrs = 0
    for right in range(len(arr)):
        cur_sum += arr[right]
        if right - left + 1 > k:
            cur_sum -= arr[left]
            left += 1
        if right - left + 1 == k:
            if cur_sum >= t*k:
                num_arrs += 1
    return  num_arrs


print(num_subarrays_sizek_averaget([2, 3, 5, 1, 6, 2], 3, 3))