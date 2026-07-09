
def distinct_elements_subarr(arr: list, k: int) -> list:
    from collections import defaultdict
    left = 0
    cur_count = 0
    distinct = []
    frequency = defaultdict(int)
    for right in range(len(arr)):
        if not frequency[arr[right]]:
            cur_count += 1
        frequency[arr[right]] += 1
        if right - left + 1 > k:
            frequency[arr[left]] -= 1
            if frequency[arr[left]] < 1:
                cur_count -= 1
            left += 1
        if right - left + 1 == k:
            distinct.append(cur_count)
    return distinct


print(distinct_elements_subarr([1, 2, 1, 3, 4, 2, 3], 4))

