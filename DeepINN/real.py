# Implementing 32bit and 64bit floating points

import numpy as np

# In backend.pytorch.tensor there is a dictionery with list of all supported data types
from . import backend as bkd

class Real:
    """
    precision : int
        number of bits of the data type
    reals : dictionary
        datatype equivalent to the precision (int) in numpy and bkd.    
    """
    def __init__(self, precision): # precision is the input
        # Initialise empty variables
        self.precision = None
        self.reals = None

        if precision == 32:
            self.set_float32()
        elif precision == 64:
            self.set_float64()
        
    def __call__(self, package):
        """
        Queries whether a numpy or backend equivalent datatype is requested.
        package : dictionary key
            np or bkd.lib
        """
        return self.reals[package]
    
    def set_float32(self):
        self.precision = 32
        self.reals = {np : np.float32, bkd.lib : bkd.float32}
        # What is bkd.lib? : print(bkd.lib.__dict__.keys())
    
    def set_float64(self):
        self.precision = 64
        self.reals = {np : np.float64, bkd.lib : bkd.float64}
    