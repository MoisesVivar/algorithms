from collections import deque

def longestSubarray(nums: list[int], limit: int) -> int:
    max_d = deque()
    min_d = deque()
    max_len = 0
    left = 0
    for right in range(len(nums)):
        while max_d and nums[max_d[-1]] < nums[right]:
            max_d.pop()
        max_d.append(right)
        while min_d and nums[min_d[-1]] > nums[right]:
            min_d.pop()
        min_d.append(right)
        while abs(nums[max_d[0]] - nums[min_d[0]]) > limit:
            if max_d[0] == left:
                max_d.popleft()
            if min_d[0] == left:
                min_d.popleft()
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len

print(longestSubarray([8,2,4,7], 4))