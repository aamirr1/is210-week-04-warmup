#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """This is just another function

    Args:
        wink (str): Str to be repeated numwink times.
        numwink (int, optional): Int by which wink will be repeated. 
        
    Returns:
        str: All arguments will be returned as specified.
        
    Examples:
        >>> know_what_i_mean('wink')
        'Know what I mean? winkwink, nudge nudge'
        >>> know_what_i_mean('wink', 4)
        'Know what I mean? winkwinkwinkwink, nudge nudge nudge nudge'
    """
    
    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr
