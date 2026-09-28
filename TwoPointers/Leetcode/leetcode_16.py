
def threeSumClosest(nums: list[int], target: int) -> int:
    nums.sort()
    closest = nums[0] + nums[1] + nums[2]
    i = 0
    while i < len(nums) - 2:
        j = i + 1
        k = len(nums) - 1
        while j < k:
            cur_sum = nums[i] + nums[j] + nums[k]
            closest = cur_sum if abs(cur_sum - target) < abs(closest - target) else closest
            if cur_sum < target:
                j += 1
            elif cur_sum > target:
                k -= 1
            else:
                return cur_sum
        i += 1
        while nums[i] == nums[i-1] and i < len(nums) - 2:
            i += 1
    return closest


print(threeSumClosest([1,1,1,0], -100))