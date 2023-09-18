# A program which will take one list of string as input For Eg -> ['A', 'B', 'B', 'C']
# and Output the most repeated string from list (in above eg -> 'B')
# and if most repeated string is more than 1 then None should be print
#                   TEST CASES:
#           INPUT              OUTPUT
#   ['A', 'B', 'C', 'A']        'A'
#   ['A', 'B', 'B', 'A']        'None'
#   ['A', 'B', 'C', 'D']        'None'
#   []                          'None'
#   ['A', 'A', 'A', 'A']        'A'


def mostRepeated(lst):
    dic = {i: lst.count(i) for i in lst}
    max_count = max(dic.values()) if dic else 0
    out = [k for k, v in dic.items() if v == max_count]
    return out[0] if len(out) == 1 else 'None'


l1 = ['A', 'B', 'C', 'A']
l2 = ['A', 'B', 'B', 'A']
l3 = ['A', 'B', 'C', 'D']
l4 = []
l5 = ['A', 'A', 'A', 'A']
mainList = [l1, l2, l3, l4, l5]
for l in mainList:
    print(mostRepeated(l))
