# COCO

[coco](https://cocodataset.org/#detection-eval)

# Download

<pre>

bash download_dataset.sh

</pre>

*** Metricas ***

"AR" se refiere a "Average Recall" (Recuperación Promedio). El Average Recall (AR) en COCO se calcula para cada categoría de objeto y luego se promedia para obtener un valor general. Se utiliza para medir qué tan bien un modelo es capaz de recuperar los objetos de una determinada categoría en el conjunto de datos.

"AP" se refiere a "Average Precision" (Precisión Promedio).El Average Precision (AP) en COCO se calcula para cada categoría de objeto y luego se promedia para obtener un valor general. Se utiliza para medir qué tan precisas son las detecciones de objetos realizadas por un modelo en términos de la

IoU significa "Intersection over Union" (Intersección sobre Unión, en español). Es una métrica utilizada en tareas de visión por computadora, como detección de objetos y segmentación semántica, para evaluar la precisión de la superposición entre dos regiones o máscaras.

El IoU se calcula como la proporción de área en la que dos regiones o máscaras se superponen, dividida por el área de su unión. Matemáticamente, se puede expresar de la siguiente manera:

IoU = Área de Intersección / Área de Unión

El valor del IoU varía entre 0 y 1, donde 0 indica una falta de superposición y 1 indica una superposición completa. Un valor alto de IoU generalmente indica una mejor coincidencia entre las regiones o máscaras.

El IoU es comúnmente utilizado en la evaluación de algoritmos de detección de objetos y segmentación semántica para medir la precisión de las predicciones en comparación con las anotaciones de referencia o ground truth. Una alta coincidencia de IoU suele ser un criterio importante para considerar una predicción como correcta o precisa.
User


<pre>

Average Precision (AP):

AP          % AP at IoU=.50:.05:.95 (primary challenge metric)
APIoU=.50   % AP at IoU=.50 (PASCAL VOC metric)
APIoU=.75   % AP at IoU=.75 (strict metric)

AP Across Scales:

APsmall     % AP for small objects: area < 322
APmedium    % AP for medium objects: 322 < area < 962
APlarge     % AP for large objects: area > 962

Average Recall (AR):

ARmax=1     % AR given 1 detection per image
ARmax=10    % AR given 10 detections per image
ARmax=100   % AR given 100 detections per image

AR Across Scales:

ARsmall     % AR for small objects: area < 322
ARmedium    % AR for medium objects: 322 < area < 962
ARlarge     % AR for large objects: area > 962

</pre>