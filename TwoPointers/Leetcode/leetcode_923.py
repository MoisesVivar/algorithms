"""
LeetCode 923 - 3Sum With Multiplicity

Brief:
Count the index triples i < j < k whose values sum to the target (modulo 10^9 + 7).

Two pointers idea:
- Sort the array, fix arr[i], and run left/right pointers over the rest as in 3Sum.
- On a match, count the run of equal values on each side.
- If both sides hold the same value, add C(n, 2) = n * (n - 1) / 2 pairs; otherwise add left_count * right_count.
- Answer: the total count modulo 10^9 + 7.
"""

def threeSumMulti(arr: list[int], target: int) -> int:
    arr.sort()
    count = 0
    for i in range(len(arr) - 2):
        j = i + 1
        k = len(arr) - 1
        cur_max_sum = arr[i] + arr[k] + arr[k - 1]
        cur_min_sum = arr[i] + arr[j] + arr[j + 1]
        if cur_max_sum < target or cur_min_sum > target:
            continue
        while j < k:
            cur_sum = arr[i] + arr[j] + arr[k]
            if cur_sum < target:
                j += 1
            elif cur_sum > target:
                k -= 1
            else:
                j_val = arr[j]
                j += 1
                j_count = 1
                while j <= k and arr[j] == arr[j - 1]:
                    j += 1
                    j_count += 1
                k_val = arr[k]
                k -= 1
                k_count = 1
                while j <= k and arr[k] == arr[k + 1]:
                    k -= 1
                    k_count += 1
                if j_val == k_val:
                    count += j_count * (j_count - 1) // 2
                else:
                    count += j_count * k_count
    return count % (10 ** 9 + 7)


print(threeSumMulti([1, 1, 2, 2, 2, 2], 5))
