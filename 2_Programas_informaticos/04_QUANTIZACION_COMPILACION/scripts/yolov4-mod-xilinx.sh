# Copyright 2020 Xilinx Inc.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#python ../keras-YOLOv3-model-set/tools/model_converter/convert.py \
#    --yolo4_reorder ../my_model/yolov4-mod-xilinx.cfg \
#    ../my_model/yolov4-mod-xilinx_best.weights \
#    ../keras_model
#
#python ../keras-YOLOv3-model-set/tools/model_converter/keras_to_tensorflow.py \
#    --input_model ./keras_model/yolov4-mod-xilinx.h5 \
#    --output_model=./tf_model/yolov4-mod-xilinx.pb

#vai_q_tensorflow quantize --input_frozen_graph ../tf_model/yolov4-mod-xilinx.pb\
#			  --input_fn yolov4_graph_input_keras_fn.calib_input \
#			  --output_dir ../yolov4_quantized \
#	          --input_nodes image_input \
#			  --output_nodes conv2d_93/BiasAdd,conv2d_101/BiasAdd,conv2d_109/BiasAdd \
#			  --input_shapes ?,512,512,3 \
#			  --gpu 1 \
#			  --calib_iter 20 \

TARGET=KV260
NET_NAME=yolov4-mod-xilinx
ARCH=./arch.json
PATH_OUT=./model_data/1_4/

vai_c_tensorflow --frozen_pb ../yolov4_quantized/yolov4-mod-xilinx.pb \
                 --arch ${ARCH} \
		 --output_dir ${PATH_OUT}  \
		 --net_name ${NET_NAME} \
		 --options "{'mode':'normal','save_kernel':'', 'input_shape':'1,512,512,3'}"

#xir subgraph ${PATH_OUT}${NET_NAME}.xmodel  2>&1 | tee ../my_modelo/${NET_NAME}.txt; 
#xir dump_txt ${PATH_OUT}${NET_NAME}.xmodel ../my_modelo/${NET_NAME}.txt;
#xir png ${PATH_OUT}${NET_NAME}.xmodel ../my_modelo/${NET_NAME}.png

#xir subgraph ../yolov4_compiled/dpu_yolov4.xmodel  2>&1 | tee ./model_data/dpu_yolov4.txt;
xir png ./model_data/yolov4-mod-xilinx.xmodel  ./model_data/yolov4-mod-xilinx.png
