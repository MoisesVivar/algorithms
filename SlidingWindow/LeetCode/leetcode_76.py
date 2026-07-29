
def minWindow(s: str, t: str) -> str:
    def get_index(c: str) -> int:
        index = ord(c) - ord('A')
        return index - 6 if c.islower() else index

    t_freq = 26 * 2 * [0]
    window_freq = 26 * 2 * [0]
    for c in t:
        t_freq[get_index(c)] += 1

    def isWindowValid(window: list[int]) -> bool:
        for i in range(26 * 2):
            if window[i] < t_freq[i]:
                return False
        return True

    left = 0
    min_indexes = (0, float('inf'))
    for right in range(len(s)):
        if t_freq[get_index(s[right])]:
            window_freq[get_index(s[right])] += 1
        while isWindowValid(window_freq):
            # Record minimum substring indexes
            if (right - left + 1) < (min_indexes[1] - min_indexes[0] + 1):
                min_indexes = (left, right)
            if t_freq[get_index(s[left])]:
                window_freq[get_index(s[left])] -= 1
            left += 1
    return s[min_indexes[0]: min_indexes[1] + 1] if min_indexes[1] != float('inf') else ''


print(minWindow("cabwefgewcwaefgcf", "cae"))
