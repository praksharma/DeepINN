import torch

"""
This file contains helper functions common to all neural networks
"""

activation_dict = {
    "linear": torch.nn.Linear,
    "tanh": torch.nn.Tanh,
    "relu": torch.nn.ReLU
}

initialiser_dict = {
    "Glorot uniform" : torch.nn.init.xavier_uniform,
}

def activation(activation_string):
    """
    Returns the activation function module from PyTorch.
    """
    if activation_string in activation_dict:
        return activation_dict[activation_string]
    else:
        raise ValueError("Invalid activation function.")

def initialiser(intialiser_string):
    """
    Returns the initialiser function module from PyTorch.
    """
    if intialiser_string in initialiser_dict:
        return initialiser_dict[intialiser_string]
    else:
        raise ValueError("Invalid initialiser function.")