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
