
def numSubarrayProductLessThanK(nums: list[int], k: int) -> int:
    count = 0
    window_prod = 1
    left = 0
    for right in range(len(nums)):
        window_prod *= nums[right]
        while window_prod >= k and left <= right:
            window_prod //= nums[left]
            left += 1
        if left > right:
            continue
        count += right - left + 1
    return count


print(numSubarrayProductLessThanK([10**9] * 100, 10**18))
