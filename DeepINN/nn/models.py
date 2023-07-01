import torch.nn as nn
from abc import ABC, abstractmethod

class BaseNetwork(nn.Module):
    """
    Base class for all neural networks
    """
    def __init__(self) -> None:
        super().__init__() # intialise all methods from nn.Module
        #print("DEBUG: Base network")

    @abstractmethod
    def forward(self):
        raise NotImplementedError(f"{self.__class__.__name__} must implement the forward() method.")
    
class FullyConnected(BaseNetwork, nn.Module):
    """
    Implementation of Fully Connected neural network
    """
    def __init__(self):
        super().__init__()

    def forward(self):
        # Implementation of forward for the Fully Connected network
        # print(f"Forward pass of {self.__class__.__name__} module.")
        pass


class TestNetwork(BaseNetwork, nn.Module):
    """
    Test network for debugging.
    """
    def __init__(self):
        super().__init__()

    def forward(self):
        print(f"Forward pass of {self.__class__.__name__} module.")
