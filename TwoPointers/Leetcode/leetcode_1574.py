
def findLengthOfShortestSubarray(arr: list[int]) -> int:
    n = len(arr)
    for left_limit in range(n):
        if left_limit == n - 1:
            return 0
        if arr[left_limit] > arr[left_limit + 1]:
            break
    for right_limit in range(n - 1, left_limit, -1):
        if arr[right_limit] < arr[right_limit - 1]:
            break
    left = left_limit
    right = right_limit
    max_len = (right_limit - left_limit - 1) + min(left_limit + 1, n - right_limit)
    while (right - left - 1) < max_len:
        if arr[left] <= arr[right]:
            return right - left - 1
        else:
            if right < n - 1 and arr[left] <= arr[right + 1]:
                return right + 1 - left - 1
            if left > 0 and arr[left - 1] <= arr[right]:
                return right - (left - 1) - 1
            right += 1
            left -= 1
    return max_len


print(findLengthOfShortestSubarray([5,16,19,20,18,10,8,4,3,4,0,10,21]))

