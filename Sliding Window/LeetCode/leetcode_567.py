
def checkInclusion(s1: str, s2: str) -> bool:
    def get_char_index(c: str) -> int:
        return ord(c) - ord('a')
    # s1 frequency
    s1_freq = [0]*26
    for c in s1:
        s1_freq[get_char_index(c)] += 1

    # s2 frequency
    window_freq = [0]*26

    # sliding window
    left = 0
    k = len(s1)
    for right in range(len(s2)):
        window_freq[get_char_index(s2[right])] += 1
        if right - left + 1 > k:
            window_freq[get_char_index(s2[left])] -= 1
            left += 1
        if right - left + 1 == k:
            if window_freq == s1_freq:
                return True
    return False

print(checkInclusion("adc", "dcda"))


