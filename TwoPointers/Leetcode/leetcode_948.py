
def bagOfTokensScore(tokens: list[int], power: int) -> int:
    score = 0
    tokens.sort()
    left, right = 0, len(tokens) - 1
    while left <= right:
        if score >= 0 and power >= tokens[left]:
            ## face up
            score += 1
            power -= tokens[left]
            left += 1
        elif score > 0 and power < tokens[left] and left < right:
            ## face down
            score -= 1
            power += tokens[right]
            right -= 1
        else:
            break
    return score

print(bagOfTokensScore([200,100], 150))
