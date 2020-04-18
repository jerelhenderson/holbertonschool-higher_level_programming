#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("{}".format(""))
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                p = matrix[i][j]
                if matrix[i][j] != matrix[i][-1]:
                    print("{:d}".format(p), end=" ")
                else:
                    print("{:d}".format(p), end="")
                    print("")
