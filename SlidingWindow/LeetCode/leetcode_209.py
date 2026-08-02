
"""
LeetCode 209 - Minimum Size Subarray Sum

Brief:
Find the smallest length of a contiguous subarray with sum >= target.

Sliding window idea:
- Expand: move right and add nums[right] to running sum.
- Shrink: while sum >= target, update minimum length and remove left element.
- Valid/goal condition: sum >= target triggers contraction to minimize length.
- Answer: smallest length found, or 0 if no valid window exists.
"""

def minSubArrayLen(target: int, nums: list[int]) -> int:
    min_len = float('inf')
    left = 0
    _sum = 0
    for right in range(len(nums)):
        _sum += nums[right]
        while _sum >= target:
            min_len = min(min_len, right - left + 1)
            _sum -= nums[left]
            left += 1
        if min_len == 1:
            return 1
    return min_len if min_len != float('inf') else 0

print(minSubArrayLen(4, [1,4,4]))


