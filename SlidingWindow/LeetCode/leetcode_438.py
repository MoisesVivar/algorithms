
"""
LeetCode 438 - Find All Anagrams in a String

Brief:
Return all start indices where an anagram of p appears in s.

Sliding window idea:
- Expand: move right and add current char to window frequency.
- Shrink: if window size exceeds len(p), remove left char.
- Fixed-size window invariant: compare only windows of length len(p).
- Answer: record left index whenever window_freq equals p_freq.
"""

def findAnagrams(s: str, p: str) -> list[int]:
    indices = []
    def char_index(c: str) -> int:
        return ord(c) - ord('a')
    p_freq = 26*[0]
    window_freq = 26*[0]
    for e in p:
        p_freq[char_index(e)] += 1
    left = 0
    k = len(p)
    for right in range(len(s)):
        window_freq[char_index(s[right])] += 1
        if right - left + 1 > k:
            window_freq[char_index(s[left])] -= 1
            left += 1
        if right - left + 1 == k:
            if window_freq == p_freq:
                indices.append(left)
    return indices

