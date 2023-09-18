def numToRoman1(num):
    if not 0 < num < 10000: return 'Error'
    romanChar = ('I', 'V', 'X', 'L', 'C', 'D', 'M', "V'", "X'")
    num = ('0' * (4 - len(str(num)))) + str(num)    # 123 -> '0123'
    out = ''
    for i, n in enumerate(num):
        n = int(n)
        a, b, c = romanChar[6 - (i * 2)], romanChar[7 - (i * 2)], romanChar[8 - (i * 2)]
        if n in (0, 1, 2, 3): txt = a * n
        elif n == 4: txt = a + b
        elif n in (5, 6, 7, 8): txt = b + a * (n - 5)
        elif n == 9: txt = a + c
        out += txt
    return out


def numToRoman(num):
    ''' This function takes integer and return it in Roman Form (String). '''
    roman = {9000: "MX'", 5000: "V'", 4000: "MV'", 1000: 'M',
             900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
             90: 'XC', 50: 'L', 40: 'XL', 10: 'X',
             9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    if not 0 < num < 10000: return 'ERROR'
    out = ''
    for i in roman.keys():
        q = num // i
        num = num % i
        out += roman[i] * q
    return out


for i in (0, 24, 69, 70, 99, 102, 356, 7896, 9999):
    print(i, '->', numToRoman(i))
