
def minSubArrayLen(target: int, nums: list[int]) -> int:
    min_len = float('inf')
    left = 0
    _sum = 0
    for right in range(len(nums)):
        _sum += nums[right]
        while _sum >= target:
            min_len = min(min_len, right - left + 1)
            _sum -= nums[left]
            left += 1
        if min_len == 1:
            return 1
    return min_len if min_len != float('inf') else 0

print(minSubArrayLen(4, [1,4,4]))


