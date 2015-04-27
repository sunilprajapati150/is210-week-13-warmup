#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests task 01."""


# Import Python libs
import os
import unittest


# Import user libs
import boroughs


class Task01TestCase(unittest.TestCase):
    """Task 01 tests"""

    def test_get_score_summary(self):
        """Tests boroughs.get_core_summary output."""
        fpath = os.path.join(os.path.dirname(boroughs.__file__),
                             'inspection_results.csv')
        results = boroughs.get_score_summary(fpath)
        results = {k.upper(): v for k, v in results.iteritems()}
        expected = {
            'BRONX': (156, 0.9762820512820514),
            'BROOKLYN': (417, 0.9745803357314141),
            'STATEN ISLAND': (46, 0.9804347826086955),
            'MANHATTAN': (748, 0.9771390374331531),
            'QUEENS': (414,  0.9719806763285017),
        }
        self.assertEqual(results, expected)


if __name__ == '__main__':
    unittest.main()
