import torch

class Config:
    """
    Set up configuration such as the data-types, number generation seeds etc.
    We use this Config object to apply during the training. So, one doesn't need to apply seeds in each jupyter notebook cell.
    """
    def __init__(self, float_type=torch.float32, random_seed=42, device = 'cuda'):
        self.float_type = float_type
        self.random_seed = random_seed
        self.device = device
        # Add more configuration parameters as needed

    def apply_seeds(self):
        torch.manual_seed(self.random_seed)

    def apply_float_type(self):
        torch.set_default_dtype(self.float_type)

    def default_device(self):
        torch.set_default_device(self.device)