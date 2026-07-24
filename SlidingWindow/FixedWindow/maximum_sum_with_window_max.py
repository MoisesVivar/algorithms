from collections import deque

def maximum_sum_with_window_max(nums: list, k: int, m: int) -> int:
    cur_sum = 0
    max_sum = float('-inf')
    left = 0
    q = deque()
    for right in range(len(nums)):
        while q and nums[q[-1]] < nums[right]:
            q.pop()
        q.append(right)

        cur_sum += nums[right]
        if right - left + 1 > k:
            cur_sum -= nums[left]
            left += 1
            if q[0] < left:
                q.popleft()
        if right - left + 1 == k and nums[q[0]] <= m:
            max_sum = max(cur_sum, max_sum)
    return max_sum if max_sum != float('-inf') else -1


print(maximum_sum_with_window_max([4, 9, 2, 3, 8, 1, 7, 6], 3, 5))