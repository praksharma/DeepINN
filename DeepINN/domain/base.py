import abc

class Dataset(abc.ABC):
    """
    Dataset base class
    """
    def sample_collocation_points(self):
        # returns the collocation points as tensor
        raise NotImplementedError(f"{self.__class__.__name__} must implement the sample_collocation_points() method.")
    
    def sample_collocation_labels(self):
        # returns the collocation points using the above function.
        # also returns the collocation points labels i.e. the residual of the PDE as tensor.
        raise NotImplementedError(f"{self.__class__.__name__} must implement the sample_collocation_labels() method.")
    
    def sample_boundary_points(self):
        # returns a list of boundary points on each boundary as tensor
        raise NotImplementedError(f"{self.__class__.__name__} must implement the sample_boundary_points method.")
    
    def sample_boundary_labels(self):
        # returns the list of boundary points on each boundary using the above function.
        # returns a list of tensor boundary conditions on each boundary.
        raise NotImplementedError(f"{self.__class__.__name__} must implement the sample_boundary_labels() method.")
