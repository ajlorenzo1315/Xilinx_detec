#!/bin/bash

#Set up the repository

## 1  Update the apt package index and install packages to allow apt to use a repository over HTTPS:
#
#sudo apt-get  -y update
#sudo apt-get  install -y ca-certificates curl gnupg
#
## 2  Add Docker’s official GPG key:
#
#sudo install -m 0755 -d /etc/apt/keyrings
#curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
#sudo chmod a+r /etc/apt/keyrings/docker.gpg
#
## 2  Use the following command to set up the repository:
#
#echo \
#  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
#  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
#  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
#
#
#sudo apt-get -y update
#sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# 1. Actualiza el índice de paquetes apt y instala los paquetes necesarios
sudo apt update
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common

# 2. Agrega la clave GPG oficial de Docker
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# 3. Agrega el repositorio de Docker al sistema
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# 4. Actualiza nuevamente el índice de paquetes apt
sudo apt update

# 5. Instala Docker y sus componentes adicionales
sudo apt install -y docker-ce docker-ce-cli containerd.io
