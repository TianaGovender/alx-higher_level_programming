#!/usr/bin/python3
"""
Defines a Mylist class
"""


def inherits_from(obj,a_class) -> bool:
    """implementation
    """
    return type(obj) != a_class and issubclass(type(obj), a_class)
