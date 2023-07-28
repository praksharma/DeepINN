# Installation
## Using pip
DeepINN can be installed via pip using the following command:
```sh
pip install DeepINN
```

## Docker image
Pull the image with suitable tagname. The image is available [here](https://hub.docker.com/r/prakhars962/deepinn).

```sh
docker pull prakhars962/deepinn:tagname
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