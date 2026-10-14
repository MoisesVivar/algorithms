
def trap(height: list[int]) -> int:
    n = len(height)
    count = 0
    if n <= 2:
        return count
    left = 0
    right = len(height) - 1
    left_tallest = 0
    right_tallest = len(height) - 1
    while left < right:
        if height[left_tallest] <= height[right_tallest]:
            left += 1
            if height[left] < height[left_tallest]:
                count += height[left_tallest] - height[left]
            else:
                left_tallest = left
        else:
            right -= 1
            if height[right] < height[right_tallest]:
                count += height[right_tallest] - height[right]
            else:
                right_tallest = right
    return count

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))