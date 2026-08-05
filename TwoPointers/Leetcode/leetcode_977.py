
def sortedSquares(nums: list[int]) -> list[int]:
    res = [0] * len(nums)
    left = 0
    right = len(nums) - 1
    while left <= right:
        if nums[left] ** 2 <= nums[right] ** 2:
            res[right - left] = nums[right] ** 2
            right -= 1
        else:
            res[right - left] = nums[left] ** 2
            left += 1
    return res


print(sortedSquares([-7, -3, 2, 3, 11]))
