#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    a = len(matrix)
    if a > 1:
        for i in range(a):
            for j in range(len(matrix[i])):
                if j < (len(matrix[i])) - 1:
                    print("{:d}".format(matrix[i][j]), end=" ")
                else:
                    print("{:d}".format(matrix[i][j]))
    else:
        print("")
