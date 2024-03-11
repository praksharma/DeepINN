import torch
from .base import BaseNetwork

class FullyConnected(BaseNetwork):
    """
    Implementation of Fully Connected neural network
    """
    def __init__(self, 
                layer_size : list,
                activation : str,
                initialiser : str,
                ):
        super().__init__()

        # Validate the types of the attributes
        if not isinstance(layer_size, list):
            raise TypeError("The 'layer_size' attribute must be an list.")
        if not isinstance(activation, str):
            raise TypeError("The 'activation' attribute must be a string.")
        if not isinstance(initialiser, str):
            raise TypeError("The 'initialiser' attribute must be a string.")
        
        self.activation = self.activation_function(activation)
        self.layer_size = layer_size
        self.initialiser = self.initialiser_function(initialiser)

        # Initialise neural network as a list using nn.Modulelist 
        self.linears = torch.nn.ModuleList([torch.nn.Linear(self.layer_size[i], self.layer_size[i+1]) for i in range(0,len(self.layer_size)-1)])

        # initialise the weights
        self.weight_init()


    def weight_init(self):
        # weight initialisation
        for i in range(len(self.layer_size)-1):
            
            # weights from a normal distribution with 
            # Recommended gain value for tanh = 5/3?
            self.initialiser(self.linears[i].weight.data, gain=1.0)
            
            # set biases to zero
            torch.nn.init.zeros_(self.linears[i].bias.data)

    def forward(self, input):
        """
        Implementation of forward for the Fully Connected network.
        All we need is the inputs tensor and rest of the things are already in the class.
        """

        self.ub = torch.max(input)
        self.lb = torch.min(input)
                      
        # Preprocessing input : feature scaling
        input = (input - self.lb)/(self.ub - self.lb)
        
        self.a = input.float()

        for i in range(len(self.layer_size)-2): # last layer is not activated
            
            self.z = self.linears[i](self.a)
                        
            self.a = self.activation(self.z)
            
        self.a = self.linears[-1](self.a) # linear feedforward no activation in the output layer.
        
        return self.a



class TestNetwork(BaseNetwork, torch.nn.Module):
    """
    Test network for debugging.
    """
    def __init__(self):
        super().__init__()

    def forward(self):
        print(f"Forward pass of {self.__class__.__name__} module.")
