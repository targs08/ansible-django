FROM debian:jessie
LABEL maintainer targs08

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
            aptitude \
            libmysqlclient-dev \
            git \
            rsync \
    && curl -L https://bootstrap.pypa.io/get-pip.py -o /usr/src/get-pip.py \
    && python /usr/src/get-pip.py

RUN pip install ansible==2.3 && \
    ansible-galaxy install carlosbuenosvinos.ansistrano-deploy carlosbuenosvinos.ansistrano-rollback

COPY ansible.cfg /etc/ansible/ansible.cfg

WORKDIR /opt/ansible
CMD ['cat']