# Create a random list of even/odd numbers.
# Ask user for a number b/w 0 to 100 to check wheather their no is in list.
# Working
# Check for middle element.
# 1.) If num = middle element --> return True
# 2.) If num < middle element --> new arrar = arr[0:mid]
# 3.) If num > middle element --> new arrar = arr[mid:]
# Repeat

def binarysearch(arr, num):
    low = 0
    high = len(arr)
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == num:
            return True, mid
        elif arr[mid] < num:
            low = mid+1
        else:
            high = mid-1
    return False

nums = list(range(2,100,2))
# print(nums)
n = int(input('Enter a number b/w 1 to 100. : '))
print(binarysearch(nums, n))

# Bubble Sort
def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(arr)

# Recursive Bubble Sort
def recursivebubblesort(arr):
    for i, num in enumerate(arr):
        try:
            if arr[i+1] < num:
                arr[i] = arr[i+1]
                arr[i+1] = num
                print(arr)
                recursivebubblesort(arr)
        except IndexError:
            pass
    return arr

arr = [90,64,34,25,22,12,11]
print('Unsorted array is : ')
print(arr)
# bubblesort(arr)
recursivebubblesort(arr)
print('Sorted array is : ')
print(arr)

