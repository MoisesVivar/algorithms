from collections import deque

def longest_subarray_max_min(nums: list, l: int) -> int:
    max_d = deque()
    min_d = deque()
    left = 0
    cur_longest = 0
    for right in range(len(nums)):
        while max_d and nums[max_d[-1]] < nums[right]:
            max_d.pop()
        max_d.append(right)
        while min_d and nums[min_d[-1]] > nums[right]:
            min_d.pop()
        min_d.append(right)
        while nums[max_d[0]] - nums[min_d[0]] > l:
            left += 1
            if left > max_d[0]:
                max_d.popleft()
            if left > min_d[0]:
                min_d.popleft()
        cur_longest = max(cur_longest, right - left + 1)
    return cur_longest


print(longest_subarray_max_min([8, 2, 4, 7], 4))

