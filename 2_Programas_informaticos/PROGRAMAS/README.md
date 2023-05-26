# Entrenamiento modelo

# PASO 1 Git clone
 
clonamos el repositorio de github de [VITIS-AI](https://github.com/Xilinx/Vitis-AI/tree/master)

<pre>
git clone --recurse-submodules https://github.com/Xilinx/Vitis-AI  
cd Vitis-AI
</pre>

# Compilamos o descargamos los docker de Vitis AI


#### Usando un  Pre-built Docker

Descargue la última versión de Vitis AI Docker con el siguiente comando. Este contenedor se ejecuta en la CPU. o la que necesitemos
<pre>

docker pull xilinx/vitis-ai-cpu:latest  

/Vitis-AI/docker_run.sh xilinx/vitis-ai-cpu:latest
</pre>

To run the docker, use command:
```
./docker_run.sh xilinx/vitis-ai-cpu:latest
```
#### Building Docker from Recipe

There are two types of docker recipes provided - CPU recipe and GPU recipe. If you have a compatible nVidia graphics card with CUDA support, you could use GPU recipe; otherwise you could use CPU recipe.

**CPU Docker**

Use below commands to build the CPU docker:
```
cd setup/docker
./docker_build_cpu.sh
```
To run the CPU docker, use command:
```
./docker_run.sh xilinx/vitis-ai-cpu:latest
```
**GPU Docker**

Use below commands to build the GPU docker:
```
cd setup/docker
./docker_build_gpu.sh
```
To run the GPU docker, use command:
```
./docker_run.sh xilinx/vitis-ai-gpu:latest
```
Please use the file **./docker_run.sh** as a reference for the docker launching scripts, you could make necessary modification to it according to your needs.
