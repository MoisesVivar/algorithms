from collections import defaultdict

def longest_substring_atmost_k_distinct(s: str, k: int) -> int:
    freq = defaultdict(int)
    cur_longest = 0
    cur_dist = 0
    left = 0
    for right in range(len(s)):
        freq[s[right]] += 1
        if freq[s[right]] == 1:
            cur_dist +=1
        while cur_dist > k:
            freq[s[left]] -= 1
            if not freq[s[left]]:
                cur_dist -= 1
            left += 1
        cur_longest = max(cur_longest, right - left + 1)
    return cur_longest


print(longest_substring_atmost_k_distinct("🙂🙃🙂😎🙃🙂", 2))


