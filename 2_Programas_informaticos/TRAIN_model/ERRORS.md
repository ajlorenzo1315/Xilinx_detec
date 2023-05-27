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

docker pull nvidia/cuda:12.1.0-runtime-ubuntu20.04

docker run --gpus all nvidia/cuda:12.1.0-runtime-ubuntu20.04 nvidia-smi
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

<pre>
sudo nvidia-ctk runtime configure --runtime=docker

</pre>
edit /etc/docker/daemon.json

<pre>
sudo nano /etc/docker/daemon.json
{
  "runtimes": {
    "nvidia": {
      "path": "nvidia-container-runtime",
      "runtimeArgs": []
    }
  },
  "default-runtime": "nvidia"
}

</pre>
<pre>
sudo service docker restart
</pre>

desintalar docker

<pre>
sudo apt-get purge docker-ce docker-ce-cli containerd.io
sudo apt autoremove

</pre>

<pre>

docker volume ls -q -f driver=nvidia-docker | xargs -r -I{} -n1 docker ps -q -a -f volume={} | xargs -r docker rm -f
sudo apt-get purge nvidia-docker
curl https://get.docker.com | sh

sudo systemctl start docker && sudo systemctl enable docker

distribution=$(. /etc/os-release;echo $ID$VERSION_ID)

curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -

curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list

nvidia-docker.list 
                                                                      
deb https://nvidia.github.io/libnvidia-container/stable/ubuntu20.04/$(ARCH) /
#deb https://nvidia.github.io/libnvidia-container/experimental/ubuntu18.04/$(ARCH) /
deb https://nvidia.github.io/nvidia-container-runtime/stable/ubuntu20.04/$(ARCH) /
#deb https://nvidia.github.io/nvidia-container-runtime/experimental/ubuntu18.04/$(ARCH) /
deb https://nvidia.github.io/nvidia-docker/ubuntu20.04/$(ARCH) /

sudo apt-get update

sudo apt-get install -y nvidia-docker2

Fichero de configuración `/etc/docker/daemon.json'
 ==> Fichero en el sistema creado por usted o por algún script.
 ==> Fichero también en el paquete.
   ¿Qué quisiera hacer al respecto?  Sus opciones son:
    Y o I  : instalar la versión del desarrollador del paquete 
    N o O  : conservar la versión que tiene instalada actualmente
      D    : mostrar las diferencias entre versiones
      Z    : ejecutar un intérprete de órdenes para examinar la situación
 La acción por omisión es conservar la versión actual.
*** daemon.json (Y/I/N/O/D/Z) [por omisión=N] ? y

sudo systemctl restart docker

prove 

docker run --gpus all nvidia/cuda:12.1.0-runtime-ubuntu20.04 nvidia-smi
</pre>