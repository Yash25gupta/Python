n = int(input('Enter number of rows : '))

# # Armstrong numbers     --->    number of n digits which are equal to sum of nth power of its digits
# # 13579                 --->    n = 5, sum = 1*5 + 3*5 + 5*5 + 7*5 + 9*5

# # my approach
# lst = []
# for i in range(1000):
#     total = 0
#     n = len(str(i))
#     for j in range(n):
#         digit = int(str(i)[j])
#         total += digit**n
#     if total == i:
#         lst.append(i)
# print(lst)

# # Video approach
# lst2 = []
# for i in range(1000):
#     num = i
#     total = 0
#     n = len(str(i))
#     while i != 0:
#         digit = i % 10
#         total += digit**n
#         i = i//10
#     if num == total:
#         lst2.append(num)
# print(lst2)

# # number pattern
# for i in range(1,n+1):
#     for j in range(i):
#         print(j+1, end='')
#     print()

# # Hollow Right Triangle
# for i in range(1,n+1):
#     for j in range(1, i+1):
#         if j == 1 or j == i or i == n:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

# # factorial using 'maths' module
# import math
# print(math.factorial(n))

# # factorial using recursion
# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(n))

# # factorial using loop
# r = 1
# for i in range(1,n+1):
#     r *= i
# print(r)

# # Reverse Hollow Right Triangle
# for i in range(n):
#     for j in range(n):
#         if i == 0 or j == i or j == n-1:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

# # number pattern
# a = 1
# for i in range(1,n+1):
#     for j in range(i):
#         print(a, end=' ')
#         a += 1
#     print()

# # complete a word in lines
# s = input('Enter a word : ')
# for i in range(1,len(s)+1):
#     print(s[0:i])

# # fibonacci Numbers
# a=0
# b=1
# for i in range(n):
#     print(a)
#     a, b = b, a+b

# def fibonacci(n):
#     a = 0
#     b = 1
#     l = []
#     for i in range(n):
#         l.append(a)
#         a,b = b,a+b
#     return l
# print(fibonacci(n))

# # reverse number
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(j, end=' ')
#     print()

# # Prime no
# for i in range(3,100):
#     for j in range(2,i):
#         if i%j == 0:
#             break
#     else:
#         print(i)

# # Check given number is Perfet or not
# total = 0
# for i in range(1, n):
#    if n % i == 0:
#        total += i
# if n == total:
#    print(f'{n} is a Perfect Number.')
# else:
#    print(f'{n} is not a Perfect Number.')


# # Give list of Perfet numbers
# for j in range(2,10000):
#    total = 0
#    for i in range(1, j):
#        if j % i == 0:
#            total += i
#    if j == total:
#        print(j)

# # Print Hollow Dimond Shape
# for i in range(1,2*n):
#    for j in range(1,2*n):
#        if i+j==n+1 or abs(i-j)==n-1 or i+j==3*n-1:
#            print('*', end='')
#        else:
#            print(' ', end='')
#    print()

# # pattern
# l = [[0 for x in range(n)] for y in range(n)]
# a=1
# low=0
# high=n-1
# count=int((n+1)/2)
# for i in range(count):
#    for j in range(low,high+1):
#        l[i][j]=a
#        a=a+1
#    for j in range(low+1,high+1):
#        l[j][high]=a
#        a=a+1
#    for j in range(high-1,low-1,-1):
#        l[high][j]=a
#        a=a+1
#    for j in range(high-1,low,-1):
#        l[j][low]=a
#        a=a+1
#    low=low+1
#    high=high-1

# for i in range(n):
#    for j in range(n):
#        print(l[i][j], end='\t')
#    print()


# # HCF
# n1 = int(input('Number1 : '))
# n2 = int(input('Number2 : '))

# divident=max(n1,n2)
# divisor=min(n1,n2)
# remainder = divident % divisor
# while remainder!=0:
#    divident = divisor
#    divisor = remainder
#    remainder = divident % divident
# print(f'HCF = {divisor}')
# print(f'LCM = {n1*n2//divisor}')

# # print "NO"
# lst_N = [[" " for i in range(6)] for j in range(6)]
# for i in range(6):
#     for j in range(6):
#         if j==0 or j==5 or i==j:
#             lst_N[i][j] = "*"

# lst_O = [[" " for i in range(6)] for j in range(6)]
# for i in range(6):
#     for j in range(6):
#         if (j==0 and i!=0 and i!=5) or (j==5 and i!=0 and i!=5) or (i==0 and j!=0 and j!=5) or (i==5 and j!=0 and j!=5) :
#             lst_O[i][j] = "*"

# for i in range(6):
#     for j in range(6):
#         print(lst_N[i][j], end=' ')
#     for j in range(6):
#         print(lst_O[i][j], end=' ')
#     print()

# # print "YASH"
# lst_Y = [[" " for i in range(6)] for j in range(6)]
# lst_A = [[" " for i in range(5)] for j in range(6)]
# lst_S = [[" " for i in range(6)] for j in range(6)]
# lst_H = [[" " for i in range(6)] for j in range(6)]

# for i in range(6):
#     for j in range(6):
#         if (i<3 and i==j) or i+j==5:
#             lst_Y[i][j] = "*"

# for i in range(6):
#     for j in range(5):
#         if (j==0 and i!=0) or (j==4 and i!=0) or (i==0 and j!=0 and j!=4) or (i==3 and j!=0 and j!=4) :
#             lst_A[i][j] = "*"

# for i in range(6):
#     for j in range(6):
#         if (i==0 and j!=0 ) or (i==5 and j!=5 ) or (i==3 and j!=0 and j!=5) or (j==5 and i==4) or (j==0 and (i==1 or i==2)):
#             lst_S[i][j] = "*"

# for i in range(6):
#     for j in range(6):
#         if j==0 or j==5 or i==3 :
#             lst_H[i][j] = "*"

# for i in range(6):
#     for j in range(6):
#         print(lst_Y[i][j], end=' ')
#     print(end='  ')
#     for j in range(5):
#         print(lst_A[i][j], end=' ')
#     print(end='  ')
#     for j in range(6):
#         print(lst_S[i][j], end=' ')
#     print(end='  ')
#     for j in range(6):
#         print(lst_H[i][j], end=' ')
#     print()


# s = 'aaaabcccdeefff'
# prt = False
# for i in range(len(s)):
#     if s.count(s[i]) == 1:
#         print(s[i])
#         prt = True
# if not prt:
#     print('_')





