from collections import deque

def maximum_subarray_value(nums: list, k: int) -> list:
    max_nums = []
    q = deque()
    left = 0
    for right in range(len(nums)):
        while q and (nums[q[-1]] < nums[right]):
            q.pop()
        q.append(right)
        if right - left + 1 > k:
            left += 1

        if left > q[0]:
            q.popleft()

        if right - left + 1 == k:
            max_nums.append(nums[q[0]])
    return max_nums


print(maximum_subarray_value([1, 2, 3, 4, 5], 3))
