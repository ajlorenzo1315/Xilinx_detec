# Evaluar

Es un modificación de  la libreria keras-YOLOv3-model-set

se modifico para poder ejecutar los modelos quantizados de xilinx 

para ejecutar el test del modelo float

<pre>
python eval.py --model_path=../float/yolov4-leaky.pb --anchors_path=yolov4-leaky_anchors.txt --classes_path=configs/coco_classes.txt --model_input_shape=512x512 --eval_type=COCO --iou_threshold=0.6 --conf_threshold=0.001 --elim_grid_sense --annotation_file=../data/val2017_docker.txt --save_result
</pre>

para ejecutar el test del modelo quantizaso

<pre>
python eval.py --model_path=../quant/yolov4-leaky.pb --anchors_path=yolov4-leaky_anchors.txt --classes_path=configs/coco_classes.txt --model_input_shape=512x512 --eval_type=COCO --iou_threshold=0.6 --conf_threshold=0.001 --elim_grid_sense --annotation_file=../data/val2017_docker.txt --save_result --quantize
</pre>


