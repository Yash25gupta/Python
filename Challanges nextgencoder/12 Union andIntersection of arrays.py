# A program which takes two array as input
# and will display two arrays with Union and Intersection of them.
#   TEST CASE:
# A - [1,3,4,5,6]   |   UNION - 1,2,3,4,5,6,8
# B - [2,3,6,4,8]   |   INTERSECTION - 3,6,4


def unionIntersection(l1, l2):
    union, intersection = l1.copy(), []
    [intersection.append(i) if i in l1 else union.append(i) for i in l2]
    return union, intersection


a = [i for i in map(int, input("enter l1 items: ").split(","))]
b = [i for i in map(int, input("enter l2 items: ").split(","))]
# b = input("enter l2 items: ").split(",")
union, intersection = unionIntersection(a, b)
print("UNION        :", union)
print("INTERSECTION :", intersection)
