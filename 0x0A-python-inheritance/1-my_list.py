#!/usr/bin/python3
"""
Defines a Mylist class
"""


class MyList(list):
    """ Mylist class
    """
    def print_sorted(self):
        """
        prints list in ascending
        """
        print(sorted(self))
        
