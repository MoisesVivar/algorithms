

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



