FROM python:3.9-slim

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends git && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /linter

RUN pip install --no-cache-dir pre-commit

COPY containers/ containers/
COPY scripts/ scripts/
COPY src/ src/
COPY .pre-commit-config.yaml .
COPY .git .git

CMD ["pre-commit", "run", "--all-files"]
