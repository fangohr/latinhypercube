# -*- coding: utf-8 -*-
"""Template file."""

from .context import latinhypercube

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        """Hmm method."""
        latinhypercube.hmm()


if __name__ == '__main__':
    unittest.main()
