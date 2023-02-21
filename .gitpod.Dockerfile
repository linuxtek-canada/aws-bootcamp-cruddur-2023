FROM gitpod/workspace-full:latest

# Install AWS CLI tool
RUN cd /workspace \
    && curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && sudo /workspace/aws/install

# Refresh OS and packages
RUN sudo apt update \
    && sudo apt install -y apt-utils --no-install-recommends apt-utils \
    && sudo apt autoremove -y \   
    && npm install -g npm@latest

# Install PostgreSQL Client into Gitpod
RUN curl -fsSL https://www.postgresql.org/media/keys/ACCC4CF8.asc|sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/postgresql.gpg \
      echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" | sudo tee -a /etc/apt/sources.list.d/pgdg.list \
      sudo apt update \
      sudo apt install -y postgresql-client-13 libpq-dev