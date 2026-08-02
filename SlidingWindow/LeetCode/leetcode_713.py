
"""
LeetCode 713 - Subarray Product Less Than K

Brief:
Count subarrays with product strictly less than k.

Sliding window idea:
- Expand: multiply by nums[right] to include right element.
- Shrink: while product >= k, divide by nums[left] and move left.
- Valid window invariant: product of window < k.
- Counting trick: for each right, add (right - left + 1) valid subarrays ending at right.
"""

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
