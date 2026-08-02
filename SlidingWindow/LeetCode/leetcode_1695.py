"""
LeetCode 1695 - Maximum Erasure Value

Brief:
Find the maximum sum of a subarray containing only unique elements.

Sliding window idea:
- Expand: add nums[right] to frequency map and running sum.
- Shrink: while nums[right] is duplicated, move left, decrement freq, subtract values.
- Valid window invariant: all elements in window are unique.
- Answer: maximum running sum of valid windows.
"""

from collections import defaultdict

def maximumUniqueSubarray(nums: list[int]) -> int:
    freq = defaultdict(int)
    left = 0
    max_sum = cur_sum = 0
    for right in range(len(nums)):
        cur_sum += nums[right]
        freq[nums[right]] += 1
        while freq[nums[right]] > 1:
            freq[nums[left]] -= 1
            cur_sum -= nums[left]
            left += 1
        max_sum = max(cur_sum, max_sum)
    return max_sum

