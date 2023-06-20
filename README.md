# DeepINN
[![DeepINN CI](https://github.com/praksharma/DeepINN/actions/workflows/main.yml/badge.svg)](https://github.com/praksharma/DeepINN/actions/workflows/main.yml) [![Documentation Status](https://readthedocs.org/projects/deepinn/badge/?version=latest)](https://deepinn.readthedocs.io/en/latest/index.html?badge=latest) [![License](https://img.shields.io/github/license/praksharma/DeepINN)](https://github.com/praksharma/DeepINN/blob/main/LICENSE) [![Codacy Badge](https://app.codacy.com/project/badge/Grade/a5c43d9b9e6a45759061ac654bdc1e3f)](https://www.codacy.com/gh/praksharma/DeepINN/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=praksharma/DeepINN&amp;utm_campaign=Badge_Grade)![Travis (.org) branch](https://app.travis-ci.com/praksharma/DeepINN.svg?branch=main)


[DeepINN](https://github.com/praksharma/DeepINN) is a deep-learning framework for solving forward  and inverse problem involving PDEs using physics-informed neural networks (PINNs).

* The geometry module has been borrowed from [TorchPhysics](https://github.com/boschresearch/torchphysics).


# Contribution
Create a `venv` in the root of the repo. Here the assumption is that the `python` is symlink to `python3`.
```sh
python -m venv .venv
```
Activate the environment.
```sh
source .venv/bin/activate
```
Confirm that the Python path is updated.
```sh
which python
```
The `STDOUT` should point to the .venv directory. Now, upgrade the pip.
```sh
python -m pip install --upgrade pip
```
Install the required packages.
```sh
pip install -r requirements.txt
```
If you want to build the docs using the same environment, then install the relevant dependencies.
```sh
pip install -r docs/requirements.txt
```

# Testing
The testing is very simple. Just run the test.py file in the current Python virtual environment.
```sh
python test.py
```

