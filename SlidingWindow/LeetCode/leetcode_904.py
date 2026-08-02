"""
LeetCode 904 - Fruit Into Baskets

Brief:
Find the longest subarray containing at most two distinct fruit types.

Sliding window idea:
- Expand: move right and update fruit frequency map.
- Shrink: while distinct types > 2, remove from left and delete zero counts.
- Valid window invariant: at most two distinct fruit values in window.
- Answer: maximum valid window length.
"""

from collections import defaultdict

def totalFruit(fruits: list[int]) -> int:
    max_types = 2
    fruits_freq = defaultdict(int)
    max_fruits = 0
    cur_types = 0
    left = 0
    for right in range(len(fruits)):
        fruits_freq[fruits[right]] += 1
        if fruits_freq[fruits[right]] == 1:
            cur_types += 1
        while cur_types > max_types:
            fruits_freq[fruits[left]] -= 1
            if not fruits_freq[fruits[left]]:
                cur_types -= 1
            left += 1
        max_fruits = max(max_fruits, right - left + 1)
    return max_fruits
