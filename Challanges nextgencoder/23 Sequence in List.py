# A program which will take one list of number as input and find all sequences in the list
# which are in ascending order, then find addition of numbers of each sequence and
# gives largest addition between sequences as output
#                   TEST CASES:
#           INPUT                   OUTPUT
#   [1,9,7,3,2,3,7,2,1,4,5,6]         16
#   [9,8,7,6,5,4,3,2,1]               0
#   [1,2,3,4,5,6,7,8,9]               45
#   []                                0


def largestSum(lst):
    lst.append(0)
    sequence, sequences = [], []
    for i in range(1, len(lst)):
        sequence.append(lst[i - 1])
        if lst[i - 1] > lst[i]:
            if len(sequence) > 1: sequences.append(sequence.copy())
            sequence.clear()
    if len(sequence) > 1: sequences.append(sequence.copy())
    sum_list = [sum(seq) for seq in sequences]
    return (max(sum_list), sum_list, sequences) if sequences else (0, None, None)
    # # If want maxSum Only
    # total_list = []
    # total = 0
    # for i in range(1, len(lst)):
    #     total += lst[i - 1]
    #     if lst[i - 1] > lst[i]:
    #         if total > lst[i - 1]: total_list.append(total)
    #         total = 0
    # return max(total_list) if total_list else 0


l0 = [4, 5, 6, 2, 1, 2, 3, 4, 12, 6, 4, 2, 1, 5, 8, 9]
l1 = [1, 9, 7, 3, 2, 3, 7, 2, 1, 4, 5, 6]
l2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
l3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l4 = []
main = (l0, l1, l2, l3, l4)
for i in main:
    maxSum, sumList, sequ = largestSum(i)
    print(i)
    print(f'Sequences: {sequ}\nSumList: {sumList}\nMaxSum: {maxSum}\n')
