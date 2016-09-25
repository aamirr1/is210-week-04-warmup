#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is a docstring for assignment 5"""


def defaults(my_required, my_optional=True):
    """This function compares My_optional with my_required
    
    Args:
        my_optional(mixed): is set to True by default
        my_required(mixed): is not set to any values 
        
    Returns:
        boolean: Returns True if the required and optional parameters are the same.
        Returns False they are not the same.
        
    Examples:
        >>> defaults(True)
        True
        >>> defaults(True, False)
        False
        >>> defaults(False, False)
        True
    """

    return my_optional is my_required
