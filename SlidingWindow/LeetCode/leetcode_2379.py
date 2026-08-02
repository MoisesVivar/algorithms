
"""
LeetCode 2379 - Minimum Recolors to Get K Consecutive Black Blocks

Brief:
Find the minimum number of recolors needed so some length-k window becomes all black.

Sliding window idea:
- Expand: move right and count whites in the current window.
- Shrink: when window size exceeds k, remove left character contribution.
- Fixed-size window invariant: keep window size equal to k.
- Answer: minimum white count among all size-k windows.
"""

def minimumRecolors(blocks: str, k: int) -> int:
    left = 0
    whites = 0
    min_whites = float('inf')
    for right in range(len(blocks)):
        if blocks[right] == 'W':
            whites += 1
        if right - left + 1 > k:
            if blocks[left] == 'W':
                whites -= 1
            left += 1
        if right - left + 1 == k:
            min_whites = min(min_whites, whites)
    return min_whites


print(minimumRecolors("WBWBBBW", 2))
