#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests task 02."""


# Import Python libs
import os
import unittest


# Import user libs
import boroughs


class Task02TestCase(unittest.TestCase):
    """Task 02 tests"""

    def test_get_market_density(self):
        """Tests boroughs.get_market_density() output."""
        fpath = os.path.join(os.path.dirname(boroughs.__file__),
                             'green_markets.json')
        results = boroughs.get_market_density(fpath)
        results = {k.upper(): v for k, v in results.iteritems()}
        expected = {
            u'BRONX': 32,
            u'BROOKLYN': 48,
            u'STATEN ISLAND': 2,
            u'MANHATTAN': 39,
            u'QUEENS': 16,
        }
        self.assertEqual(results, expected)


if __name__ == '__main__':
    unittest.main()
