# app.py

Es una adaptación del codigo proporcionado en el Github de  keras-YOLOv3-model-set y xilinxs

En la carpeta code tiene el script app.py es el codigo que permite ejecutar la inferencia entre dos modelo el test al que hay que pasarle

python aop.py --model_path=../float/yolov4-leaky.pb --anchors_path=yolov4-leaky_anchors.txt --classes_path=configs/coco_classes.txt  --boxthreshold=0.6 --classthreshold=0.35  --annotation_file=../data/val2017.txt


Por otro lado en utils.py esta el sensor que mide el consumo
