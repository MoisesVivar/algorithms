"""
LeetCode 3090 - Maximum Length Substring With Two Occurrences

Brief:
Find the longest substring where each character appears at most twice.

Sliding window idea:
- Expand: move right and increment frequency of s[right].
- Shrink: while freq of s[right] exceeds 2, move left and decrement frequencies.
- Valid window invariant: every character count in window is <= 2.
- Answer: maximum valid window length.
"""

from collections import defaultdict

def maximumLengthSubstring(s: str) -> int:
    left = 0
    freq = defaultdict(int)
    longest = 0
    for right in range(len(s)):
        freq[s[right]] += 1
        while freq[s[right]] > 2:
            freq[s[left]] -= 1
            left += 1
        longest = max(longest, right - left + 1)
    return longest


print(maximumLengthSubstring("bcbbbcba"))