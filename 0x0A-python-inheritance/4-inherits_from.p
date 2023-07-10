#!/usr/bin/python3
"""My fonction"""


def inherits_from(obj, a_class):
    """Check if obj is a subclass"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
