
"""
LeetCode 1208 - Get Equal Substrings Within Budget

Brief:
Find the longest substring you can transform from s to t with total conversion cost <= maxCost.

Sliding window idea:
- Expand: include s[right] and t[right], add their char distance to current_cost.
- Shrink: while current_cost > maxCost, remove left pair cost and advance left.
- Valid window invariant: current_cost <= maxCost.
- Answer: maximum valid window length.
"""

def equalSubstring(s: str, t: str, maxCost: int) -> int:
    def get_cost(c1: str, c2: str) -> int:
        return abs(ord(c1) - ord(c2))
    current_cost = 0
    left = 0
    max_len = 0
    for right in range(len(s)):
        current_cost += get_cost(s[right], t[right])
        while current_cost > maxCost:
            current_cost -= get_cost(s[left], t[left])
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len


print(equalSubstring("abcd", "acde", 0))
