"""Core module."""

# -*- coding: utf-8 -*-


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

