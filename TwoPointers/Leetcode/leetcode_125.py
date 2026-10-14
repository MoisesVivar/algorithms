

"""
LeetCode 125 - Valid Palindrome

Brief:
Check whether a string reads the same forwards and backwards, ignoring case and non-alphanumeric characters.

Two pointers idea:
- Start with pointers at both ends and move them toward each other.
- Skip any non-alphanumeric character on either side.
- Compare the characters case-insensitively; any mismatch means not a palindrome.
- Answer: True if the pointers meet without a mismatch.
"""

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
