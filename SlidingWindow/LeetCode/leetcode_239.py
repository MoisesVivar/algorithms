"""
LeetCode 239 - Sliding Window Maximum

Brief:
Return the maximum value in every contiguous subarray of size k.

Sliding window idea:
- Expand: move right and keep a decreasing deque of indices by value.
- Shrink: when window exceeds k, pop left index if it leaves the window.
- Deque invariant: front index always points to current window maximum.
- Answer: append nums[deque_front] whenever window size is k.
"""

from collections import deque

def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    max_window = []
    q = deque()
    left = 0
    for right in range(len(nums)):
        while q and nums[q[-1]] < nums[right]:
            q.pop()
        q.append(right)
        if right - left + 1 > k:
            if q[0] == left:
                q.popleft()
            left += 1
        if right - left + 1 == k:
            max_window.append(nums[q[0]])
    return max_window
