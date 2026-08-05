

def isPalindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1
    while left < right:
        if not s[left].isalnum() and left < len(s) - 1:
            left += 1
            continue
        if not s[right].isalnum() and right > 0:
            right -= 1
            continue
        if s[left].lower() == s[right].lower():
            left += 1
            right -= 1
        else:
            return False
    return True


print(isPalindrome("race a car"))
