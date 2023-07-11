#!/usr/bin/python3
"""function read from file"""


 def append_write(filename="", text=""):
         
    """
    Read and print the contents of a file.
    """
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
