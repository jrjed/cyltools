'''
Contains functions for modifying the datasets output by Cyltech into a more
managable format
'''

import re
import datetime

def date_format(dates, strip_pattern='%m/%d/%Y'):
    '''
    Creates datetime objects from dates in the dataset
    '''
    return [datetime.datetime.strptime(date.strip(), strip_pattern) for date in dates] 


def fix_neg(s):
    '''
    Corrects placement of minus sign for negative values
    '''
    bad_num = re.search(r'(\d+)-', s)
    if bad_num:
        return '-' + bad_num.group(1)
    else:
        return s


def formatter(column):
    '''
    Converts elements of a column to stripped strings and corrects
    placement of minus sign
    '''
    return [fix_neg(str(x).strip()) for x in column]
