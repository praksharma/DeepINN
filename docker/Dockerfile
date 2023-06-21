FROM pytorch/pytorch:latest
LABEL description="DeepINN with PyTorch and GPU support"

ENV PYTHONPATH="/workspace"

COPY docker/requirements.txt /workspace
COPY DeepINN /workspace/DeepINN
WORKDIR /workspace
RUN pip3 install -r requirements.txt 
EXPOSE 8888/tcp
ENTRYPOINT ["jupyter-lab", "--ip", "0.0.0.0", "--no-browser", "--allow-root"]