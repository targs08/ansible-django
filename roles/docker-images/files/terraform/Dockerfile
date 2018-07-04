FROM debian:jessie
LABEL maintainer targs08

ENV TERRAFORM_VERSION 0.11.6
ENV TERRAFORM_HCLOUD_VERSION 1.1.0

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
            unzip \
    && curl -L https://bootstrap.pypa.io/get-pip.py -o /usr/src/get-pip.py \
    && python /usr/src/get-pip.py

RUN pip install ansible==2.4 requests && \
    ansible-galaxy install carlosbuenosvinos.ansistrano-deploy carlosbuenosvinos.ansistrano-rollback

RUN mkdir -p ~/.terraform.d/plugins/ && \
    curl -o /usr/src/terraform_${TERRAFORM_VERSION}_linux_amd64.zip -L https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
    curl -o /usr/src/terraform-provider-hcloud_v${TERRAFORM_HCLOUD_VERSION}_linux_amd64.zip -L https://github.com/hetznercloud/terraform-provider-hcloud/releases/download/v${TERRAFORM_HCLOUD_VERSION}/terraform-provider-hcloud_v${TERRAFORM_HCLOUD_VERSION}_linux_amd64.zip && \
    unzip /usr/src/terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /usr/bin && \
    unzip /usr/src/terraform-provider-hcloud_v1.1.0_linux_amd64.zip -d ~/.terraform.d/plugins && \
    rm -rf /usr/src/terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
    rm -rf terraform-provider-hcloud_v${TERRAFORM_HCLOUD_VERSION}_linux_amd64.zip

COPY ansible.cfg /etc/ansible/ansible.cfg

WORKDIR /opt/ansible
CMD ['cat']