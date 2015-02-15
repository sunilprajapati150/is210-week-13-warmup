#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Smoke test for test suite."""


# Import Python libs
import unittest

class SmokeTestCase(unittest.TestCase):
    """Test cases to ensure that the test suite is operational."""

    def test_true(self):
        """Tests that True is True."""
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
