# Copyright 2019 Xilinx Inc.
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

#!/usr/bin/python3
# -*- coding=utf-8 -*-
"""Miscellaneous utility functions."""

import os
import numpy as np
import time
from enum import Enum
import cv2, colorsys
from PIL import Image
from matplotlib.colors import rgb_to_hsv, hsv_to_rgb




def get_custom_objects():
    '''
    form up a custom_objects dict so that the customized
    layer/function call could be correctly parsed when keras
    .h5 model is loading or converting
    '''
    custom_objects_dict = {
        'tf': tf,
        'swish': swish,
        'hard_sigmoid': hard_sigmoid,
        'hard_swish': hard_swish,
        'mish': mish
    }

    return custom_objects_dict


def get_multiscale_list():
    input_shape_list = [(320,320), (352,352), (384,384), (416,416), (448,448), (480,480), (512,512), (544,544), (576,576), (608,608)]

    return input_shape_list


def resize_anchors(base_anchors, target_shape, base_shape=(416,416)):
    '''
    original anchor size is clustered from COCO dataset
    under input shape (416,416). We need to resize it to
    our train input shape for better performance
    '''
    return np.around(base_anchors*target_shape[::-1]/base_shape[::-1])


def get_classes(classes_path):
    '''loads the classes'''
    with open(classes_path) as f:
        class_names = f.readlines()
    class_names = [c.strip() for c in class_names]
    return class_names

def get_anchors(anchors_path):
    '''loads the anchors from a file'''
    with open(anchors_path) as f:
        anchors = f.readline()
    anchors = [float(x) for x in anchors.split(',')]
    return np.array(anchors).reshape(-1, 2)

def get_colors(number, bright=True):
    """
    Generate random colors for drawing bounding boxes.
    To get visually distinct colors, generate them in HSV space then
    convert to RGB.
    """
    if number <= 0:
        return []

    brightness = 1.0 if bright else 0.7
    hsv_tuples = [(x / number, 1., brightness)
                  for x in range(number)]
    colors = list(map(lambda x: colorsys.hsv_to_rgb(*x), hsv_tuples))
    colors = list(
        map(lambda x: (int(x[0] * 255), int(x[1] * 255), int(x[2] * 255)),
            colors))
    np.random.seed(10101)  # Fixed seed for consistent colors across runs.
    np.random.shuffle(colors)  # Shuffle colors to decorrelate adjacent classes.
    np.random.seed(None)  # Reset seed to default.
    return colors

def get_dataset(annotation_file, shuffle=True):
    with open(annotation_file) as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]

    if shuffle:
        np.random.seed(int(time.time()))
        np.random.shuffle(lines)
        #np.random.seed(None)

    return lines

labelType = Enum('labelType', ('LABEL_TOP_OUTSIDE',
                               'LABEL_BOTTOM_OUTSIDE',
                               'LABEL_TOP_INSIDE',
                               'LABEL_BOTTOM_INSIDE',))

def draw_label(image, text, color, coords, label_type=labelType.LABEL_TOP_OUTSIDE):
    font = cv2.FONT_HERSHEY_PLAIN
    font_scale = 1.
    (text_width, text_height) = cv2.getTextSize(text, font, fontScale=font_scale, thickness=1)[0]

    padding = 5
    rect_height = text_height + padding * 2
    rect_width = text_width + padding * 2

    (x, y) = coords

    if label_type == labelType.LABEL_TOP_OUTSIDE or label_type == labelType.LABEL_BOTTOM_INSIDE:
        cv2.rectangle(image, (x, y), (x + rect_width, y - rect_height), color, cv2.FILLED)
        cv2.putText(image, text, (x + padding, y - text_height + padding), font,
                    fontScale=font_scale,
                    color=(255, 255, 255),
                    lineType=cv2.LINE_AA)
    else: # LABEL_BOTTOM_OUTSIDE or LABEL_TOP_INSIDE
        cv2.rectangle(image, (x, y), (x + rect_width, y + rect_height), color, cv2.FILLED)
        cv2.putText(image, text, (x + padding, y + text_height + padding), font,
                    fontScale=font_scale,
                    color=(255, 255, 255),
                    lineType=cv2.LINE_AA)

    return image

def draw_boxes(image, boxes, classes, scores, class_names, colors, show_score=True):
    if boxes is None or len(boxes) == 0 or classes is None or len(classes) == 0:
        return image

    height, width, _ = image.shape
    label_type_top_outside = labelType.LABEL_TOP_OUTSIDE
    label_type_bottom_outside = labelType.LABEL_BOTTOM_OUTSIDE
    label_type_top_inside = labelType.LABEL_TOP_INSIDE

    for box, cls, score in zip(boxes, classes, scores):
        ymin, xmin, ymax, xmax = box.astype(int)

        class_name = class_names[cls]
        if show_score:
            label = '{} {:.2f}'.format(class_name, score * 100)
        else:
            label = '{}'.format(class_name)

        if colors is None:
            color = (0, 0, 0)
        else:
            color = colors[cls]

        if ymin > 20:
            label_coords = (xmin, ymin)
            label_type = label_type_top_outside
        elif ymin <= 20 and ymax <= height - 20:
            label_coords = (xmin, ymax)
            label_type = label_type_bottom_outside
        elif ymax > height - 20:
            label_coords = (xmin, ymin)
            label_type = label_type_top_inside

        cv2.rectangle(image, (xmin, ymin), (xmax, ymax), color, 1, cv2.LINE_AA)
        image = draw_label(image, label, color, label_coords, label_type)

    return image


def draw_box(box,cls,score,class_names,colors,image,show_score=True):
    height, width, _ = image.shape
    label_type_top_outside = labelType.LABEL_TOP_OUTSIDE
    label_type_bottom_outside = labelType.LABEL_BOTTOM_OUTSIDE
    label_type_top_inside = labelType.LABEL_TOP_INSIDE
    ymin, xmin, ymax, xmax = box.astype(int)
    adjustment = -0.15
    box_height = ymax-ymin
    box_width = xmax-xmin
    ymin    += int(adjustment*box_height)
    ymax   -= int(adjustment*box_height)
    xmin   += int(adjustment*box_width)
    xmax  -= int(adjustment*box_width)  
    class_name = class_names[cls]
    if show_score:
        label = '{} {:.2f}'.format(class_name, score * 100)
    else:
        label = '{}'.format(class_name)
    if colors is None:
        color = (0, 0, 0)
    else:
        color = colors[cls]
    if ymin > 20:
        label_coords = (xmin, ymin)
        label_type = label_type_top_outside
    elif ymin <= 20 and ymax <= height - 20:
        label_coords = (xmin, ymax)
        label_type = label_type_bottom_outside
    elif ymax > height - 20:
        label_coords = (xmin, ymin)
        label_type = label_type_top_inside
    cv2.rectangle(image, (xmin, ymin), (xmax, ymax), color, 1, cv2.LINE_AA)
    image = draw_label(image, label, color, label_coords, label_type)
