import torch
import sys
from .backend import loss_metric, choose_optimiser
from .config import Config
from .utils import timer

class Model():
    """
    This class combines both the domain and the network. The class will be responsible for bringing the geometry, network and other parameters and then train the neural network.
    domain : an instance of dp.domain
    network : class derived from dp.nn.BaseNetwork  
    """
    def __init__(self, domain, network) -> None:
        self.domain = domain
        self.network = network

    def compile(self, optimiser_string : str, lr : float, metrics_string : str, device : str):
        """
        Loads the sampled points, loss functions and the network to the model.
        """
        self.optimiser_function = choose_optimiser(optimiser_string)
        self.lr = lr 
        self.metric = loss_metric(metrics_string)
        self.device = device

        self.compile_domain()
        self.compile_network()

    def compile_domain(self):
        # sample collocation points
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

    def initialise_training(self, iterations : int = None):
        if self.iter == 0: # We are running a fresh training
            self.training_history = []  # Initialize an empty list for storing loss values
            self.iterations = iterations
            # Load all the seeds, data types, devices etc.
            self.config.apply_seeds()
            self.config.apply_float_type()
            self.config.default_device()

            # In 1D problem we need to combine the BCs as there is only one point for each BC, which returns an undefined feature scaling because the ub and lb are same in the denominator, so we get infinity
            # For problem with multiple points on each boundary, we don't need to combine them.
            if self.boundary_point_sample[0].size()[0] == 1: # if row is 1 in the particular boundary tensor
                self.boundary_point_sample = torch.cat(self.boundary_point_sample, dim=0)
                self.boundary_point_labels = torch.cat(self.boundary_point_labels, dim=0)

            # Set requires_grad=True for self.collocation_point_sample
            self.collocation_point_sample.requires_grad = True

    def train(self, iterations : int = None, display_every : int = 1):
        """_summary_

        Args:
            iterations (int): _description_. Number of iterations.
            display_every (int, optional): _description_. Display the loss every display_every iterations. Defaults to 1.           
        """
        self.initialise_training(iterations)
        self.trainer()
        
    @timer
    def trainer(self):
        # implement training loop
        while self.iter <= self.iterations:

            self.BC_forward = self.network.forward(self.boundary_point_sample)
            self.BC_loss = self.metric(self.BC_forward, self.boundary_point_labels)

            self.collocation_forward = self.network.forward(self.collocation_point_sample)
            self.PDE_loss = self.metric(self.domain.pde(self.collocation_point_sample, self.collocation_forward), self.collocation_point_labels)
        
            self.total_loss = self.BC_loss +  self.PDE_loss

            # Clear gradients, otherwise it will start accumulating in each iteration.
            self.optimiser.zero_grad()

            # backprop the total loss
            self.total_loss.backward() 
            
            # Update model parameters based on the older values and the backprop gradient
            self.optimiser.step()
            if self.iter % (self.iterations/10) == 0:
                print(f"Iteration: {self.iter+1} \t BC Loss: {self.BC_loss:0.4f}\t PDE Loss: {self.PDE_loss:0.4f} \t Loss: {self.total_loss:0.4f}")

            # Append the total loss value to the training history list
            self.training_history.append(self.total_loss.item())

            self.iter = self.iter + 1
        else:
            print('Training finished')

