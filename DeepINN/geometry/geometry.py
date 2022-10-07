import abc # abstract base class
# all functions with @abstractmethod decorator must be defiend in the child class.
# This is useful for more consistent programming.

import numpy as np

class Geometry(abc.ABC):
    """
    Base class for all geometry classes.

    dim (int): the dimension of the geometry (1D, 2D or 3D)
    bbox (array of floats): the bounds of the geometry
    diam (array of floats): length of the geometry    
    """
    def __init__(self, dim, bbox, diam) -> None:
        # -> None to make sure __init__() is not returning anything
        # https://stackoverflow.com/a/64934194/14598633
        self.dim = dim
        self.bbox = bbox
        self.diam = min(diam, np.linalg.norm(bbox[1] - bbox[0]))  # minimum of the diam and L2 norm of the bbox
        self.idstr = type(self).__name__  # check Geometry.__dict__ for the entire list
        # Geometry.idstr = Geometry which is the __name__
    
    @abc.abstractmethod
    def inside(self, x):
        # all Geometry should contain an algorithm to find whether the point is inside or outside
        """Check if x is inside the geometry (including the boundary)."""

    @abc.abstractmethod
    def on_boundary(self, x):
        # all Geometry should be able to find nodes on the boundary
        """Check if x is on the geometry boundary."""
    
    def distance2boundary(self, x, dirn):
        raise NotImplementedError(
            f"{self.idstr}.distance2boundary is not implemented" # fstring is better than .format() thing
        )
    
    def mindist2boundary(self, x):
        raise NotImplementedError(
            f"{self.idstr}.mindist2boundary to be implemented"
        )

    def boundary_normal(self, x):
        """Compute the unit normal at x for Neumann or Robin boundary conditions."""
        raise NotImplementedError(
            f"{self.idstr}.boundary_normal to be implemented"
        )

    def uniform_points(self, n, boundary = True):
        """Generate uniform point cloud in the geometry"""
        print(f"Warning: {self.idstr}.uniform_points is not implemented. Using random_points instead")
        return self.random_points(n) # Fallback to random sampling

    @abc.abstractmethod
    def random_points(self, n, random ='pseudo'):
        # We decide that all geometry will have the random sampling, as it fairly easy to do so.
        """Compute the random point locations in the geometry."""

    def uniform_boundary_points(self, n):
        """Compute the equispaced point locations on the boundary."""
        print(f"Warning: {self.idstr}.uniform_boundary_points not implemented. Using random_boundary_points instead.")
        return self.random_boundary_points(n) # fallback to random sampling

    @abc.abstractmethod
    def random_boundary_points(self, n, random="pseudo"):
        # We decide that all geometry will have the random sampling, as it fairly easy to do so.
        """Compute the random point locations on the boundary."""    

    # TODO : add CSG boolean operations. It is all maths and can be deal later.