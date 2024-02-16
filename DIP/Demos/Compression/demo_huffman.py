#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 11:22:12 2021

@author: Mads Dyrmann
"""

import huffman    # Can be installed using "pip3 install huffman"
import numpy as np

im = np.array([[1, 2, 3, 4],
               [4, 2, 5, 3],
               [4, 1, 1, 1],
               [1, 4, 5, 4]])


# The huffman function expects a list of the following structure:
# [(symbol1, counts), (sumbol2, counts),..]
counts = np.unique(im, return_counts=True)
listofcounts = [(s, c) for s, c in zip(*counts)]


codebook = huffman.codebook(listofcounts)
