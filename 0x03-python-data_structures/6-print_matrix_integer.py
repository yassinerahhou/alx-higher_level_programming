#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for num in matrix:
        for i in num:
            print("{:d}".format(i), end=" " if i != num[-1]else "")
        print()
