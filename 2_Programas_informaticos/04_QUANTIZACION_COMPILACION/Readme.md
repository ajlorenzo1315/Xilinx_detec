# Quantización y Compilación del modelo

# PASO 1 Git clone

[Keras-Yolov3](https://github.com/david8862/keras-YOLOv3-model-set.git)

<pre>
git clone https://github.com/david8862/keras-YOLOv3-model-set.git
</pre>

# PASO 2 CONVERTIR MODELO

de pesos y cfg a un archivo .pb pasando por h5

<pre>
cd scripts
bash convert_yolov4_me.sh
</pre>

# PASO 3 QUANTIZAMOS EL MODELO

En este caso se parte de un conjunto de imagenes tomadas de los cubos pero se redimensionaron debido a que el ordenaor se sobrecargaba por las originales son muy grandes. En este caso tienes que tener un .txt que contenga los nombres de las imagenes

<pre>
data/img1
data/img2
data/img3
</pre>

<pre>
cd scripts
bash quantize_yolov4_me.sh
</pre>

# PASO 4 COMPILAMOS

<pre>
cd scripts
bash yolov4-mod-xilinx.sh
</pre>
