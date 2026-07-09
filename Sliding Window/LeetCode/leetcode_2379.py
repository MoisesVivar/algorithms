
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
