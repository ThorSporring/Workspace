#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 11:33:08 2021

@author: mads

Stolen from : https://pythonise.com/categories/python/python-run-length-encoder
"""

import numpy as np



def runlength(text):

    """
    Returns a run-length encoded string from an input string.
    This method uses a list comprehension to build the return
    string.

    Args:
        text (str): A string to encode

    Returns:
        str: A run length encoded string

    Example:
        input: "aaabbcdddd"
        returns: [('a',3),('b',2),('c',1),('d',4)]
    """

    count = 1
    previous = ""
    mapping = list()

    for character in text:
        if character != previous:
            if previous:
                mapping.append((previous, count))
            count = 1
            previous = character
        else:
            count += 1
    else:
        mapping.append((character, count))

    return mapping





# Assuming x is a vector
x = np.array([4, 4, 5, 5, 5, 6, 8, 8, 8, 8, 8, 8])

# and one wants to obtain the this list of values
# [(value1, runLenght), (value2, runLenght),...]
# i.e. y = [(4, 2), (5, 3), (6, 1), (8, 6)]


y = runlength(x)
