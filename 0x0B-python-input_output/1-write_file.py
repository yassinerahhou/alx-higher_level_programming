def write_file(filename="", text=""):
    """
    Read and print the contents of a file.
    """
    with open('filename', encoding="utf-8") as f:
        return f.write(text)
