# A fork from DeepXDE.
# The backend is used to use different ML langauges.
# Link: https://github.com/dmlc/dgl/tree/master/python/dgl/backend
# Here we are only implementing PyTorch
# I have copied the PyTorch version of backend: https://github.com/lululxvi/deepxde/tree/master/deepxde/backend

import importlib
import json
import os
import sys

from . import backend
from .set_default_backend import set_default_backend

_enabled_apis = set()


def _gen_missing_api(api, mod_name):
    def _missing_api(*args, **kwargs):
        raise ImportError(
            'API "%s" is not supported by backend "%s"' % (api, mod_name)
        )

    return _missing_api


def load_backend(mod_name):
    if mod_name not in ["pytorch"]:
        raise NotImplementedError("Please Install PyTorch: %s" % mod_name)
    else:
        print("Using default backend: PyTorch\n", file=sys.stderr, flush=True)   # print backend name like an error # https://www.askpython.com/python/python-stdin-stdout-stderr
    
    mod = importlib.import_module(".%s" % mod_name.replace(".", "_"), __name__) # import a module and assign to a variable. Here we import pytorch (folder) and assign it to this mod
    thismod = sys.modules[__name__] # __name__ = __main__ for this module.
    # log backend name
    # setting attribute to this module: backend name 
    setattr(thismod, "backend_name", mod_name) # an explanation: https://stackoverflow.com/a/72911884/14598633
    for api in backend.__dict__.keys(): # loop over all the attributes of `backend` object
        # to see a list of backend.__dict__.keys()
        # import deepxde as dde
        # print(dde.backend.__dict__.keys())
        # here is a list of all APIs
        """
        dict_keys(['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__path__', '__file__', '__cached__', '__builtins__', 'importlib', 'json', 
        'os', 'sys', 'backend', 'set_default_backend', '_enabled_apis', '_gen_missing_api', 'load_backend', 'get_preferred_backend', 'pytorch', 'backend_name', 
        'lib', 'tf', 'torch', 'jax', 'paddle', 'float16', 'float32', 'float64', 'uint8', 'int8', 'int16', 'int32', 'int64', 'bool', 'data_type_dict', 
        'reverse_data_type_dict', 'is_gpu_available', 'is_tensor', 'shape', 'ndim', 'Variable', 'as_tensor', 'from_numpy', 'to_numpy', 'elu', 'relu', 
        'selu', 'sigmoid', 'silu', 'sin', 'square', 'tanh', 'mean', 'reduce_mean', 'sum', 'reduce_sum', 'norm', 'zeros', 'zeros_like', 'is_enabled'])
        """
        if api.startswith("__"): # some APIs start with "__" they are built in so ignore them
            # ignore python builtin attributes
            continue
        # checking for data types
        if api == "data_type_dict": # list of supported data types in backend/pytorchtensor.py "def data_type_dict()"" 
            # load data type
            if api not in mod.__dict__: # if API is not available in PyTorch folder in the backend/PyTorch directory
                raise ImportError(
                    'API "data_type_dict" is required but missing for backend "%s".'
                    % mod_name
                )
            data_type_dict = mod.__dict__[api]() # copy mod.__dict__[api]() key to data_type_dict of thismod
            for name, dtype in data_type_dict.items(): # unrolling the dictionary
                setattr(thismod, name, dtype) # set the keys and values as the attribute of thismod

            # override data type dict function
            setattr(thismod, "data_type_dict", data_type_dict)
            setattr(
                thismod,
                "reverse_data_type_dict",
                {v: k for k, v in data_type_dict.items()},
            )
        else:
            # load functions
            if api in mod.__dict__:
                _enabled_apis.add(api)
                setattr(thismod, api, mod.__dict__[api])
            else:
                setattr(thismod, api, _gen_missing_api(api, mod_name))


def get_preferred_backend():
    # I am only implementing PyTorch because I don't know Tensorflow. 
    return "pytorch"


load_backend(get_preferred_backend())


def is_enabled(api):
    """Return true if the api is enabled by the current backend.

    Args:
        api (string): The api name.

    Returns:
        bool: ``True`` if the API is enabled by the current backend.
    """
    return api in _enabled_apis