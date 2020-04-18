#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("{}".format(""))
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] != matrix[i][-1]:
                    print("{}".format(matrix[i][j]), end=" ")
                else:
                    print("{}".format(matrix[i][j]), end="")
                    print("")
