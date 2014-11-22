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

[In] 1: from common import csv_to_df

# After making changes to csv_to_df reload into IPython

[In] 2: reload(csv_to_df)

# If run from commandline provide system argument filename after script
"""

from __future__ import print_function
__version__ = '21.11.2014'

import os
import sys
import glob
import datetime
import pandas as pd

from pandas import DataFrame
from pandas import Series

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
        return 'NaT'

def summer(x=0):
    """Consecutive summer"""
    x = int(x)
    total = 0
    try:
        return x + total
    except TypeError:
        print("Not an integer")

def relabel(frame=None):
    """Reindexes a DataFrame from 0 to len(DataFrame)[inserts blanks NaN]"""
    total = len(frame.index)
    ben = list(range(total))
    return frame.reindex(index=ben)

def meter(progress):
    """Provides visual indicator of progress"""
    print("\r{}%".format(int(progress * 100)))


def averagetool(inframe=None):
    """Sifts through categories and averages incidence values per"""

    # Values to branch down to
    country_code = 'adm0_name'
    region_code = 'adm1_name'
    date_code = 'ndate'

    # Value to average and report on regardless of other categories
    food_price = 'mp_price'

    # Initialize final DataFrame for return
    averaged_frame = DataFrame(columns=(country_code, region_code,
                                        date_code, food_price))

    # Keep track of each row appended to averaged_frame
    i = 0

    countries = provideunique(inframe[country_code])
    for country in countries:
        country_frame = inframe[inframe[country_code] == country]
        regions = provideunique(country_frame[region_code])
        for region in regions:
            region_frame = country_frame[country_frame[region_code] == region]
            dates = provideunique(region_frame[date_code])
            for date in dates:
                date_frame = region_frame[region_frame[date_code] == date]
                if not date_frame.empty:

                    # Computes average of value to be averaged
                    average = date_frame[food_price].mean(axis=1)

                    # Assign row to index i in averagedFrame
                    averaged_frame.loc[i] = [country, region, date, average]

                    # Increment row entry
                    i += 1

    return averaged_frame

def provideunique(series=None):
    """Pass Series return list of unique values"""
    uniques = []
    for x in series:
        if x not in uniques:
            uniques.append(x)
    return uniques

def deaths_report_avg(deaths):
    """Not toally sure if this works, by Darren"""
    overalldict = {}
    sourcesum = 0
    for country in deaths['country']:
        countries = deaths[deaths['country'] == country]
        regiondict = {}
        for region in countries['localite']:
            regions = countries[countries['localite'] == region]
            datedict = {}
            for date in regions['ndate']:
                dates = regions[regions['ndate'] == date]
                count = 0
                for source in dates['sources']:
                    sourcery = dates[dates['sources']==source]
                    sourcesum += sourcery['value']
                    count += 1
                avgreport = sourcesum/count
                datedict[date] = avgreport
            regiondict[region] = datedict
        overalldict[country] = regiondict
    return DataFrame.from_dict(overalldict)




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
