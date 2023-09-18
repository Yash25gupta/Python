# A program which will take 1 whole number as input containing 5-9 digits and
# convert those number into words.
# INPUT - 999 < number < 1000000000
# OUTPUT - Number in Words : Five Thousand Eight Hundred Four


def getOnes(n):
    i = int(n)
    if i == 0: return ''
    elif i == 1: return 'One '
    elif i == 2: return 'Two '
    elif i == 3: return 'Three '
    elif i == 4: return 'Four '
    elif i == 5: return 'Five '
    elif i == 6: return 'Six '
    elif i == 7: return 'Seven '
    elif i == 8: return 'Eight '
    elif i == 9: return 'Nine '


def getTeens(n):
    i = int(n)
    if i < 10: return getOnes(n)
    elif i == 10: return 'Ten '
    elif i == 11: return 'Eleven '
    elif i == 12: return 'Twelve '
    elif i == 13: return 'Thirteen '
    elif i == 14: return 'Fourteen '
    elif i == 15: return 'Fifteen '
    elif i == 16: return 'Sixteen '
    elif i == 17: return 'Seventeen '
    elif i == 18: return 'Eighteen '
    elif i == 19: return 'Nineteen '


def getTens(n):
    i, txt = int(n), ''
    if i < 20: return getTeens(n)
    elif i < 30: txt = 'Twenty '
    elif i < 40: txt = 'Thirty '
    elif i < 50: txt = 'Forty '
    elif i < 60: txt = 'Fifty '
    elif i < 70: txt = 'Sixty '
    elif i < 80: txt = 'Seventy '
    elif i < 90: txt = 'Eighty '
    elif i < 100: txt = 'Ninety '
    return txt + getOnes(n[1])


def numToWords(num: int) -> str:
    """ This function convert a Whole Number into Word form.
        Input : integer
        Output: string
        Maximum number of digits allowed: 9 """
    if num == 0: return 'Zero'
    length = len(str(num))
    if length > 9: return 'Range exceeded.\nDigits should be less then 10.'
    num = '0' * (9 - length) + str(num)  # 12345 -> '000012345'
    word = ''
    if int(num[0:2]) != 0: word += getTens(num[0:2]) + 'Crore '
    if int(num[2:4]) != 0: word += getTens(num[2:4]) + 'Lakh '
    if int(num[4:6]) != 0: word += getTens(num[4:6]) + 'Thousand '
    if int(num[6]) != 0: word += getOnes(num[6]) + 'Hundred '
    if word != '': word += 'and '
    if int(num[7:]) != 0: word += getTens(num[7:])  # get Tens and Ones
    return word


num1 = 987654321
print(numToWords(num1))
