#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    zero_tuple = (0, 0)
    tuple_a = tuple_a + zero_tuple
    tuple_b = tuple_b + zero_tuple

    new_tuple_0 = tuple_a[0] + tuple_b[0]
    new_tuple_1 = tuple_a[1] + tuple_b[1]
    return ("({}, {})".format(new_tuple_0, new_tuple_1))
