#!/usr/bin/python3
"""Function to append text to a file"""


def append_write(filename="", text=""):
    """
    Append text to a file and return the number of characters written.
    """
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
