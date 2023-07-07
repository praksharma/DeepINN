import torch

def grad(X, y, i = 0, j = 0):
    """
    Computes dy[:, i]/dX[:, j] using PyTorch's autograd.
    X : Inputs to the neural network.
        Type : Tensor
    y : Output of the neural network.
        Type : Tensor
     
    TODO: write the description
    """
    return X[:, j] 