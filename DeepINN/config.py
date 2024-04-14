import torch
import random
import numpy as np

class Config:
    """
    Set up configuration such as the data-types, number generation seeds etc.
    We use this Config object to apply during the training. So, one doesn't need to apply seeds in each jupyter notebook cell.
    """
    def __init__(self, torch_type=torch.float32, torch_seed=0, random_seed=0, numpy_seed=0, device = 'cuda'):
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False

        self.float_type = torch_type
        self.torch_seed = torch_seed
        self.random_seed = random_seed
        self.numpy_seed = numpy_seed
        self.device = device
        # Add more configuration parameters as needed

        # self.apply_seeds()
        # self.apply_float_type()
        # self.default_device()
    def load_all_configs(self):
        self.torch_seeds()
        self.random_seeds()
        self.numpy_seeds()

    def torch_seeds(self):
        torch.manual_seed(self.random_seed)
    
    def random_seeds(self):
        random.seed(self.random_seed)
    
    def numpy_seeds(self):
        np.random.seed(self.numpy_seed)

    def apply_float_type(self):
        torch.set_default_dtype(self.float_type)

    def default_device(self):
        torch.set_default_device(self.device)