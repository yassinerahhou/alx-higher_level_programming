#!/usr/bin/python3
"""My list printed sorted"""


class MyList(list):
    """ mylist is shit
    """
    def print_sorted(self):
        """
        Prints the sorted list in ascending order.
        """
        print(sorted(self))
