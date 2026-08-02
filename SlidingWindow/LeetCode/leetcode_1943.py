
"""
LeetCode 1493 - Longest Subarray of 1's After Deleting One Element
Note: file is named leetcode_1943.py, but the implemented logic matches 1493.

Brief:
Find the longest subarray of 1s you can obtain after deleting exactly one element.

Sliding window idea:
- Expand: move right and count zeros in the window.
- Shrink: while zero count > 1, move left and remove zeros passed.
- Valid window invariant: window contains at most one zero (the deletable element).
- Answer: right - left (window length minus one deleted element).
"""

def longestSubarray(nums: list[int]) -> int:
    deleted = 0
    left = 0
    longest = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            deleted += 1
        while deleted > 1:
            if nums[left] == 0:
                deleted -= 1
            left += 1
        longest = max(longest, right - left)
    return longest


print(longestSubarray([1,1,1]))
