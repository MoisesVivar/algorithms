
def findLengthOfShortestSubarray(arr: list[int]) -> int:
    n = len(arr)

    left_limit = 0
    while left_limit + 1 < n and arr[left_limit] <= arr[left_limit + 1]:
        left_limit += 1
    if left_limit == n - 1:
        return 0

    right_limit = n - 1
    while right_limit > 0 and arr[right_limit] >= arr[right_limit - 1]:
        right_limit -= 1

    left, right = 0, right_limit
    min_len = n - max(left_limit + 1, n - right_limit)
    while left <= left_limit and right <= n - 1:
        if arr[left] <= arr[right]:
            min_len = min(min_len, right - left - 1)
            left += 1
        else:
            right += 1
    return min_len


print(findLengthOfShortestSubarray([1,8,34,2,3,22,18,27,3,1,0,12,21,23,8,7,17]))

