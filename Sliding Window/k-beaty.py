

def divisor_substrings(num: int, k: int) -> int:
    _num = str(num)
    count = 0
    for right in range(len(_num) - k + 1):
        current_num = str(_num[right: right+k])
        if int(current_num) != 0 and num % int(current_num) == 0:
            count += 1
    return count


print(divisor_substrings(430043, 2))
