import numpy as np
from .geometry import Geometry
from .. import config

class Interval(Geometry):
    # if we don't define the abstract methods of Geometry class, we will get error
    # this is the purpose of ABC.
    """
    A 1D interval class
    l : coodinate of the left point
    r : coodinate of the right point 
    """
    def __init__(self, l,r) -> None:
        super().__init__(dim = 1, bbox = [np.array([l]), np.array([r])], diam = r-l)
        self.l = l
        self.r = r

    def inside(self, x):
        # all Geometry should contain an algorithm to find whether the point is inside or outside
        return np.logical_and(x >= self.l, x<= self.r).flatten() # .flatten() will create a numpy array of just 1 truth value. i.e. [True] instead of True

    def on_boundary(self, x):
        # np.any() returns only array elements which satisfy an if condition
        return np.any(np.isclose(x, [self.l, self.r]), axis=1) # perform np.any along the columns i.e axis=1

    # TODO: Add extra functions