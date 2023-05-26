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

confogurar  PASO1-install-cuda-MANUAL y ejecutarlo



