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
    """
    def __init__(self, geom, sampling_strategy, no_points, filter_fn = None) -> None:
        self.geom = geom
        self.no_points = no_points
        self.filter_fn = filter_fn

        # assign the correct sampling strategy
        if sampling_strategy in strategy_dict:
            self.sampler = strategy_dict[sampling_strategy]
        else:
            raise ValueError("Invalid sampling strategy")

    def sample_points(self):
        if self.filter_fn == None:
            return self.sampler(self.geom.boundary, n_points = self.no_points)
        else:
            return self.sampler(self.geom.boundary, n_points = self.no_points, filter_fn = self.filter_fn)