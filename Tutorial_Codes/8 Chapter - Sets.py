# Tutorial 126 - Intro to Sets
# set data type
# unordered collection of unique items
# we cant store list, dictionary, tuple, set, etc in a set

s = {1, 2, 3, 4, 3}
# print(s[1])        # no indexing can done

# l = [1,2,1,3,4,3,4,5,4,6,5,2]
# l = list(set(l))        # generate list with unique items
# print(l)

s.add(5)                # add item to set
# s.remove(3)             # if not in set, generate error
s.discard(3)            # if not in set, no error
# s.clear()               # clear set
print(s)


# Tutorial 127 - More about sets
# in keyword in sets and for Loop
s = {'a', 'b', 'c'}

if 'a' in s:
    print('present')
else:
    print('not present')

# for loop
for item in s:
    print(item)

# se maths
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(s1 | s2)        # union of sets
print(s1 & s2)        # intersection
