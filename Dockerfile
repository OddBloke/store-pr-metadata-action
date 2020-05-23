# Container image that runs your code
FROM ubuntu:20.04

RUN apt-get update && apt-get install -y git python3-github

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY entrypoint.py /entrypoint.py

# Code file to execute when the docker container starts up (`entrypoint.py`)
ENTRYPOINT ["/entrypoint.py"]
