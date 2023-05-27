# NVIDIA

<pre>

nvidia-smi

No se ha encontrado la orden «nvidia-smi», pero se puede instalar con:

sudo apt install nvidia-340               # version 340.108-0ubuntu5.20.04.2, or
sudo apt install nvidia-utils-390         # version 390.157-0ubuntu0.20.04.1
sudo apt install nvidia-utils-450-server  # version 450.236.01-0ubuntu0.20.04.1
sudo apt install nvidia-utils-470         # version 470.182.03-0ubuntu0.20.04.1
sudo apt install nvidia-utils-470-server  # version 470.182.03-0ubuntu0.20.04.1
sudo apt install nvidia-utils-510         # version 510.108.03-0ubuntu0.20.04.1
sudo apt install nvidia-utils-515         # version 515.105.01-0ubuntu0.20.04.1
sudo apt install nvidia-utils-515-server  # version 515.105.01-0ubuntu0.20.04.1
sudo apt install nvidia-utils-525         # version 525.105.17-0ubuntu0.20.04.1
sudo apt install nvidia-utils-525-server  # version 525.105.17-0ubuntu0.20.04.1
sudo apt install nvidia-utils-530         # version 530.41.03-0ubuntu0.20.04.2
sudo apt install nvidia-utils-435         # version 435.21-0ubuntu7
sudo apt install nvidia-utils-440         # version 440.82+really.440.64-0ubuntu6
sudo apt install nvidia-utils-418-server  # version 418.226.00-0ubuntu0.20.04.2

nvidia-smi
Fri May 26 13:55:05 2023       
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 530.41.03              Driver Version: 530.41.03    CUDA Version: 12.1     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                  Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf            Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  NVIDIA GeForce RTX 3070 L...    Off| 00000000:01:00.0 Off |                  N/A |
| N/A   38C    P0               24W /  N/A|      0MiB /  8192MiB |      8%      Default |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+
                                                                                         
+---------------------------------------------------------------------------------------+
| Processes:                                                                            |
|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|        ID   ID                                                             Usage      |
|=======================================================================================|
|  No running processes found                                                           |
+---------------------------------------------------------------------------------------+

nvcc --version
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2023 NVIDIA Corporation
Built on Mon_Apr__3_17:16:06_PDT_2023
Cuda compilation tools, release 12.1, V12.1.105
Build cuda_12.1.r12.1/compiler.32688072_0

nvidia-ctk --version
NVIDIA Container Toolkit CLI version 1.13.1
commit: 28b70663f1a2b982e59e83bcf1844177dc745208


</pre>

# DOCKER

<pre>

Client: Docker Engine - Community
 Version:           24.0.2
 API version:       1.43
 Go version:        go1.20.4
 Git commit:        cb74dfc
 Built:             Thu May 25 21:52:22 2023
 OS/Arch:           linux/amd64
 Context:           default

Server: Docker Engine - Community
 Engine:
  Version:          24.0.2
  API version:      1.43 (minimum version 1.12)
  Go version:       go1.20.4
  Git commit:       659604f
  Built:            Thu May 25 21:52:22 2023
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          1.6.21
  GitCommit:        3dce8eb055cbb6872793272b4f20ed16117344f8
 runc:
  Version:          1.1.7
  GitCommit:        v1.1.7-0-g860f061
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0

</pre>