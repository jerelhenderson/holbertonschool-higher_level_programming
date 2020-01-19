#!/usr/bin/python3
def pascal_triangle(n):
    col = 0
    arr = []
    list_arr = []

    if n <= 0:
        return([])

    while col < n:
        new_arr = []
        new_arr.append(1)
        if col > 0:
            for row in range(col - 1):
                new_arr.append(arr[row] + arr[row + 1])
            new_arr.append(1)
        arr = new_arr
        col = col + 1
        list_arr.append(new_arr)
    return list_arr
