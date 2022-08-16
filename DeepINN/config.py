# Set up configuration such as the data-types, number generation seeds etc.

from .real import Real # we can set the default datatype
import random # for random number generating seeds
from .backend import backend_name, torch
import numpy as np


# Default float type
# This can be changed to float64 but requires more memory and is more expensive.
real = Real(32) 

# Random seed
random_seed = None

# XLA JIT is only available for TPU: https://pytorch.org/xla/release/1.12/index.html
xla_jit = False

def default_float():
    """Returns the default data type, as a string."""
    if real.precision == 32:
        return "float32" # no need of else as the condition will be terminated here is true
    return "float64"

def set_default_float(value):
    """Sets the default float type
    Args:
        value (String): 'float32' or 'float64'.
    """
    # TODO : remove default_float() and directly connect real = Real(32) to this function
    if value == "float32":
        print("Set the default float type to float32")
        real.set_float32()
    elif value == "float64":
        print("Set the default float type to float64")
        real.set_float64()

def set_random_seed(seed):
    """Sets all random seeds for the program (Python random, NumPy, and backend), and
    configures the program to run deterministically.

    You can use this to make the program fully deterministic. This means that if the
    program is run multiple times with the same inputs on the same hardware, it will
    have the exact same outputs each time. This is useful for debugging models, and for
    obtaining fully reproducible results.

    Warning:
        Note that determinism in general comes at the expense of lower performance and
        so your model may run slower when determinism is enabled.

    Args:
        seed (int): The desired seed.
    """

    random.seed(seed) # Python seed
    np.random.seed(seed) # numpy seed


    if backend_name == "pytorch": # pytorch random seed
        torch.manual_seed(seed)

    global random_seed # define global variable in the current Python kernel
    random_seed = seed

def enable_xla_jit(mode=True):
    """Enables just-in-time compilation with XLA.
    - Backends PyTorch and PaddlePaddle do not support XLA.
    - Ok I am not sure.

    Args:
        mode (bool): Whether to enable just-in-time compilation with XLA (``True``) or
            disable just-in-time compilation with XLA (``False``).
    """

    if backend_name == "pytorch":
        if mode:
            raise ValueError("Backend PyTorch does not support XLA.")

    global xla_jit
    xla_jit = mode

    if xla_jit:
        print("Enable just-in-time compilation with XLA.\n")
    else:
        print("Disable just-in-time compilation with XLA.\n")

def disable_xla_jit():
    """Disables just-in-time compilation with XLA.

    - For backend TensorFlow 1.x, by default, compiles with XLA when running on GPU.
      XLA compilation can only be enabled when running on GPU.
    - For backend TensorFlow 2.x, by default, compiles with XLA when running on GPU. If
      compilation with XLA makes your code slower on GPU, in addition to calling
      ``disable_xla_jit``, you may simultaneously try XLA with auto-clustering via

          $ TF_XLA_FLAGS=--tf_xla_auto_jit=2 path/to/your/program

    - Backend JAX always uses XLA.
    - Backends PyTorch and PaddlePaddle do not support XLA.

    This is equivalent with ``enable_xla_jit(False)``.
    """
    #enable_xla_jit(False)