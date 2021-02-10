FROM ubuntu:18.04
LABEL maintainer=""
LABEL repository=""

RUN apt update && \
    apt install -y bash \
                   build-essential \
                   git \
                   curl \
                   ca-certificates \
                   python3 \
                   python3-pip && \
    rm -rf /var/lib/apt/lists

RUN python3 -m pip install --no-cache-dir --upgrade pip && \
    python3 -m pip install --no-cache-dir \
    jupyter \
    torch

WORKDIR /workspace
COPY . project_template/
RUN cd project_template/ && \
    python3 -m pip install --no-cache-dir .

CMD ["/bin/bash"]