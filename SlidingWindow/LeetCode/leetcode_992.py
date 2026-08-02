"""
LeetCode 992 - Subarrays with K Different Integers

Brief:
Count subarrays with exactly k distinct integers.

Sliding window idea:
- Core identity: exactly_k = at_most(k) - at_most(k - 1).
- Expand (inside at_most): move right and add current number frequency.
- Shrink (inside at_most): while distinct values exceed limit, move left and clean map.
- Counting trick: add right - left + 1 valid windows ending at each right.
"""

from collections import defaultdict

def subarraysWithKDistinct(nums: list[int], k:int) -> int:
    def atMostK(nums: list[int], _k:int) -> int:
        substringsCount = 0
        window_freq = defaultdict(int)
        left = 0
        for right in range(len(nums)):
            window_freq[nums[right]] += 1
            while len(window_freq) > _k:
                window_freq[nums[left]] -= 1
                if not window_freq[nums[left]]:
                    del window_freq[nums[left]]
                left += 1
            substringsCount += right - left + 1
        return substringsCount

    return atMostK(nums, k) - atMostK(nums, k-1)

print(subarraysWithKDistinct([1,2,1,3,4], 3))
