FROM debian:jessie
LABEL maintainer targs08

ENV DOCKER_BUCKET get.docker.com
ENV DOCKER_VERSION 17.03.0-ce
ENV DOCKER_SHA256 4a9766d99c6818b2d54dc302db3c9f7b352ad0a80a2dc179ec164a3ba29c2d3e

RUN apt-get update && apt-get install --no-install-recommends --assume-yes \
            build-essential \
            python2.7 \
            python2.7-dev \
            python-setuptools \
            libffi-dev \
            libssl-dev \
            ca-certificates \
            curl \
            openssl \
            openssh-server \
            sshpass \
            mc \
            aptitude \
            libmysqlclient-dev \
            git \
    && curl -L https://bootstrap.pypa.io/get-pip.py -o /usr/src/get-pip.py \
    && python /usr/src/get-pip.py

RUN set -x \
	&& curl -fSL "https://${DOCKER_BUCKET}/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz" -o docker.tgz \
	&& echo "${DOCKER_SHA256} *docker.tgz" | sha256sum -c - \
	&& tar -xzvf docker.tgz \
	&& mv docker/* /usr/local/bin/ \
	&& rmdir docker \
	&& rm docker.tgz \
	&& docker -v

RUN pip install ansible docker-compose==1.9.0 passlib mysql-python netaddr
