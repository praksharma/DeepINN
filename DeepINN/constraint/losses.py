from ..geometry import samplers, spaces, domains
from enum import Enum
import torch


# A list of all sampling strategies
strategy_dict = {
    "random": samplers.RandomUniformSampler,
    "grid": samplers.GridSampler,
    "LatinHypercube": samplers.LHSSampler
}

class DirichletBC():
    """
    Dirichlet boundary conditions
    geom : the geometry
        must be a domain available in dp.domains
    function : the prescribed Dirichlet BC value
        must be a function
    sampling_strategy: sampling method
        see strategy_dict for available options
    n_points: number of points to sample
        must be a natural number
    filter_fn: sample points based on a function
        must be a function
    """
    def __init__(self, geom, function, sampling_strategy, no_points, filter_fn = None) -> None:
        self.geom = geom
        self.function = function
        self.sampling_strategy = sampling_strategy
        self.no_points = no_points
        self.filter_fn = filter_fn

        # assign the correct sampling strategy
        if self.sampling_strategy in strategy_dict:
            self.sampler = strategy_dict[self.sampling_strategy]
        else:
            raise ValueError("Invalid sampling strategy")

    def sampler_object(self):
        # training points sampler : use sample_points() method to sample points of tensor type.
        if self.filter_fn == None:
            return self.sampler(self.geom.boundary, n_points = self.no_points)
        else:
            return self.sampler(self.geom.boundary, n_points = self.no_points, filter_fn = self.filter_fn)
    
    def sample_labels(self, sampled_points):
        # evaluate the BC labels at each training point.
        return self.function(sampled_points)

class PDE():
    """
    PDE loss condition.
    We move everything in the PDE to the left side, resulting a RHS with zeros.
    """

    def __init__(self, geom, sampling_strategy, no_points, filter_fn = None) -> None:
        self.geom = geom
        self.sampling_strategy = sampling_strategy
        self.no_points = no_points
        
        # TODO : See if we need filter function for PDE.
        if filter_fn is not None:
            raise NotImplementedError("Filter function isn't implemented for collocation points. Use filter_fn=None.")
        
                # assign the correct sampling strategy
        if self.sampling_strategy in strategy_dict:
            self.sampler = strategy_dict[self.sampling_strategy]
        else:
            raise ValueError("Invalid sampling strategy")
        
    def sampler_object(self):
        # training points sampler : use sample_points() method to sample points of tensor type.
        return self.sampler(self.geom, n_points = self.no_points)
    def sample_labels(self, sampled_points):
        # evaluate the BC labels at each training point.
        # return a tensor of zeros for the RHS equal to the number of rows in sampled_points, i.e., the number of collocation points.
        return torch.zeros(sampled_points.size()[0])