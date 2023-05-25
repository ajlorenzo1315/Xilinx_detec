## Instalaciones 

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