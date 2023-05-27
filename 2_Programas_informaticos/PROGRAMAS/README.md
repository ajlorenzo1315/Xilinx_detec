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


#### Building Docker from Recipe


Se proporcionan dos tipos  de docker:  CPU y  GPU. Si tiene una tarjeta gráfica NVidia compatible con soporte CUDA, puede usar la receta GPU; de lo contrario, podría usar la receta de la CPU.


Para compilar 2.0:

<pre>
cd setup/docker
</pre>

**CPU Docker**

<pre>

./docker_build_cpu.sh
</pre>

**GPU Docker**

<pre>
./docker_build_gpu.sh
</pre>

***Si presenta errores a la hora de compilarlo reduzca el uso de hilos en las intalaciones del dockerfile***
modificar  ***opencv 3.4.3*** y ***protobuf 3.4.0***  el 'make -j' por  'make'  o 'make -j4' (en mi caso)


Ejemplo para correr un imagne compilada

<pre>

/Vitis-AI/docker_run.sh xilinx/vitis-ai-gpu:2.0.0.11030


</pre>
