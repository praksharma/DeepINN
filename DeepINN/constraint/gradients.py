__all__ = ["jacobian", "hessian"] # callable classes

#from typing import Any
import torch

"""
Majority sections in this module is inspired from DeepXDE's lazy gradient evaluation. 
Lazy evaluation of the gradients is in the todo list.
"""
# This function is in the todo list

# def jacobian(X, y, i = 0, j = 0):
#     """
#     Computes Jacobian matrix J[i],[j] :dy_i/dX_j automatic differentiation.
#     Here, i = 0, 1, 2, ..., y.size()[1] and j = 0, 1, 2, ..., X.size()[1]
#     where, X (inputs) and y (outputs) are tensors and index [1] denotes the number of columns in the respective tensor.

#     In simple words, Jacobian is used to compute the first-order derivatives because according to DeepXDE's dev there are certain advantages over the native PyTorch implementation.

#     * It is lazy evaluation,  i.e., it only computes J[i][j] when needed.
#     * It will remember the gradients that have already been computed to avoid duplicate comptation. This is discussed later.

#     X : Inputs to the neural network.
#         Type : Tensor
#     y : Output of the neural network.
#         Type : Tensor
     
#     TODO: write the description
#     """
#     return X

class Jacobian():
    """
    Computer the jacobian matrix J[i],[j] :dy_i/dX_j automatic differentiation.
    Here, i = 0, 1, 2, ..., y.size()[1] and j = 0, 1, 2, ..., X.size()[1]
    where, X (inputs) and y (outputs) are tensors and index [1] denotes the number of columns in the respective tensor.

    
    X : Inputs to the neural network.
        Type : Tensor
    y : Output of the neural network.
        Type : Tensor
    
    * We use torch.autograd.grad(y, X, grad_outputs=torch.ones_like(y), create_graph=True)[0]
    * here, grad_outputs makes sure that the output is a tensor too. There are some technical reason to use this which I don't know.
    * create_graph=True : This argument specifies whether to create a computation graph for the gradients, which is necessary when you want to compute higher-order derivatives.  
    * [0] is used to access the first gradient in the tuple, which corresponds to the gradient with respect to X.
    * The resulting gradients are multiplied element-wise with a tensor of ones, and the first gradient in the tuple is extracted.
    * As an extra, you must have noticed that you don't need to pass the graph or the network. How will the pytorch implement the chain rule if the graph isn't an argument to grad() function?
    Actually, an attribute called `grad_fn` that holds information about the function that created the tensor and the computational graph associated with it. We can access the graph object using `tensor.grad_fn`.
    """
    def __init__(self, X, y) -> None:
        self.X = X
        self.y = y

        # calculate the number of columns if the tensor isn't 1D. 
        self.dim_X = self.X.size()[1] if len(self.X.size()) > 1 else 1
        self.dim_y = self.y.size()[1] if len(self.y.size()) > 1 else 1

    def __call__(self, i = 0, j = 0):
        """
        Call method is a special method that allows an object to be called as if it were a function.

        i = 0, since we haven't implemented it for multiple output neurons.
        """

        # Some dimension checks.
        if not 0 <= i < self.dim_y:
            raise ValueError(f"i={i} is not valid.")
        if not 0 <= j < self.dim_X:
            raise ValueError(f"j={j} is not valid.")
        
        # for 1D tensors
        if len(self.X.size()) == 1:
            #print("1D")
            all_jacobian = torch.autograd.grad(self.y, self.X, create_graph=True, retain_graph=True)[0]
            return all_jacobian#[:, [j]]
        # This only allows gradients with 1 output neuron.
        all_jacobian = torch.autograd.grad(self.y, self.X, grad_outputs=torch.ones_like(self.y), create_graph=True, retain_graph=True)[0]
        
        return all_jacobian[:, [j]]
