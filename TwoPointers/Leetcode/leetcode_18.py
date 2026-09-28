
def fourSum(nums: list[int], target: int) -> list[list[int]]:
    if len(nums) < 4: return []
    nums.sort()
    quadruplets = []
    i = 0
    while i < len(nums) - 3:
        j = i + 1
        while j < len(nums) - 2:
            k = j + 1
            l = len(nums) - 1
            cur_min_sum = nums[i] + nums[j] + nums[k] + nums[k + 1]
            cur_max_sum = nums[i] + nums[j] + nums[l] + nums[l - 1]
            if cur_min_sum > target or cur_max_sum < target:
                j += 1
                while nums[j] == nums[j - 1] and j < len(nums) - 2: j += 1
                continue
            while k < l:
                cur_sum = nums[i] + nums[j] + nums[k] + nums[l]
                if cur_sum < target:
                    k += 1
                elif cur_sum > target:
                    l -= 1
                else:
                    quadruplets.append([nums[i], nums[j], nums[k], nums[l]])
                    k += 1
                    while nums[k] == nums[k - 1] and k < l: k += 1
                    l -= 1
                    while nums[l] == nums[l + 1] and k < l: l -= 1
            j += 1
            while nums[j] == nums[j - 1] and j < len(nums) - 2: j += 1
        i += 1
        while nums[i] == nums[i - 1] and i < len(nums) - 3: i += 1
    return quadruplets


print(fourSum([1,0,-1,0,-2,2], 0))
