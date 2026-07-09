from collections import defaultdict

def maximum_score(nums: list, k: int, p: int) -> int:
    freq = defaultdict(int)
    left = 0
    cur_sum = 0
    cur_dist = 0
    cur_max = float('-inf')
    for right in range(len(nums)):
        cur_sum += nums[right]
        freq[nums[right]] += 1
        if freq[nums[right]] == 1:
            cur_dist += 1
        if right - left + 1 > k:
            cur_sum -= nums[left]
            freq[nums[left]] -= 1
            if freq[nums[left]] < 1:
                cur_dist -= 1
            left += 1
        if right - left + 1 == k:
            cur_max = max(cur_sum - p*cur_dist, cur_max)
    return cur_max


print(maximum_score([1,1,1], 3, 10))


