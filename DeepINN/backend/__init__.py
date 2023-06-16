# A fork from DeepXDE.
# The backend is used to use different ML langauges.
# Link: https://github.com/dmlc/dgl/tree/master/python/dgl/backend
# Here we are only implementing PyTorch
# I have copied the PyTorch version of backend: https://github.com/lululxvi/deepxde/tree/master/deepxde/backend
import sys

def load_backend():
    try:
        import torch
        print("Using default backend: PyTorch\n", file=sys.stderr, flush=True)   # print backend name like an error # https://www.askpython.com/python/python-stdin-stdout-stderr
    except ImportError:
        raise ImportError('PyTorch not found.')
        
load_backend()

