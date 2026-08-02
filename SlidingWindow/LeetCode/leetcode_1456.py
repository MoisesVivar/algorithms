
"""
LeetCode 1456 - Maximum Number of Vowels in a Substring of Given Length

Brief:
Return the maximum number of vowels in any substring of size k.

Sliding window idea:
- Expand: include right character and increment current vowel count if needed.
- Shrink: if window size exceeds k, remove left character contribution.
- Fixed-size window invariant: window size is kept at most k.
- Answer: best vowel count when window size is exactly k.
"""

def maxVowels(s: str, k: int) -> int:

    def isVowel(s: str) -> bool:
        return s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u'

    left = 0
    max_vowels = 0
    cur_max = 0
    for right in range(len(s)):
        if isVowel(s[right]):
            cur_max += 1
        if right - left + 1 > k:
            if isVowel(s[left]):
                cur_max -= 1
            left += 1
        if right - left + 1 == k:
            max_vowels = max(cur_max, max_vowels)
    return max_vowels

print(maxVowels('abciiidef', 3))






