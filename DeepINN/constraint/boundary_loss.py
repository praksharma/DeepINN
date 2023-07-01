from ..geometry import samplers, spaces, domains
from enum import Enum

class dimension(Enum):
    """
    An enum of available dimensions
    """
    R1 = spaces.R1
    R2 = spaces.R2
    R3 = spaces.R3
    Rn = spaces.Rn

class shape(Enum):
    """
    An enum of available shapes
    """
    circle = domains.Circle
    interval = domains.Interval
    parallelegram = domains.Parallelogram
    point = domains.Point
    sphere = domains.Sphere
    triangle = domains.Triangle

class strategy(Enum):
    """
    A list of all sampling strategies
    """
    random = samplers.RandomUniformSampler
    grid = samplers.GridSampler
    LatinHypercube = samplers.LHSSampler

class DirichletBC():
    """
    Dirichlet boundary conditions
    """
    def __init__(self, geom, sampling_strategy, no_points, filter_fn = None) -> None:
        self.geom = geom
        self.no_points = no_points
        if sampling_strategy == "random":
            self.sampler = strategy.random.value
        elif sampling_strategy == "grid":
            self.sampler = strategy.grid.value
        elif sampling_strategy == "LatinHypercube":
            self.sampler = strategy.LatinHypercube.value
        else:
            raise ValueError("Invalid sampling strategy")
    
    def sample_points(self):
        return self.sampler(self.geom.boundary, n_points = self.no_points)