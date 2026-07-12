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

