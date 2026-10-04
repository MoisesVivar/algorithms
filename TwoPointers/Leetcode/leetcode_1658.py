
def minOperations(nums: list[int], x: int) -> int:
    n = len(nums)
    target = sum(nums) - x

    if target == 0:
        return n
    if target < 0:
        return - 1

    window_sum = 0
    max_window = 0
    left = 0

    for right in range(len(nums)):
        window_sum += nums[right]
        while window_sum > target:
            window_sum -= nums[left]
            left += 1
        if window_sum == target:
            max_window = max(max_window, right - left + 1)

    return n - max_window if max_window else - 1


print(minOperations([3,2,20,1,1,3], 10))
