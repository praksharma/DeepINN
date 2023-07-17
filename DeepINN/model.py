import torch
import sys
from .backend import loss_metric, choose_optimiser
from  .config import Config

class Model():
    """
    This class combines both the domain and the network. The class will be responsible for bringing the geometry, network and other parameters and then train the neural network.
    domain : an instance of dp.domain
    network : class derived from dp.nn.BaseNetwork  
    """
    def __init__(self, domain, network) -> None:
        self.domain = domain
        self.network = network

    def compile(self, optimiser : str, lr : float, metrics : str, device : str):
        """
        Loads the sampled points, loss functions and the network to the model.
        """
        self.optimiser_function = choose_optimiser(optimiser)
        self.lr = lr 
        self.metrics = loss_metric(metrics)
        self.device = device

        self.compile_domain()
        self.compile_network()

    def compile_domain(self):
        # sample collcation points
        self.collocation_point_sample, self.collocation_point_labels = self.domain.sample_collocation_labels()
                
        # sample boundary points
        self.boundary_point_sample, self.boundary_point_labels = self.domain.sample_boundary_labels()
        print("Domain compiled", file=sys.stderr, flush=True)

    def compile_network(self):
        # initialise the iteration number
        self.iter = 0
        # network parameters
        self.network_parameters = list(self.network.parameters())
        # seeds, default data types and default device
        self.config = Config(device = self.device)
        # Initialise optimiser
        self.optimiser = self.optimiser_function(self.network_parameters,
                                                 lr = self.lr,
                                                 )
        print("Network compiled", file=sys.stderr, flush=True)

    def train(self, iterations : int = None):
        # Load all the seeds, data types, devices etc.
        self.config.apply_seeds()
        self.config.apply_float_type()
        self.config.default_device()

        # implement training loop