from ..geometry import samplers, spaces, domains
from enum import Enum

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
        self.no_points = no_points
        self.filter_fn = filter_fn

        # assign the correct sampling strategy
        if sampling_strategy in strategy_dict:
            self.sampler = strategy_dict[sampling_strategy]
        else:
            raise ValueError("Invalid sampling strategy")

    def sampler_object(self):
        # training points sampler
        if self.filter_fn == None:
            return self.sampler(self.geom.boundary, n_points = self.no_points)
        else:
            return self.sampler(self.geom.boundary, n_points = self.no_points, filter_fn = self.filter_fn)
    
    def sample_labels(self, sampled_points):
        # evaluate the BC labels at each training point.
        return self.function(sampled_points)