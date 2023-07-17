import torch

class Model():
    """
    This class combines both the domain and the network. The class will be responsible for bringing the geometry, network and other parameters and then train the neural network.
    domain : an instance of dp.domain
    network : class derived from dp.nn.BaseNetwork  
    """
    def __init__(self, domain, network) -> None:
        self.domain = domain
        self.network = network

    def compile(self):
        """
        Loads the sampled points, loss functions and the network to the model.
        """
        self.compile_domain()

    def compile_domain(self):
        # sample collcaotion points
        self.collocation_point_sample, self.collocation_point_labels = self.domain.sample_collocation_labels()
                
        # sample boundary points
        self.boundary_point_sample, self.boundary_point_labels = self.domain.sample_boundary_labels()

    def compile_network(self):
        