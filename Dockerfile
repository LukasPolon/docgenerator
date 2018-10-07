############################
## Dockerfile for production
##
## Usage:
##      - docker service start (if needed)
##      - docker build -t <name>:<tag>
##      - docker run -i -t --entrypoint /bin/bash --volume <current_dir_abs_path>:/docgenerator/ <name>:<tag>
##
############################

FROM python:3.6.3
RUN pip install --upgrade pip
RUN mkdir /docgenerator
WORKDIR /docgenerator
RUN python setup.py develop
