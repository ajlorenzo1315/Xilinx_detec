# Configuración del Portatil

<pre>
lsb_release -a 

No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 20.04.6 LTS
Release:	20.04
Codename:	focal


uname -m && cat /etc/*release
x86_64
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=20.04
DISTRIB_CODENAME=focal
DISTRIB_DESCRIPTION="Ubuntu 20.04.6 LTS"
NAME="Ubuntu"
VERSION="20.04.6 LTS (Focal Fossa)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 20.04.6 LTS"
VERSION_ID="20.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=focal
UBUNTU_CODENAME=focal


lspci | grep VGA
01:00.0 VGA compatible controller: NVIDIA Corporation GA104M [GeForce RTX 3070 Mobile / Max-Q] (rev a1)
06:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Cezanne (rev c4)

lspci | grep VGA
01:00.0 VGA compatible controller: NVIDIA Corporation Device 249d (rev a1)
06:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 1638 (rev c4)

echo "options nvidia NVreg_OpenRmEnableUnsupportedGpus=1" | sudo tee /etc/modprobe.d/nvidia-gsp.conf
options nvidia NVreg_OpenRmEnableUnsupportedGpus=1

</pre>

<pre>
gcc --version
gcc (Ubuntu 11.3.0-1ubuntu1~22.04) 11.3.0
Copyright (C) 2021 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.


</pre>
buscamos en la pagina oficial https://www.nvidia.com/es-es/geforce/drivers/ 

*** Versión del controlador: 530.41 - Fecha de lanzamiento: 2023 Marzo 23  compatible***

install driver nvidia :

xilinxs comment that uses CUDA 11 o higher

<pre>

nvidia-smi
No se ha encontrado la orden «nvidia-smi», pero se puede instalar con:
sudo apt install nvidia-utils-390         # version 390.157-0ubuntu0.22.04.1, or
sudo apt install nvidia-utils-418-server  # version 418.226.00-0ubuntu5~0.22.04.1
sudo apt install nvidia-utils-450-server  # version 450.236.01-0ubuntu0.22.04.1
sudo apt install nvidia-utils-470         # version 470.182.03-0ubuntu0.22.04.1
sudo apt install nvidia-utils-470-server  # version 470.182.03-0ubuntu0.22.04.1
sudo apt install nvidia-utils-510         # version 510.108.03-0ubuntu0.22.04.1
sudo apt install nvidia-utils-515         # version 515.105.01-0ubuntu0.22.04.1
sudo apt install nvidia-utils-515-server  # version 515.105.01-0ubuntu0.22.04.1
sudo apt install nvidia-utils-525         # version 525.105.17-0ubuntu0.22.04.1
sudo apt install nvidia-utils-525-server  # version 525.105.17-0ubuntu0.22.04.1
sudo apt install nvidia-utils-530         # version 530.41.03-0ubuntu0.22.04.2
sudo apt install nvidia-utils-510-server  # version 510.47.03-0ubuntu3

nvidia-smi
Fri May  5 17:01:10 2023       
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 530.41.03              Driver Version: 530.41.03    CUDA Version: 12.1     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                  Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf            Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  NVIDIA GeForce RTX 3070 L...    Off| 00000000:01:00.0 Off |                  N/A |
| N/A   44C    P0               25W /  N/A|      6MiB /  8192MiB |      0%      Default |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+
                                                                                         
+---------------------------------------------------------------------------------------+
| Processes:                                                                            |
|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|        ID   ID                                                             Usage      |
|=======================================================================================|
|    0   N/A  N/A      2044      G   /usr/lib/xorg/Xorg                            4MiB |
+---------------------------------------------------------------------------------------+

</pre>

install docker : https://docs.docker.com/engine/install/ubuntu/

xilinx commet that it used 19.03 or higher

<pre>
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
</pre>



<pre>

docker version

Client: Docker Engine - Community
 Version:           23.0.5
 API version:       1.42
 Go version:        go1.19.8
 Git commit:        bc4487a
 Built:             Wed Apr 26 16:21:07 2023
 OS/Arch:           linux/amd64
 Context:           default

Server: Docker Engine - Community
 Engine:
  Version:          23.0.5
  API version:      1.42 (minimum version 1.12)
  Go version:       go1.19.8
  Git commit:       94d3ad6
  Built:            Wed Apr 26 16:21:07 2023
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          1.6.20
  GitCommit:        2806fc1057397dbaeefbea0e4e17bddfbd388f38
 runc:
  Version:          1.1.5
  GitCommit:        v1.1.5-0-gf19387a
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0


</pre>

permision 

<pre>
permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.24/version": dial unix /var/run/docker.sock: connect: permission denied
 
# solved

sudo chmod 666 /var/run/docker.sock

</pre>

# Docs 

https://docs.xilinx.com/r/en-US/ug1414-vitis-ai

# Xilinx docker version  git@github.com:Xilinx/Vitis-AI.git

**remotes/origin/1.4**

build docker  

in folder Vitis-AI

<pre>
docker pull xilinx/vitis-ai:latest
cd /setup/docker

bash docker_build_gpu.sh
</pre>

# pasos

<pre>
./docker_run.sh xilinx/vitis-ai-gpu:2.5.0.1260
</pre>

Instalar los requerimientos

<pre>
(vitis-ai-pytorch) Vitis-AI /workspace/beca/Yolo_pytorch > pip install -r requerement.txt 
</pre>

inspirate in 
https://github.com/gau-nernst/macaque-detection

# Data

/media/ali/WD_BLACK


# Git hub

<pre>

ssh-keygen -t ed25519 -C "ajlorenzon.1315@gmail.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
cat ~/.ssh/id_ed25519.pub

</pre>

<pre>
ssh-keygen -t ed25519 -C "ajlorenzon.1315@gmail.com"
Generating public/private ed25519 key pair.
Enter file in which to save the key (/home/alourido/.ssh/id_ed25519): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/alourido/.ssh/id_ed25519
Your public key has been saved in /home/alourido/.ssh/id_ed25519.pub
The key fingerprint is:
SHA256:T3W/gAbXhedSbQosF+tM4Nru3Wm7kpHA0aj65ZydLJk ajlorenzon.1315@gmail.com
The key's randomart image is:
+--[ED25519 256]--+
|          .+.....|
|         .+.*o.oo|
|         +.=+o=o |
|        .o==.o.o |
|       .S o+oo. .|
|      .  +o o . .|
|       . +o* + . |
|        ..E.*... |
|          ...o=o |
+----[SHA256]-----+

alourido@alourido:~$ eval "$(ssh-agent -s)"
Agent pid 6566

ssh-add ~/.ssh/id_ed25519
Identity added: /home/alourido/.ssh/id_ed25519 (ajlorenzon.1315@gmail.com)


cat ~/.ssh/id_ed25519.pub
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILIefBTkbf2Kfp5O2s9yDTj3lHP1MEqakUCYErzLg1SI ajlorenzon.1315@gmail.com


</pre>