# Write a program to create a matrix calculator with add, sub, mul Operations


def printMatrix(matrix):
    for i in matrix:
        print(i)


def createMatrix(order, lst):
    matrix = [[0 for i in range(order)] for i in range(order)]
    for i in range(order):
        for j in range(order):
            matrix[i][j] = int(lst[(i * order) + j])
    return matrix


def operationOnMatrixs(order, m1, m2, operation):
    matrix = [[0 for i in range(order)] for i in range(order)]
    for i in range(order):
        for j in range(order):
            a, b = m1[i][j], m2[i][j]
            if operation == 1:
                matrix[i][j] = a + b
            elif operation == 2:
                matrix[i][j] = a - b
            elif operation == 3:
                for k in range(order):
                    matrix[i][j] += m1[i][k] * m2[k][j]
    return matrix


order = int(input("Enter order of matrix: "))
while True:
    m1 = input("Enter Matrix 1 values sep by ',': ").split(",")
    if len(m1) == order * order: break
    print(f"Please enter {order*order} values.")
while True:
    m2 = input("Enter Matrix 2 values sep by ',': ").split(",")
    if len(m2) == order * order: break
    print(f"Please enter {order*order} values.")

mat1 = createMatrix(order, m1)
mat2 = createMatrix(order, m2)

operation = int(input(
    "Select your operation\n1. Addition\n2. Substraction\n3. Multiplication\n\nYourChoice: "))

printMatrix(operationOnMatrixs(order, mat1, mat2, operation))
