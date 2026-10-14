"""
LeetCode 948 - Bag of Tokens

Brief:
Starting with some power and score 0, play tokens face up (spend power, gain 1 score) or face down (spend 1 score, gain power) to maximize score.

Two pointers idea:
- Sort the tokens: cheapest on the left, most valuable on the right.
- Face up the cheapest token (left) when power allows it.
- Otherwise, if there is score to spend, face down the most expensive token (right) to gain the most power.
- Stop when neither move is possible; answer: the score reached.
"""

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
