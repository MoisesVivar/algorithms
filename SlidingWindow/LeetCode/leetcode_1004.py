
def lognestOnes(nums: list[int], k: int) -> int:
    left = 0
    zero_count = 0
    max_ones = 0
    for right in range(len(nums)):
        if not nums[right]:
            zero_count += 1
        while zero_count > k:
            if not nums[left]:
                zero_count -= 1
            left += 1
        max_ones = max(max_ones, right - left + 1)
    return max_ones

print(lognestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))