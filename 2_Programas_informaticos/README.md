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

# PASO 1 

INSTALACION

# PASO 2

DATA-SET

# PASO 3

TRAIN

# PASO 4

QUANTIZACIÓN

# PASO 5 

DESPLIEGUE

# PASO 6

EVALUACIÓN


# [Docs](https://docs.xilinx.com/r/en-US/ug1414-vitis-ai)



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
cd Vitis-AI
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