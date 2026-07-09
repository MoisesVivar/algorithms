
def longest_substring(s: str) -> int:
    from collections import defaultdict
    frequency = defaultdict(int)
    count = 0
    n = 3
    if len(s) < 3:
        return 0
    has_duplicate = False
    for i in range(n):
        frequency[s[i]] += 1
        if frequency[s[i]] >= 2:
            has_duplicate = True
    if not has_duplicate:
        count += 1
    has_duplicate = False
    left = 1
    for right in range(n, len(s)):
        frequency[s[left - 1]] -= 1
        if frequency[s[left - 1]] == 0:
            del frequency[s[left -1]]
        frequency[s[right]] += 1
        if frequency[s[left]] >= 2 or frequency[s[left+1]] >= 2 or frequency[s[right]] >= 2:
            has_duplicate = True
        if not has_duplicate:
            count += 1
        has_duplicate = False
        left += 1
    return count

_s = "ylqosyvvmroovnulaesxeghhhcvuagiicrbujm"
print(longest_substring(_s))



