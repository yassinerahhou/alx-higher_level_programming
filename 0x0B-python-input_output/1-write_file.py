#!/usr/bin/python3
"""write text"""


def write_file(filename="", text=""):
    """write function"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
