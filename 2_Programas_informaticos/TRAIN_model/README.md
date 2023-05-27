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


# [Docs](https://docs.xilinx.com/r/en-US/ug1414-vitis-ai)


**remotes/origin/1.4**

# pasos 

[mi repositorio](https://github.com/ajlorenzo1315/Xilinx_detec)

<pre>

git clone https://github.com/ajlorenzo1315/Xilinx_detec.git
cd Vitis-AI
./docker_run.sh xilinx/vitis-ai-gpu:2.0.0.11030

</pre>

Instalar los requerimientos

<pre>
cd Xilinx_detec/2_Programas_informaticos/2_Programas_informaticos
(vitis-ai-pytorch) Vitis-AI /workspace/Xilinx_detec/2_Programas_informaticos/2_Programas_informaticos > pip install -r requerement.txt 
</pre>

inspirate in [macaque-detection](https://github.com/gau-nernst/macaque-detection)