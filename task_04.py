#!/bin/usr/env python
# -*- coding: utf-8 -*-
"""This is a docstring for this assignment"""

def too_many_kittens(kittens,litterboxes,catfood=bool):
    """This is another docstring inside the function.

    Args:
        kittens(int): the number of kittens
        litterboxes(int): the number of available litterboxes
        catfood(bool): represents whether or not any catfood exists
        
    Returns:
        bool: If the number of litterboxs are greater than the number of kittens
        and catfood, return false. Otherwise returns True. exmaples can bee seen below
        
    Examples:
        >>> too_many_kittens(12, 12, False)
        True
        >>> too_many_kittens(13, 12, True)
        True
        >>> too_many_kittens(12, 13, True)
        False
    """

    return not (litterboxes >= kittens and catfood)
