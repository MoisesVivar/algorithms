"""
LeetCode 977 - Squares of a Sorted Array

Brief:
Given a sorted array (possibly with negatives), return the squares of each number in sorted order.

Two pointers idea:
- The largest square is always at one of the two ends (most negative or most positive).
- Compare squares at left and right, write the larger one at the end of the result, and move that pointer inward.
- Fill the result array from back to front.
- Answer: the result array, built in O(n) without sorting.
"""

def sortedSquares(nums: list[int]) -> list[int]:
    res = [0] * len(nums)
    left = 0
    right = len(nums) - 1
    while left <= right:
        if nums[left] ** 2 <= nums[right] ** 2:
            res[right - left] = nums[right] ** 2
            right -= 1
        else:
            res[right - left] = nums[left] ** 2
            left += 1
    return res


print(sortedSquares([-7, -3, 2, 3, 11]))
