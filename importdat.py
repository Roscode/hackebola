#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2014 Clint Valentine
# Disable Pylint Numpy Errors:
# pylint: disable=E1101
# pylint: disable=E1103
# pylint: disable=C0103
# pylint: disable=W0108

"""
Pass sys.argv[1] as filename in relative data\ file
Returns dataframe variable of tab delimited data in Interactive python
"""

from __future__ import division
from __future__ import print_function
import sys
import pandas as pd

def importdat(filename=None):
    """Pass relative data file string and return pandas Dataframe"""
    return pd.read_csv(filename, sep="\t", header=0)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Error: No filename supplied")
    else:
        frame = importdat('data\\{0}'.format(sys.argv[1]))
