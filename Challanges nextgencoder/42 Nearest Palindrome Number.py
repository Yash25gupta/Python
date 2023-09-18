def isPalindrome(num):
    return str(num) == str(num)[::-1]


def nearestPalindrome(num, d=0):
    if isPalindrome(num + d): return num + d
    if isPalindrome(num - d): return num - d
    return nearestPalindrome(num, d + 1)


for i in (120, 1228, 3773):
    print(nearestPalindrome(i))
