#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2014 Clint Valentine
# Disable Pylint Numpy Errors:
# pylint: disable=E1101
# pylint: disable=E1103
# pylint: disable=C0103
# pylint: disable=W0108

"""
# Store common python functions here
# Import into Ipython kernel with following syntax

from common import csv_to_df

# If run from commandline provide system argument filename after script
"""

__version__ = '21.11.2014'
from __future__ import print_function

import sys
import pandas as pd

def csv_to_df(filename=None):
    """Pass relative filename string and return pandas DataFrame"""
    return pd.read_csv('data\\{0}'.format(filename), sep="\t", header=0)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Error: No filename or dataframe name supplied")
    else:
        FRAME = csv_to_df('data\\{0}'.format(sys.argv[1]))
