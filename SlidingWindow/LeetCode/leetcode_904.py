from collections import defaultdict

def totalFruit(fruits: list[int]) -> int:
    max_types = 2
    fruits_freq = defaultdict(int)
    max_fruits = 0
    cur_types = 0
    left = 0
    for right in range(len(fruits)):
        fruits_freq[fruits[right]] += 1
        if fruits_freq[fruits[right]] == 1:
            cur_types += 1
        while cur_types > max_types:
            fruits_freq[fruits[left]] -= 1
            if not fruits_freq[fruits[left]]:
                cur_types -= 1
            left += 1
        max_fruits = max(max_fruits, right - left + 1)
    return max_fruits
