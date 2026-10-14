"""
LeetCode 11 - Container With Most Water

Brief:
Given vertical line heights, pick two lines that together with the x-axis hold the most water.

Two pointers idea:
- Start with pointers at both ends (widest container).
- Area = width * min(height[left], height[right]).
- Move the pointer at the shorter line inward: moving the taller one can only shrink width without raising the limiting height.
- Answer: the largest area seen.
"""

def maxArea(height: list[int]) -> int:
    left = 0
    right = len(height) - 1
    max_area = 0
    while left < right:
        max_area = max((right - left) * min(height[left], height[right]), max_area)
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1
    return max_area


print(maxArea([1,8,6,2,5,4,8,3,7]))
