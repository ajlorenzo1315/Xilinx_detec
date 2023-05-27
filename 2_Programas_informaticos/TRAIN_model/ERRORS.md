## DOCKER

<pre>
docker: Error response from daemon: could not select device driver "" with capabilities: [[gpu]].
</pre>

sol

descarger una imagen de nvidia para comprobar si docker encuentra gpus
<pre>
# en mi configuración
docker pull nvidia/cuda:12.1.1-runtime-ubuntu20.04

docker run --gpus all nvidia/cuda:12.1.1-runtime-ubuntu20.04 nvidia-smi

</pre>

<pre>
docker info | grep -i runtime
 Runtimes: io.containerd.runc.v2 runc
 Default Runtime: runc

</pre>

Según la salida del comando docker info | grep -i runtime, parece que Docker no está configurado para utilizar un tiempo de ejecución de GPU específico, como el tiempo de ejecución de contenedores NVIDIA (nvidia-container-runtime).

instal [nvidia-container-toolkit](https://gitlab.com/nvidia/container-toolkit/container-toolkit/-/tree/main/cmd/nvidia-container-runtime)

<pre>
sudo apt-get update \
    && sudo apt-get install -y nvidia-container-toolkit-base
</pre>