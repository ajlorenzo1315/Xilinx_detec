## Instalaciones 
### PASO 0 DOCKER Y PAQUETES NEE

[install docker : ](https://docs.docker.com/engine/install/ubuntu/)
xilinx commet that it used 19.03 or higher

<pre>
bash install-adicional-software.sh
bash install-docker.sh
</pre>

Error de permisos docker 
<pre>
sudo chmod 666 /var/run/docker.sock
</pre>

<pre>

gcc --version
gcc (Ubuntu 11.3.0-1ubuntu1~22.04) 11.3.0
Copyright (C) 2021 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.


</pre>

## PASO 1

buscamos en la [pagina oficial](https://www.nvidia.com/es-es/geforce/drivers/)

*** Versión del controlador: 530.41 - Fecha de lanzamiento: 2023 Marzo 23  compatible***

install driver nvidia :

xilinxs comment that uses CUDA 11 o higher

[README](http://us.download.nvidia.com/XFree86/Linux-x86_64/530.41.03/README/index.html)

o 

configurar  PASO1-install-cuda-MANUAL y ejecutarlo


<pre>

  Installation of the NVIDIA Accelerated Graphics Driver for Linux-x86_64      
  (version: 530.41.03) is now complete.  Please update your xorg.conf file as  
  appropriate; see the file /usr/share/doc/NVIDIA_GLX-1.0/README.txt for       
  details.

</pre>
#### CUDA
si instalastes los driver de manera automatica con el run instala cuda a aparte 

[nvidia_instal](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=20.04&target_type=deb_network)

<pre>
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-keyring_1.0-1_all.deb
sudo dpkg -i cuda-keyring_1.0-1_all.deb
sudo apt-get update
sudo apt-get -y install cuda
</pre>

<pre>

echo "#Cambiamos os pahts pola instalacion de cuda" >> ~/.bashrc
echo "export PATH=/usr/local/cuda-12.1/bin:$PATH" >> ~/.bashrc
echo "export LD_LIBRARY_PATH=/usr/local/cuda-12.1/lib64:$LD_LIBRARY_PATH" >> ~/.bashrc
echo "export CUDA_HOME=/usr/local/cuda-12.1" >> ~/.bashrc

</pre>

# Docker con nvidia

instalar [NVIDIA Container Toolki](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html)

<pre>
sudo apt-get update \
    && sudo apt-get install -y nvidia-container-toolkit-base
</pre>

# OPCIONAL 

###  CREAR UNA CLABE SSH PARA GITHUB

# Git hub

<pre>

ssh-keygen -t ed25519 -C "ajlorenzon.1315@gmail.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
cat ~/.ssh/id_ed25519.pub

</pre>

