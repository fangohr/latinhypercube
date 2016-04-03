# -*- coding: utf-8 -*-
"""Template test file."""

from .context import latinhypercube

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_absolute_truth_and_meaning(self):
        """Template test method."""
        assert True

        # use latinhypercube
        latinhypercube


if __name__ == '__main__':
    unittest.main()
