#!/usr/bin/python3
"""function read from file"""


def read_file(filename=""):
    """
    Read and print the contents of a file.

    Args:
        None
    """
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end='')
