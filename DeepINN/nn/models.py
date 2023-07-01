import torch.nn as nn
from abc import ABC, abstractmethod

class BaseNetwork(nn.Module):
    """
    Base class for all neural networks
    """
    def __init__(self) -> None:
        super().__init__() # intialise all methods from nn.Module
        print("DEBUG: Base network")

    @abstractmethod
    def forward(self):
        raise NotImplementedError(f"{self.__class__.__name__} must implement the forward() method.")
