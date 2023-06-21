# DeepINN
[![DeepINN CI](https://github.com/praksharma/DeepINN/actions/workflows/main.yml/badge.svg)](https://github.com/praksharma/DeepINN/actions/workflows/main.yml) [![docker_container](https://github.com/praksharma/DeepINN/actions/workflows/docker.yml/badge.svg)](https://github.com/praksharma/DeepINN/actions/workflows/docker.yml) [![Documentation Status](https://readthedocs.org/projects/deepinn/badge/?version=latest)](https://deepinn.readthedocs.io/en/latest/index.html?badge=latest) [![License](https://img.shields.io/github/license/praksharma/DeepINN)](https://github.com/praksharma/DeepINN/blob/main/LICENSE) [![Codacy Badge](https://app.codacy.com/project/badge/Grade/a5c43d9b9e6a45759061ac654bdc1e3f)](https://www.codacy.com/gh/praksharma/DeepINN/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=praksharma/DeepINN&amp;utm_campaign=Badge_Grade)![Travis (.org) branch](https://app.travis-ci.com/praksharma/DeepINN.svg?branch=main)


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

## Docker image
Pull the image with suitable tagname:

```sh
docker push prakhars962/deepinn:tagname
```
### CPU Only
The image opens a jupyter server by default. 
```sh
docker run -p 8888:8888 prakhars962/deepinn:pre-release
```

You can override the jupyter server entrypoint using the following command.
```sh
docker run -it --entrypoint /bin/bash prakhars962/deepinn:pre-release
```
### GPU passthrough
First install `nvidia-docker` using this [guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#step-2-install-nvidia-container-toolkit). 

Now run the container with `nvidia-docker`.
```sh
nvidia-docker run -it --entrypoint /bin/bash prakhars962/deepinn:pre-release
```
This command will bind the `pwd` to `/workspace/tutorials` and open a jupyter-lab with GPU support.
```sh
nvidia-docker run -v $(pwd):/workspace/tutorials -p 8888:8888  prakhars962/deepinn:pre-release
```
Alternatively, one can run interactive session.
```sh
nvidia-docker run -v $(pwd):/workspace/tutorials -it --entrypoint /bin/bash  prakhars962/deepinn:pre-release
```

### Tagless copy
Each time you pull the updated image, docker will create a tagless copy of the old one. 
```sh
╰─ docker images                              
REPOSITORY            TAG           IMAGE ID       CREATED             SIZE
prakhars962/deepinn   pre-release   886808706155   4 minutes ago       6.99GB
prakhars962/deepinn   <none>        0bb744f6159e   38 minutes ago      6.99GB
prakhars962/deepinn   <none>        4ffbb67f8447   About an hour ago   6.8GB
prakhars962/deepinn   <none>        fe16ca34f9d9   About an hour ago   6.8GB
```
The only solution is to delete them one by one using the IMAGE_ID.
```sh
docker image rm -f IMAGE_ID
```

