#!/usr/bin/python3
def matrix_divided(matrix, div):
    new_matrix = []

    for row in matrix:
        for num in row:
            if type(matrix) is not list:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            if type(num) is not int and type(num) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            if len(matrix[0]) != len(matrix[1]):
                raise TypeError("Each row of the matrix must have the same size")

        if type(div) is not int and type(div) is not float:
            raise TypeError("div must be a number")
        if div is 0:
            raise ZeroDivisionError("division by zero")

        for row in range(len(matrix)):
            new_matrix.append(list(map(lambda x: round(x / div, 2), matrix[row])))
        return new_matrix
