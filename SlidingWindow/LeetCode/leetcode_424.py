
"""
LeetCode 424 - Longest Repeating Character Replacement

Brief:
Find the longest substring you can make all one letter by replacing at most k chars.

Sliding window idea:
- Expand: move right and update character frequencies.
- Shrink: if (window_size - highest_char_freq) > k, move left and reduce freq.
- Valid window invariant: needed replacements <= k.
- Answer: maximum valid window length.
"""


def characterReplacement(s: str, k: int) -> int:
    def char_index(c: str) -> int:
        return ord(c) - ord('A')

    window_freq = 26 * [0]
    left = 0
    longest_seq = 0
    for right in range(len(s)):
        window_freq[char_index(s[right])] += 1
        flips = (right - left + 1) - max(window_freq)
        while flips > k:
            window_freq[char_index(s[left])] -= 1
            left += 1
            flips = (right - left + 1) - max(window_freq)
        longest_seq = max(longest_seq, right - left + 1)
    return longest_seq


print(characterReplacement("AABABBA", 1))



