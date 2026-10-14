"""
LeetCode 15 - 3Sum

Brief:
Find all unique triplets in the array that sum to zero.

Two pointers idea:
- Sort the array, then fix one element nums[i] and look for a pair summing to -nums[i].
- Pair search: left pointer j after i, right pointer k at the end; sum too small -> j++, too big -> k--.
- On a match, record the triplet and move both pointers.
- Skip duplicate values for i, j and k to avoid repeated triplets.
"""

def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    triplets = []
    i = 0
    while i < len(nums) - 2:
        j = i + 1
        k = len(nums) - 1
        target = -nums[i]
        while j < k:
            if nums[j] + nums[k] > target:
                k -= 1
            elif nums[j] + nums[k] < target:
                j += 1
            else:
                triplets.append([nums[i], nums[j], nums[k]])
                j += 1
                while nums[j] == nums[j-1] and j < k:
                    j += 1
                k -= 1
                while nums[k] == nums[k+1] and j < k:
                    k -= 1
        i += 1
        while nums[i] == nums[i-1] and i < len(nums) - 2:
            i += 1
    return triplets


print(threeSum([-1,0,1,2,-1,-4]))
