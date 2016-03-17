# -*- coding: utf-8 -*-

"""Tests for core.py."""

import numpy as np
import pytest

from .context import latinhypercube


def test_initialiser():
    """Test."""
    latinhypercube.Cube(1, np.array([10]))
    latinhypercube.Cube(2, np.array([10, 5]))
    latinhypercube.Cube(3, np.array([10, 5, 2]))

    with pytest.raises(AssertionError):
        latinhypercube.Cube(1, np.array([10, 5]))

    with pytest.raises(AssertionError):
        latinhypercube.Cube(0, np.array([]))

    with pytest.raises(AssertionError):
        latinhypercube.Cube(-1, np.array([10]))
