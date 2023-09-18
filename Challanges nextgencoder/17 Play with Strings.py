# A Program which will take 1 string containing char-A & B and integers which
# adds 1 to the digit followed by 'A' and subtract 1 from digit followed by 'B'.
#          TEST CASES:
#     INPUT          OUTPUT
#   '2A53B24'       '26314'
#   '3A95A48A'      '310558'
#   '7A86B9B0'      '7968'


def myFunc(string):
    i, s = 0, ''
    try:
        while i < len(string):
            if string[i] not in 'AB': s += string[i]
            else:
                val = int(string[i + 1]) + (1 if string[i] == 'A' else -1)
                s += str(val) if val != -1 else ''
                i += 1
            i += 1
    finally:
        return s


s1 = '2A53B24'
s2 = '3A95A48A'
s3 = '7A86B9B0'
print(myFunc(s1))
print(myFunc(s2))
print(myFunc(s3))
