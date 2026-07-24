
def longest_subarray_sum_less_s(nums: list, S: int) -> int:
    cur_sum = 0
    left = 0
    longest = 0
    for right in range(len(nums)):
        cur_sum += nums[right]
        while cur_sum > S:
            cur_sum -= nums[left]
            left += 1
        longest = max(longest, right - left + 1)
    return longest


print(longest_subarray_sum_less_s([5, -10, 5], 4))