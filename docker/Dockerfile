FROM pytorch/pytorch:latest
LABEL description="DeepINN with PyTorch and GPU support"

COPY requirements.txt /workspace
COPY ../DeepINN /workspace/
WORKDIR /workspace
RUN pip3 install -r requirements.txt 
EXPOSE 8888/tcp
ENV SHELL /bin/bash
ENTRYPOINT ["jupyter", "notebook", "--ip", "0.0.0.0", "--no-browser", "--allow-root"]