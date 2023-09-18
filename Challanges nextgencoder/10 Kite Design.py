# Design a kite using for loops
# a = int(input("Enter no of '#' for the width of kite: ")) - 1
a = 15
for i in range(a, -1, -1):
    if (a - i) % 2 == 0:
        for j in range(i // 2):
            print(" ", end=" ")
        for j in range(a - i + 1):
            print("#", end=" ")
        print()
for i in range(2, a + 1):
    if (a - i) % 2 == 0:
        for j in range(i // 2):
            print(" ", end=" ")
        for j in range(a - i + 1):
            print("#", end=" ")
        print()
for i in range(a // 2, -1, -1):
    s = "  " * i + "#"
    print(s)
