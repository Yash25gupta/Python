# A program which will take 1 array of marks of 5 students as input and
# display an array of candies distributes to them based on their marks (Max 15 Candies)
#   TEST CASE:
# INPUT - [1,9,7,3,2]       |   [8,2,5,2,7]
# OUTPUT - [1,5,4,2,2]      |   [4,2,3,2,4]


def distributeCandies(lst, CANDIES):
    return [round(i / sum(lst) * CANDIES) for i in lst]


lst = [8, 2, 5, 2, 7]
print(distributeCandies(lst, 15))
