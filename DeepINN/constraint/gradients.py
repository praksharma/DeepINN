__all__ = ["jacobian", "hessian"] # callable classes

import torch

"""
Majority sections in this module is inspired from DeepXDE's lazy gradient evaluation. 
"""

def jacobian(X, y, i = 0, j = 0):
    """
    Computes Jacobian matrix J[i],[j] :dy_i/dX_j automatic differentiation.
    Here, i = 0, 1, 2, ..., y.size()[1] and j = 0, 1, 2, ..., X.size()[1]
    where, X (inputs) and y (outputs) are tensors and index [1] denotes the number of columns in the respective tensor.

    In simple words, Jacobian is used to compute the first-order derivatives because according to DeepXDE's dev there are certain advantages over the native PyTorch implementation.

    * It is lazy evaluation,  i.e., it only computes J[i][j] when needed.
    * It will remember the gradients that have already been computed to avoid duplicate comptation. This is discussed later.

    X : Inputs to the neural network.
        Type : Tensor
    y : Output of the neural network.
        Type : Tensor
     
    TODO: write the description
    """
    return X[:, j] 