
"""
LeetCode 1358 - Number of Substrings Containing All Three Characters

Brief:
Count substrings that contain at least one 'a', one 'b', and one 'c'.

Sliding window idea:
- Expand: move right and update frequency of a/b/c.
- Shrink: while window is valid (all 3 present), add len(s) - right to answer,
  then move left to find the next smaller valid window.
- Counting trick: if [left..right] is valid, every extension to the right is also valid.
"""

def numberOfSubstrings(s: str) -> int:
    def char_index(c: str):
        return ord(c) - ord('a')

    window_freq = 3 * [0]
    substring_count = 0
    left = 0
    for right in range(len(s)):
        window_freq[char_index(s[right])] += 1
        while window_freq[0] >= 1 and window_freq[1] >= 1 and window_freq[2] >= 1:
            substring_count += len(s) - right
            window_freq[char_index(s[left])] -= 1
            left += 1
    return substring_count