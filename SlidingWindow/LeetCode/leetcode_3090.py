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