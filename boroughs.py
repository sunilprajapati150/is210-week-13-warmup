#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Creating a function  takes a filename as a string and returning surrerized data"""

import csv
import json


GRADES = {
    'A': float(1.00),
    'B': float(0.90),
    'C': float(0.80),
    'D': float(0.70),
    'F': float(0.60),
}

def get_score_summary(filename):

    """A function that returns the score summary of 5-boro restaurants.

    Args:
        filename (str): the file that contains the data to be analyzed.

    Returns:
        dict: A dictionary keyed by boro, with tuples of the number of
              restaurants in each boro, and the average scores for the boro.

    Examples:
    >>> get_score_summary('inspection_results.csv')
    {'BRONX': (156, 0.9762820512820514), 'BROOKLYN':
    (417, 0.9745803357314141), 'STATEN ISLAND': (46, 0.9804347826086955),
    'MANHATTAN': (748, 0.9771390374331531), 'QUEENS':
    (414, 0.9719806763285017)}
    """

    data = {}
    fhandler = open(filename, 'r')
    csv_f = csv.reader(fhandler)
    for row in csv_f:
        if row[10] not in ['P', '', 'GRADE']:
            data[row[0]] = [row[1], row[10]]
            data.update(data)
            
    fhandler.close()
    buro_data = {}
    for value in data.itervalues():
        if value[0] not in buro_data:
            val1 = 1
            val2 = GRADES[value[1]]
        else:
            val1 = buro_data[value[0]][0] + 1
            val2 = buro_data[value[0]][1] + GRADES[value[1]]
        buro_data[value[0]] = (val1, val2)

    final_data ={}
    for key in buro_data.iterkeys():
        val1= buro_data[key][0]
        val2= buro_data[key][1]/float(buro_data[key][0])
        final_data [key]=(val1, val2)
    return final_data

def get_market_density(filename):

    """A function that returns the green market density in NYC.
    Args:
        filename (string): the file that contains the data to be analyzed.

    Returns:
        dict: A dictionary with each boro as the keys and the number of markets
              as the value.

    Examples:
        >>> get_market_density('green_markets.json')
        {'BRONX': 32, 'BROOKLYN': 48, 'STATEN ISLAND': 2, 'MANHATTAN': 39,
        'QUEENS': 16}
    """
    
  
    fhandler = open(filename, 'r')
    all_data = json.load(fhandler)
    buro_data = all_data["data"]
    final_data = {}
    fhandler.close()
    for data in buro_data:
        data[8] = data[8].strip()
        if data[8] not in final_data.iterkeys():
            val = 1
        else:
            val = final_data[data[8]] + 1
        final_data[data[8]] = val
       
    return final_data

def correlate_data(file1='inspection_results.csv',
                    file2='green_markets.json',
                    file3='result.json'):

    
    data1 = get_score_summary(file1)
    data2 = get_market_density(file2)
    result = {}
    for key2 in data2.iterkeys():
        for key1 in data1.iterkeys():
            if key1 == str(key2).upper():
                val1 = data1[key1][1]
                val2 =(data2[key2])/float(data1[key1][0])
                result[key2] = (val1, val2)
                
    fhandler = open(file3, 'w')
    json.dump(result,fhandler)
    fhandler.close()
