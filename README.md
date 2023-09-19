# Xilinx_detect In KV260 with Yolov4 [Paper](Xilinx_detec/1_Memoria/1_Memoria_del_TFG_AJLL.pdf)

DEEP LEARNING EN EL BORDE

by

ALICIA JIAJUN LORENZO LOURIDO

Titores

FERNANDO RAFAEL PARDO SECO  (Titor/a)

Xosé Ramón Fernández Vidal  (Cotitor/a) 

## Resumen

Palabras Clave: Visión Artificial, Aprendizaje máquina, FPGA, Quantización, Detección
de objetos

En este trabajo se investigó la viabilidad de las FPGAs (Matrices de puertas progra-
mables en campo) como dispositivos de computación en el borde (Edge Computing)
para la detección de objetos en una cadena industrial, centrándose específicamente
en la detección de cubos. Para ello se utilizó el popular conjunto de datos COCO
2017 para realizar comparativas y, posteriormente, se entrenó un modelo adaptado
a una aplicación industrial de detección de cubos en una cadena de producción.
Los resultados obtenidos indicaron que las FPGAs consumen menos energía en com-
paración con las GPUs, lo que las convierte en una opción eficiente desde el punto
de vista energético. Sin embargo, también se observa una pérdida de precisión en la
tarea de encuadrar los objetos, aunque esta pérdida no afecta de forma crítica a la
detección de cubos en una cadena industrial.


### Capítulo 1. Introducción
#### 1.1. Propuesta y justificación
En la actualidad, el uso de técnicas de inteligencia artificial, especialmente el apren-
dizaje profundo o Deep Learning, ha tenido un impacto transformador en la resolu-
ción de problemas complejos relacionados con la visión por computadora en diver-
sos ámbitos industriales. Estas técnicas han demostrado ser eficaces en aplicaciones
como sistemas de vigilancia, seguridad y control de calidad en líneas de producción.
Sin embargo, la implementación del aprendizaje profundo en el contexto industrial y
de automatización presenta desafíos significativos. Uno de los principales desafíos
es el alto consumo de recursos que requiere el aprendizaje profundo, debido a la
gran cantidad de parámetros y la potencia de cálculo necesaria para su ejecución.
En este campo, donde la eficiencia y la optimización de recursos son fundamentales,
el consumo excesivo de los mismos puede obstaculizar la adopción de técnicas de in-
teligencia artificial. Los sistemas de automatización, como las líneas de producción y
los sistemas de control de calidad, requieren un procesamiento rápido y eficiente de
la información en tiempo real. La implementación del aprendizaje profundo puede
requerir una infraestructura costosa y potente, lo que afecta la viabilidad y rentabi-
lidad de su aplicación. Además, se trabaja con grandes volúmenes de datos, lo que
plantea desafíos adicionales en términos de velocidad de procesamiento y capaci-
dad de respuesta. Esto puede afectar significativamente el funcionamiento correcto
del proceso en ejecución, lo cual puede resultar contraproducente.
Es crucial abordar estos desafíos y encontrar soluciones que permitan aprovechar los
beneficios del aprendizaje profundo en el contexto industrial y de automatización, al
mismo tiempo que se optimiza el consumo de recursos y se garantiza una ejecución
eficiente y rápida de las tareas de procesamiento de datos. Por lo tanto, es necesario
explorar nuevas formas de optimizar los recursos sin comprometer la precisión ni la
velocidad de ejecución.
Hasta hace algunos años, la solución predominante consistía en ejecutar el procesa-
miento en la nube, lo cual no tenía en cuenta el consumo de recursos. Esto generaba
una mayor carga en las redes y una mayor latencia en el procesamiento de infor-
mación, limitando la capacidad de respuesta en tiempo real y afectando la eficiencia
operativa.
En este sentido, resulta interesante investigar la viabilidad de utilizar FPGA (Field-
Programmable Gate Array) para aplicar el aprendizaje profundo en la visión por
computadora en el contexto industrial. Las FPGA permiten implementar algoritmos
de aprendizaje profundo directamente en hardware especializado, lo que puede lle-
var a una ejecución más eficiente y rápida de las tareas de procesamiento de imá-
genes. Además, tienen un tamaño reducido, lo que permite integrarlas en sistemas

embebidos, lo que las hace aún más interesantes en el campo de la automatización
industrial.
Una posible solución es utilizar FPGA como sistema de edge computing (es un en-
foque de computación distribuida donde el procesamiento de datos ocurre cerca del
punto de generación de los mismos). De esta manera, se busca superar estas limi-
taciones, al realizar el procesamiento cerca de la fuente de datos, lo que reduce la
latencia y mejora la capacidad de respuesta.

#### 1.2. Aportación
##### Alcance y Objetivo
El objetivo principal de este estudio es demostrar que el edge computing utilizando
una FPGA es adecuado para desplegar técnicas de aprendizaje profundo (en este
caso, para VA - Visión Artificial) en entornos industriales que requieren tiempo real.
Se realizarán pruebas comparativas entre la FPGA y la GPU, utilizando un modelo
entrenado como YOLOv4. Se medirán métricas clave como precisión de detección,
tiempo de procesamiento y consumo de energía. Estas métricas permitirán comparar
y analizar las ventajas y desventajas de cada plataforma en términos de rendimiento
y eficiencia. El objetivo final es demostrar la viabilidad y eficiencia de las FPGAs en
realizar tareas de detección en el edge computing en comparación con las GPUs.

##### Aplicación
La aplicación de este estudio en detección y aceleración de procesos en entornos
industriales mediante el uso de FPGAs en el edge computing ofrece beneficios sig-
nificativos, como detección en tiempo real, mayor eficiencia energética y mejora en
la capacidad de respuesta. Al procesar los datos directamente en la FPGA, se reduce
la latencia y la dependencia de la conectividad de red, lo que optimiza los procesos
industriales. Esto permite una mayor productividad, calidad y eficiencia operativa
en áreas como control de calidad, gestión de inventario y detección de anomalías.
