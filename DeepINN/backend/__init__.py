# Based on DeepXDE.
# The backend is used to use different ML langauges.
# Link: https://github.com/dmlc/dgl/tree/master/python/dgl/backend
# Here we are only implementing PyTorch
# I have copied the PyTorch version of backend: https://github.com/lululxvi/deepxde/tree/master/deepxde/backend
import sys
from .utils import loss_metric, choose_optimiser
from ..__about__ import __version__

ascii_art = """┌───────────────────────────────────────────────────────────────────┐
│$$\      $$\                                                       │
│$$$\    $$$ |                                                      │
│$$$$\  $$$$ | $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\  $$$$$$\$$$$\  │
│$$\$$\$$ $$ | \____$$\ $$  __$$\ $$  __$$\  \____$$\ $$  _$$  _$$\ │
│$$ \$$$  $$ | $$$$$$$ |$$ |  \__|$$ /  $$ | $$$$$$$ |$$ / $$ / $$ |│
│$$ |\$  /$$ |$$  __$$ |$$ |      $$ |  $$ |$$  __$$ |$$ | $$ | $$ |│
│$$ | \_/ $$ |\$$$$$$$ |$$ |      \$$$$$$$ |\$$$$$$$ |$$ | $$ | $$ |│
│\__|     \__| \_______|\__|       \____$$ | \_______|\__| \__| \__|│
│                                 $$\   $$ |                        │
│                                 \$$$$$$  |                        │
│                                  \______/                         │
└───────────────────────────────────────────────────────────────────┘"""

def load_backend():
    try:
        import torch
        print(ascii_art, file=sys.stderr, flush=True) # print ascii art
        print("Margam version:" + __version__, file=sys.stderr, flush=True) # print DeepINN version
        print("Using default backend: PyTorch(",torch.device(0).type,")", file=sys.stderr, flush=True)   # print backend name like an error # https://www.askpython.com/python/python-stdin-stdout-stderr
        print("Pytorch version: ",torch.__version__, file=sys.stderr, flush=True) # print pytorch version

    except ImportError:
        raise ImportError('PyTorch not found.')

load_backend()
