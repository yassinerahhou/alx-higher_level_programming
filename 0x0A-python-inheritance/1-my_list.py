#!/usr/bin/python3
"""My list printed sorted"""


class MyList(list):
    def print_sorted(self):
        """
        Prints the sorted list in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
