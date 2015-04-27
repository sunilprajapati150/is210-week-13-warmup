#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests task 03."""


# Import Python libs
import json
import os
import unittest


# Import user libs
import boroughs


class Task03TestCase(unittest.TestCase):
    """Task 03 tests"""

    maxDiff = None

    def test_correlate_data(self):
        """Tests boroughs.correlate_data() output."""
        dirpath = os.path.dirname(boroughs.__file__)
        restaurants = os.path.join(dirpath, 'inspection_results.csv')
        markets = os.path.join(dirpath, 'green_markets.json')
        outfile = os.path.join(dirpath, 'newfilename.json')
        boroughs.correlate_data(restaurants, markets, outfile)

        fhandler = open(outfile, 'r')
        results = json.load(fhandler)
        fhandler.close()

        results = {k.upper(): tuple(v) for k, v in results.iteritems()}
        expected = {
            u'BRONX': (0.9762820512820514, 0.20512820512820512),
            u'BROOKLYN': (0.9745803357314141, 0.11510791366906475),
            u'STATEN ISLAND':  (0.9804347826086955, 0.043478260869565216),
            u'MANHATTAN': (0.9771390374331531, 0.05213903743315508),
            u'QUEENS': (0.9719806763285017, 0.03864734299516908),
        }
        self.assertEqual(results, expected)


if __name__ == '__main__':
    unittest.main()
