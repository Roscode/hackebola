#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2014 Clint Valentine
# Disable Pylint Numpy Errors:
# pylint: disable=E1101
# pylint: disable=E1103
# pylint: disable=C0103
# pylint: disable=W0108

"""
# Store common Python functions here
# Import into IPython kernel with following syntax
from common import csv_to_df

# After making changes to csv_to_df reload into IPython
reload(csv_to_df)

# If run from commandline provide system argument filename after script
"""

from __future__ import print_function
__version__ = '21.11.2014'

import os
import sys
import glob
import datetime
import pandas as pd



def csv_to_df(filename=None, index_col=None):
    """Pass relative filename string and return pandas DataFrame"""
    return pd.read_csv('data\\{0}'.format(filename), sep="\t", header=0,
                       index_col=index_col)

def convert_time(time=None):
    """ Converts Excel days since Dec. 31st 1899 to current time"""
    time = int(time)
    try:
        return datetime.date(1899, 12, 30) + datetime.timedelta(days=time)
    except TypeError:
        return 'NaN'

def summer(x=0):
    """Consecutive summer"""
    x = int(x)
    total = 0
    try:
        return x + total
    except TypeError:
        print("Not an integer")

def relabel(frame=None):
    """Reindexes a DataFrame from 0 to len(DataFrame)"""
    total = len(frame.index)
    ben = list(range(total))
    return frame.reindex(index=ben)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        try:
            FRAME = csv_to_df(sys.argv[1])
        except IOError:
            print('Cannot open: {0}'.format(sys.argv[1]))
    else:
        print('Please provide a filename as a system argument')


"""
Clint's Tricks

Oh you know
Removes NaN and ' '
deaths = deaths[pd.notnull(deaths['value'] != ' ')]

Cumulative summer
deaths['cum_sum'] = deaths['value'].cumsum()

Intifyer
deaths['values'] = deaths['value'].map(lambda x: int(x))



"""
