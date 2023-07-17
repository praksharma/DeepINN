import torch
from .base import BaseNetwork

class FullyConnected(BaseNetwork, torch.nn.Module):
    """
    Implementation of Fully Connected neural network
    """
    def __init__(self, 
                layer_size,
                activation,
                initializer):
        super().__init__()

    def forward(self):
        # Implementation of forward for the Fully Connected network
        # print(f"Forward pass of {self.__class__.__name__} module.")
        pass


class TestNetwork(BaseNetwork, torch.nn.Module):
    """
    Test network for debugging.
    """
    def __init__(self):
        super().__init__()

    def forward(self):
        print(f"Forward pass of {self.__class__.__name__} module.")
