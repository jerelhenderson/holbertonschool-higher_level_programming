#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    idx = 0
    
    if not matrix:
        return None

    for row in matrix:
        for val in row:
            print("{:d}".format(val), end='')
            if val is not matrix[idx][-1]:
                print(end=" ")
        print (" ")
        idx = idx + 1
