
def removeDuplicates(nums: list[int]) -> int:
    threshold = 1
    count = 1
    max_dup = 2
    prev = nums[0]
    for current in range(1, len(nums)):
        if nums[current] - prev == 0:
            count += 1
        else:
            count = 1
        prev = nums[current]
        if count <= max_dup:
            nums[threshold], nums[current] = nums[current], nums[threshold]
            threshold += 1
    print(nums)
    return threshold


print(removeDuplicates([1,1,1,2,2,2,3,3]))