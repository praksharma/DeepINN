# Set up configuration such as the data-types, number generation seeds etc.

from .real import Real # we can set the default datatype
import random # for random number generating seeds
from .backend import backend_name, torch
import numpy as np


# Default float type
# This can be changed to float64 but requires more memory and is more expensive.
real = Real(32)
