from collections import defaultdict

def longest_substring_without_repeating_chars(s: str) -> int:
    freq = defaultdict(int)
    left = 0
    cur_longest = 0
    for right in range(len(s)):
        freq[s[right]] += 1
        while freq[s[right]] > 1:
            freq[s[left]] -= 1
            left += 1
        cur_longest = max(cur_longest, right - left + 1)
    return cur_longest


print(longest_substring_without_repeating_chars("🙂🙃🙂🙂🙃😎"))