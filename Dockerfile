FROM ubuntu:20.04
LABEL maintainer='Kenan BOLAT'

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
COPY ./requirements.txt /tmp/requirements.txt
WORKDIR /app

ARG DEV=false

RUN apt-get update && \
    export CPLUS_INCLUDE_PATH=/usr/include/gdal && \
    export C_INCLUDE_PATH=/usr/include/gdal

RUN apt-get install -y python3 && \
    apt-get install -y software-properties-common && \
    apt-get -y install libgl1 libpq-dev python3.8-dev python3-venv binutils g++  && \
    add-apt-repository ppa:ubuntugis/ppa &&  apt-get update && \
    apt-get install -y gdal-bin libgdal-dev && \
    python3 -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        mallon-user

USER mallon-user
