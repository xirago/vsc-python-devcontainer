FROM ubuntu:24.04

LABEL maintainer="xirago@gmail.com"
LABEL description="VSCode DevContainer for python developement"

# Set locale for Ansible to use based on the already installed locales
ENV LC_ALL="C.utf8"
ENV TZ="UTC"

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get clean && apt-get update && apt-get -yq upgrade
RUN apt-get -yq install python3 python3-pip jq openssl git curl wget unzip
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && ./aws/install \
    && rm awscliv2.zip
RUN python3 -m pip install --break-system-packages ansible-core ansible-lint ansible-creator boto3 botocore

CMD ["/bin/bash"]
