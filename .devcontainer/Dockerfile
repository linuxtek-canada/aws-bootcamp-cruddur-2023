FROM ubuntu:jammy-20230301

# Install packages used by Gitpod for compatibility based on: 
# https://hub.docker.com/r/gitpod/workspace-full/dockerfile
# Skipping some of the build tools for languages we aren't using

RUN yes | unminimize \
    && apt update \
    && apt install -yq \
        apt-utils --no-install-recommends apt-utils \
        asciidoctor \
        bash-completion \
        build-essential \
        git \
        git-lfs \
        htop \
        jq \
        less \
        llvm \
        locales \
        man-db \
        nano \
        software-properties-common \
        sudo \
        vim \
        nodejs \
        npm \
        sudo \
        python3 \        
        python3-pip \    
    && locale-gen en_US.UTF-8 \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/*
ENV LANG=en_US.UTF-8

# Set up user bootcamp
ARG USERNAME=bootcamp
ARG USER_UID=1000
ARG USER_GID=$USER_UID
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME
USER $USERNAME

# Install AWS CLI tool
RUN cd /tmp \
    && curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && sudo ./aws/install

# Install PostgreSQL Client into Gitpod
RUN curl -fsSL https://www.postgresql.org/media/keys/ACCC4CF8.asc|sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/postgresql.gpg \
    && echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" | sudo tee -a /etc/apt/sources.list.d/pgdg.list \
    && sudo apt update \
    && sudo apt install -y postgresql-client-13 libpq-dev

# Refresh OS and packages
RUN sudo apt update \    
    && sudo apt autoremove -y \   
    && npm install -g npm@latest \
    && pip install --upgrade pip

