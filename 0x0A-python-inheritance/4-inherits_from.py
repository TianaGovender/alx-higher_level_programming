#!/usr/bin/python3
"""
Defines a Mylist class
"""


def is_kind_of_class(obj, a_class):
    """Mylist class

    Args:
        obj: object to check
        a_class: Type to check

    Returns:
        response
     
    """
    return type(obj) != a_class and issubclass(type(obj), a_class)
