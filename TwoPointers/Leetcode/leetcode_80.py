"""
LeetCode 80 - Remove Duplicates from Sorted Array II

Brief:
In a sorted array, modify it in place so each value appears at most twice, and return the new length.

Two pointers idea:
- A reader pointer (current) scans the array while a writer pointer (threshold) marks the next slot to fill.
- Track how many times the current value has repeated in a row.
- If the run count is <= 2, place the element at the writer slot and advance it.
- Answer: the writer index, i.e. the length of the valid prefix.
"""

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