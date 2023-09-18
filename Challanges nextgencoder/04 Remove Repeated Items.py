# Take list as input and remove all duplicate items
# Input : ["Next", "Gen", "Next", "Coder"]
# Output : ["Next", "Gen", "Coder"]


def removeDuplicate(lst):
    new_lst = []
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)
    return new_lst


lst = list(input("Enter values sep by comma: ").split(","))

print(lst)

print(removeDuplicate(lst))

print(set(lst))
