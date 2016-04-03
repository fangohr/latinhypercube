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


def test_reporting_just_initialised():
    """Test occupancy reporting from the cube."""
    cube = latinhypercube.Cube(1, np.array([5]))
    for i in range(5):
        assert cube.counts[i] == 0
    with pytest.raises(IndexError):
        cube.counts[5]

    cube = latinhypercube.Cube(2, np.array([5, 2]))
    for i in range(5):
        assert cube.counts[i, 0] == 0
        assert cube.counts[i, 1] == 0

    with pytest.raises(IndexError):
        cube.counts[5, 2]
    with pytest.raises(IndexError):
        cube.counts[6, 0]


def test_add_value_index():
    """Test adding values by index (IndexADD)."""
    cube = latinhypercube.Cube(1, np.array([5]))

    for i in range(5):
        index = (i,)      # must be tuple
        assert cube.counts[i] == 0
        ret = cube.iadd(index, increment=1)  # return value is current count
        assert ret == 1
        assert cube.counts[i] == 1
        ret = cube.iadd(index, increment=2)
        assert ret == 3
        assert cube.counts[i] == 3
        ret = cube.iadd(index, increment=-3)
        assert ret == 0
        assert cube.counts[i] == 0

    cube = latinhypercube.Cube(2, np.array([5, 2]))

    for j in range(2):
        for i in range(5):
            index = (i, j)
            assert cube.counts[i, j] == 0
            # RETurn value is current count
            ret = cube.iadd(index, increment=1)
            assert ret == 1
            assert cube.counts[i, j] == 1
            ret = cube.iadd(index, increment=2)
            assert ret == 3
            assert cube.counts[i, j] == 3
            ret = cube.iadd(index, increment=-3)
            assert ret == 0
            assert cube.counts[i, j] == 0

    with pytest.raises(TypeError):
        cube.iadd([0, 0])


def test_eq():
    """Testing equality comparison."""
    cube1 = latinhypercube.Cube(1, [42])
    cube2 = latinhypercube.Cube(2, [5, 2])
    cube3 = latinhypercube.Cube(2, [5, 2])
    cube4 = latinhypercube.Cube(3, [6, 2, 5])

    assert cube1 != cube2
    assert cube2 == cube3
    assert cube3 != cube4
    assert cube4 != cube1


def test_repr():
    """Testing representation method."""
    cube = latinhypercube.Cube(2, [5, 2])
    r = repr(cube)
    cube_recreated = eval(r)
    assert cube_recreated == cube

