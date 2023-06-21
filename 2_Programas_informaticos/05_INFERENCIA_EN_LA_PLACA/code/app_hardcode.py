'''
Copyright 2021 Avnet Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

# USAGE
# python avnet_face_detection.py [--input 0] [--detthreshold 0.55] [--nmsthreshold 0.35]

from ctypes import *
from typing import List
import cv2
import numpy as np
import vart
import pathlib
import xir
import os
import math
import threading
import time
import sys
import argparse

from imutils.video import FPS
from utils import Sensor,annotation_parse,transform_gt_record
from eval_me import compute_AP_COCO,get_scale_gt_dict,compute_AP_COCO_Scale

sys.path.append(os.path.abspath('../'))
sys.path.append(os.path.abspath('./'))
from vitis_ai_vart.facedetect import FaceDetect
from vitis_ai_vart.utils import get_child_subgraph_dpu

from common.utils_me import get_dataset, get_classes, get_anchors, get_colors, draw_boxes, get_custom_objects,draw_box
from PIL import Image

from collections import OrderedDict
from tqdm import tqdm


def non_max_suppression_grouped(boxes, scores, classes, threshold, suppress_class=False):
    
    COCO_INSTANCE_CATEGORY_NAMES = [
    'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus',
    'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'stop sign',
    'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
    'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella',
    'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
    'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket',
    'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl',
    'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
    'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'dining table',
    'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
    'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book',
    'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush']

    # Ordenar las cajas, las puntuaciones y las clases de mayor a menor confianza
    sorted_indices = np.argsort(scores)[::-1]
    boxes = boxes[sorted_indices]
    scores = scores[sorted_indices]
    classes = classes[sorted_indices]

    selected_boxes = []
    selected_scores = []
    selected_classes = []
    
    while len(boxes) > 0:
        best_box = boxes[0]
        best_score = scores[0]
        best_class = classes[0]

        #selected_boxes.append(best_box)
        #selected_scores.append(best_score)
        #selected_classes.append(best_class)

        ious = calculate_iou(boxes, best_box)

        mask = ious <= threshold
       
        if suppress_class:
            class_mask = classes != best_class
            mask = class_mask #np.logical_and(mask, class_mask)
     
        overlapping_boxes = boxes[np.logical_not(mask)]

        boxes = boxes[mask]
        scores = scores[mask]
        classes = classes[mask]

        if len(overlapping_boxes) > 0:
            min_x = np.min(overlapping_boxes[:, 0])
            min_y = np.min(overlapping_boxes[:, 1])
            max_x = np.max(overlapping_boxes[:, 2])
            max_y = np.max(overlapping_boxes[:, 3])
           
            ## adjust box size
            adjustment = -0.15
            #top    += int(adjustment*box_height)
            #bottom -= int(adjustment*box_height)
            #left   += int(adjustment*box_width)
            #right  -= int(adjustment*box_wisdth)     
            
            new_box = np.array([min_x, min_y, max_x, max_y])#+(np.array([+0.15,-0.15,+0.15,-0.15])*np.array([min_x, min_y, max_x, max_y]))
            
            selected_boxes.append(new_box)
            selected_scores.append(best_score)
            selected_classes.append(best_class)
        
        else:
            selected_boxes.append(best_box)
            selected_scores.append(best_score)
            selected_classes.append(best_class)

       
    for i,box in enumerate(boxes):
        selected_boxes.append(box)
        selected_scores.append(scores[i])
        selected_classes.append(classes[i])
   
    return np.array(selected_boxes), np.array(selected_scores), np.array(selected_classes)


def calculate_iou(boxes, target_box):
    x1 = np.maximum(boxes[:, 0], target_box[0])
    y1 = np.maximum(boxes[:, 1], target_box[1])
    x2 = np.minimum(boxes[:, 2], target_box[2])
    y2 = np.minimum(boxes[:, 3], target_box[3])

    intersection_area = np.maximum(x2 - x1, 0) * np.maximum(y2 - y1, 0)
    target_area = (target_box[2] - target_box[0]) * (target_box[3] - target_box[1])
    box_areas = (boxes[:, 2] - boxes[:, 0]) * (boxes[:, 3] - boxes[:, 1])
    union_area = target_area + box_areas - intersection_area

    ious = intersection_area / union_area

    return ious



def calculate_intersection_area(box, other_boxes):
    x1 = np.maximum(box[0], other_boxes[:, 0])
    y1 = np.maximum(box[1], other_boxes[:, 1])
    x2 = np.minimum(box[2], other_boxes[:, 2])
    y2 = np.minimum(box[3], other_boxes[:, 3])
    
    intersection_width = np.maximum(0, x2 - x1)
    intersection_height = np.maximum(0, y2 - y1)
    
    return intersection_width * intersection_height

#medidor=Sensor(1, True)
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=False,
    help = "input camera identifier (default = 0)")
ap.add_argument("-d", "--detthreshold", required=False,
    help = "face detector softmax threshold (default = 0.55)")
ap.add_argument("-n", "--nmsthreshold", required=False,
    help = "face detector NMS threshold (default = 0.35)")
args = vars(ap.parse_args())

if not args.get("input",False):
    inputId = 0
else:
    inputId = int(args["input"])
print('[INFO] input camera identifier = ',inputId)

if not args.get("detthreshold",False):
    detThreshold = 0.10#0.55
else:
    detThreshold = float(args["detthreshold"])
print('[INFO] face detector - softmax threshold = ',detThreshold)

if not args.get("nmsthreshold",False):
    nmsThreshold = 0.10#0.35
else:
    nmsThreshold = float(args["nmsthreshold"])
print('[INFO] face detector - NMS threshold = ',nmsThreshold)

# Initialize Vitis-AI/DPU based face detector
#densebox_xmodel = "/usr/share/vitis_ai_library/models/densebox_640_360/densebox_640_360.xmodel"
moodelos_name=["../2_5/yolov4-mod-xilinx_kv260.xmodel","../../coco/yolov4-coco-xilinx_kv260.xmodel",
"../yolov4_leaky_512_tf/yolov4_leaky_512_tf.xmodel","../coco_xilinx/yolov4-coco-xilinx_kv260_xilinx.xmodel",
"../yolov4_leaky_spp_m/yolov4_leaky_spp_m.xmodel","../../app/2_5/yolov4-mod-xilinx_kv260.xmodel"]

densebox_xmodel =moodelos_name[-1] #"../../coco/yolov4-coco-xilinx_kv260.xmodel"  #"../../2_5/yolov4-mod-xilinx_kv260.xmodel"
densebox_graph = xir.Graph.deserialize(densebox_xmodel)
densebox_subgraphs = get_child_subgraph_dpu(densebox_graph)
assert len(densebox_subgraphs) == 1 # only one DPU kernel
densebox_dpu = vart.Runner.create_runner(densebox_subgraphs[0],"run")

COCO_INSTANCE_CATEGORY_NAMES = [
    'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus',
    'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'stop sign',
    'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
    'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella',
    'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
    'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket',
    'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl',
    'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
    'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'dining table',
    'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
    'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book',
    'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush']

Project_names=["bm","br","bn","bmt","brt","bnt",]

class_names =Project_names# COCO_INSTANCE_CATEGORY_NAMES#["bm","br","bn","bmt","brt","bnt",]
anchor_list = [12,16,19,36,40,28,36,75,76,55,72,146,142,110,192,243,459,401]
anchor_float = [float(x) for x in anchor_list]
anchors = np.array(anchor_float).reshape(-1, 2)
dpu_face_detector = FaceDetect(densebox_dpu,class_names,anchors,detThreshold,nmsThreshold)
dpu_face_detector.start()

# Initialize the camera input
#print("[INFO] starting camera input ...")
#cam = cv2.VideoCapture(inputId)
#cam.set(cv2.CAP_PROP_FRAME_WIDTH,640)
#cam.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
#if not (cam.isOpened()):
#        print("[ERROR] Failed to open camera ", inputId )
#        exit()

# start the FPS counter
fps = FPS().start()
#foto_name='../../data/IMG20230309115431.jpg'#'../../data/dog.jpg'  #'../../coco/dog.jpg' #'../../data/IMG20230309115431.jpg'
#frame=cv2.imread(foto_name)
new_width = 512
new_height = 512
datas=['../data_me/data.txt','../data/val2017.txt','../data_me/data_short.txt']
pred_classes_records = OrderedDict()
annotation_file=datas[0] # '../data/val2017.txt' #'../data_me/data_short.txt' #val2017_short#val2017
annotation_lines = get_dataset(annotation_file, shuffle=False)
annotation_records, gt_classes_records = annotation_parse(annotation_lines, class_names)
save_result=True
start = time.time()
os.makedirs('result', exist_ok=True)
result_file = open(os.path.join('result','detection_result.txt'), 'w')
pbar = tqdm(total=len(annotation_records), desc='Eval model')
#pbar = tqdm(total=1, desc='Eval model')
#print(annotation_records)
#image_name,gt_records= list(annotation_records.items())[0]# #../data/val2017/000000000139.jpg' #'../../data/IMG20230309115431.jpg'
#gt_records=gt_classes_records[0]

#print(list(annotation_records.items())[0])
colors = get_colors(len(class_names))
if save_result:
    result_dir=os.path.join('result','detection')
    os.makedirs(result_dir, exist_ok=True)
for image_name,gt_records in list(annotation_records.items()):
    # loop over the frames from the video stream
    #while True:
    # Capture image from camera
    #ret,frame = cam.read()
  
    #if image_name not in {'/home/root/Vitis-AI/examples/vai_runtime/tfg/xilinx_version/data/val2017/000000000139.jpg',
    #    '/home/root/Vitis-AI/examples/vai_runtime/tfg/xilinx_version/data/val2017/000000000285.jpg',
    #    '/home/root/Vitis-AI/examples/vai_runtime/tfg/xilinx_version/data/val2017/000000000632.jpg',
    #    '/home/root/Vitis-AI/examples/vai_runtime/tfg/xilinx_version/data/val2017/000000000724.jpg',
    #    '/home/root/Vitis-AI/examples/vai_runtime/tfg/xilinx_version/data/val2017/000000000776.jpg',
    #    '/home/root/Vitis-AI/examples/vai_runtime/tfg/xilinx_version/data/val2017/000000000785.jpg',
    #    '/home/root/Vitis-AI/examples/vai_runtime/tfg/xilinx_version/data/val2017/000000000872.jpg',}:
    #    continue
    # Camera provided BGR, and DPU needs RGB
    frame=cv2.imread(image_name)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image_array=frame_rgb.copy()
    image_array=cv2.cvtColor(image_array, cv2.COLOR_RGB2BGR)
    #frame_rgb= cv2.resize(frame_rgb, (new_width, new_height))
    #frame_rgb = cv2.resize(frame_rgb, (64, 64))
    imgHeight = frame_rgb.shape[0]
    imgWidth  = frame_rgb.shape[1]
    #print(frame_rgb.shape)
    # Vitis-AI/DPU based face detector

    boxes, scores, classes = dpu_face_detector.process(frame_rgb)
    boxes, scores, classes =  non_max_suppression_grouped(boxes, scores, classes,0.1)
    boxes, scores, classes =  non_max_suppression_grouped(boxes, scores, classes,0.4)
    #boxes, scores, classes =  non_max_suppression_grouped(boxes, scores, classes,0.4)
    # loop over the faces

    pred_boxes, pred_classes, pred_scores=boxes,classes,scores
    #print(pred_boxes)
    # Nothing detected
    pbar.update(1)

    if pred_boxes is None or len(pred_boxes) == 0:
        continue
   
    result_file.write(image_name)
    
    for box, cls, score in zip(pred_boxes, pred_classes, pred_scores):
        ymin,xmin,ymax, xmax = box
        box_height = ymax-ymin
        box_width = xmax-xmin
        #adjustment = -0.15
        #ymax    += int(adjustment*box_height)
        #ymin   -= int(adjustment*box_height)
        #xmin   += int(adjustment*box_width)
        #xmax  -= int(adjustment*box_width)     
        

        box_annotation = " %f,%f,%f,%f,%d,%f" % (
            xmin, ymin, xmax, ymax, cls, score)
        result_file.write(box_annotation)

        pred_class_name = class_names[cls]
        coordinate = "{},{},{},{}".format(xmin, ymin, xmax, ymax)

        record = [os.path.basename(image_name), coordinate, score]
        if pred_class_name in pred_classes_records:
            pred_classes_records[pred_class_name].append(record)
        else:
            pred_classes_records[pred_class_name] = list([record])
        if save_result:
            draw_box(box, cls, score,class_names, colors,image_array)

    result_file.write('\n')
    result_file.flush()
    if save_result:
        #gt_boxes, gt_classes, gt_scores = transform_gt_record(gt_records, class_names)
        

        #for _box, _score, _class_num in zip(boxes, scores, classes):
        #    _name = class_names[_class_num]
        #    _score = int(_score*100)
        #    top,left,bottom,right = _box.astype(int)
        #    box_height = bottom-top
        #    box_width = right-left
        #    
        #    
        #    # draw a bounding box surrounding the object so we can
        #    color = (64, 64, 255)
        #    cv2.rectangle( frame, (left,top), (right,bottom), color, 4)
        #    cv2.putText(frame, f"{_score}% {_name}",
        #                (left+8,bottom-8), cv2.FONT_HERSHEY_SIMPLEX, 
        #                0.8, color, 2, cv2.LINE_AA)
        # image_array = draw_boxes(frame_rgb, pred_boxes, pred_classes, pred_scores, class_names, colors)
        cv2.imwrite(os.path.join('./',result_dir, image_name.split(os.path.sep)[-1]), image_array)

    
    # Update the FPS counter
    fps.update()
    fps.stop()
    fps_count = fps.fps()
    #if save_result:
    #    
    #    #color = (255, 255, 255)
    #    #cv2.putText(frame, f"FPS: {fps_count:.2f}", (8, 24), cv2.FONT_HERSHEY_SIMPLEX, 
    #    #                                    0.5, color, 2, cv2.LINE_AA)
    #    # Display the processed image
       

# sort pred_classes_records for each class according to score
for pred_class_list in pred_classes_records.values():
        pred_class_list.sort(key=lambda ele: ele[2], reverse=True)

AP, _ = compute_AP_COCO(annotation_records, gt_classes_records, pred_classes_records, class_names, None)
scale_gt_classes_records = get_scale_gt_dict(gt_classes_records, class_names)
compute_AP_COCO_Scale(annotation_records, scale_gt_classes_records, pred_classes_records, class_names)
## Stop the timer and display FPS information
fps.stop()
print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
print("[INFO] elapsed FPS: {:.2f}".format(fps.fps()))

# Stop the face detector
dpu_face_detector.stop()
del densebox_dpu

# Cleanup
#cv2.destroyAllWindows()
#medidor.detener()