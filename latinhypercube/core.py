"""Core module providing functionality of latinhypercube."""

# -*- coding: utf-8 -*-

import numpy as np


def get_hmm():
    """Get a thought."""
    return 'hmmm...'


def hmm():
    """Contemplation..."""
    print(get_hmm())


class Cube:
    """Main class representing the latin hyper cube.

    In particular, this class can count how many data points have been gathered
    in subparts of the cube.
    """

    def __init__(self, n, subdivisions):
        """
        Initialiser of Cube class.

        Expect the number of dimensions dimensions (n), and the number
        of subdivisions (subdivisions).

        n is a positive integer

        subdivisions is an array of length n, giving the number of subvidisions
        of the hypercube in the respective dimensions.
        """
        self.n = n
        self.subdivisions = subdivisions

        assert len(self.subdivisions) == self.n

        assert isinstance(self.n, int)
        assert n > 0

        # create numpy array for occupancy
        self.counts = np.zeros(tuple(self.subdivisions))

    def iadd(self, index, increment=1):
        """IndexADD: Add INCREMENT at hypercube INDEX.

        INDEX is a n-tuple for self.n, increment
        is what should be added to that cell.

        Return the new count value at the given index.
        """
        if not isinstance(index, tuple):
            raise TypeError("index='{}' ({}) must be of"
                            " type tuple".format(index, type(index)))

        self.counts[index] += increment
        return self.counts[index]

    def __eq__(self, other):
        """Compare two Cube objects."""
        if self.n != other.n or self.subdivisions != other.subdivisions:
            return False
        # if we have data, do compare the data
        if np.all(self.counts == other.counts):
            return True
        else:
            return False

    def __repr__(self):
        """Represention of Cube object."""
        msg = "latinhypercube.Cube({}, {})".format(self.n, self.subdivisions)
        return msg
