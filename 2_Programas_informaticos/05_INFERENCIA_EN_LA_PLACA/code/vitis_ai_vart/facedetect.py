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


from ctypes import *
import cv2
import os
import threading
import time
import sys
import numpy as np
from numpy import float32
import math

import vart
#from utils import get_child_subgraph_dpu

import tf_yolov3_helper
  
def time_it(msg,start,end):
    print("[INFO] {} took {:.8} seconds".format(msg,end-start))

def nms_boxes(boxes, scores, nms_threshold):
    """
    Suppress non-maximal boxes.

    # Arguments
        boxes: ndarray, boxes of objects.
        scores: ndarray, scores of objects.
        nms_threshold: threshold for NMS algorithm

    # Returns
        keep: ndarray, index of effective boxes.
    """
    x1 = boxes[:, 0]
    y1 = boxes[:, 1]
    x2 = boxes[:, 2]
    y2 = boxes[:, 3]

    areas = (x2-x1+1)*(y2-y1+1)
    order = scores.argsort()[::-1]

    keep = []
    while order.size > 0:
        i = order[0]
        keep.append(i)

        xx1 = np.maximum(x1[i], x1[order[1:]])
        yy1 = np.maximum(y1[i], y1[order[1:]])
        xx2 = np.minimum(x2[i], x2[order[1:]])
        yy2 = np.minimum(y2[i], y2[order[1:]])

        w1 = np.maximum(0.0, xx2 - xx1 + 1)
        h1 = np.maximum(0.0, yy2 - yy1 + 1)
        inter = w1 * h1

        ovr = inter / (areas[i] + areas[order[1:]] - inter)
        inds = np.where(ovr <= nms_threshold)[0]  # threshold
        order = order[inds + 1]

    return keep

def softmax_2(data):
    '''
    Calculate 2-class softmax on CPU
      y = exp(x-max(x) / sum( exp(x-max(x)) )
    Using the following properties
      a^(b-c) = a^b / a^c
      e^x / (e^max(x) * sum(e^x/e^max(x)))
      e^x / sum(e^x)
    We simplify to
      y = exp(x) / sum( exp(x) )

    # Arguments
        data: ndarray, vector of input data

    # Returns
        softmax: ndarray, softmax result
    '''

    data_exp = np.zeros(data.shape)
    data_sum = np.zeros(data.shape)
    result = np.zeros(data.shape)
    data_exp = np.exp(data)
    data_sum[:,0] = np.sum(data_exp, axis=1)
    data_sum[:,1] = data_sum[:,0]
    result = data_exp / data_sum

    return result


class FaceDetect():
#  def __init__(self, dpu_xmodel, detThreshold=0.55, nmsThreshold=0.35):
#    #"""Create Runner"""
#    dpu_graph = xir.Graph.deserialize(dpu_xmodel)
#    dpu_subgraphs = get_child_subgraph_dpu(dpu_graph)
#    assert len(dpu_subgraphs) == 1 # only one DPU kernel
#    print("[INFO] FaceDetect dpu_xmodel=",dpu_xmodel)
#    dpu = vart.Runner.create_runner(dpu_subgraphs[0],"run")
	  
  def __init__(self, dpu, class_names, anchors, detThreshold=0.55, nmsThreshold=0.35):

    self.dpu = dpu
    self.class_names = class_names
    self.anchors = anchors

    self.detThreshold = detThreshold
    self.nmsThreshold = nmsThreshold

    self.inputTensors = []
    self.outputTensors = []
    self.inputChannels = []
    self.inputHeight = []
    self.inputWidth = []
    self.inputShape = []
    self.output0Channels = []
    self.output0Height = []
    self.output0Width = []
    self.output0Size = []
    self.output0Shape = []
    self.output1Channels = []
    self.output1Height = []
    self.output1Width = []
    self.output1Size = []
    self.output1Shape = []

  def start(self):
    dpu = self.dpu
    print("[INFO] facedetect runner=",dpu)

    inputTensors = dpu.get_input_tensors()
    print("[INFO] inputTensors=",inputTensors)
    
    outputTensors = dpu.get_output_tensors()
    print("[INFO] outputTensors=",outputTensors)
    
    print("[INFO] inputTensors[0]=",inputTensors[0])
    inputHeight = inputTensors[0].dims[1]
    inputWidth = inputTensors[0].dims[2]
    inputChannels = inputTensors[0].dims[3]
    #print("[INFO] input tensor : format=NHWC, Height=",inputHeight," Width=",inputWidth,", Channels=", inputChannels)
    
    print("[INFO] outputTensors[0]=",outputTensors[0])
    output0Height = outputTensors[0].dims[1]
    output0Width = outputTensors[0].dims[2]
    output0Channels = outputTensors[0].dims[3]
    #print("[INFO] output[0] tensor : format=NHWC, height=",output0Height," width=",output0Width,", channels=",output0Channels)
    
    print("[INFO] outputTensors[1]=",outputTensors[1])
    output1Height = outputTensors[1].dims[1]
    output1Width = outputTensors[1].dims[2]
    output1Channels = outputTensors[1].dims[3]
    #print("[INFO] output[1] tensor : format=NHWC, height=",output1Height," width=",output1Width,", channels=",output1Channels)
    
    print("[INFO] outputTensors[2]=",outputTensors[2])
    output2Height = outputTensors[2].dims[1]
    output2Width = outputTensors[2].dims[2]
    output2Channels = outputTensors[2].dims[3]
    #print("[INFO] output[1] tensor : format=NHWC, height=",output1Height," width=",output1Width,", channels=",output1Channels)

    output0Size = output0Height*output0Width*output0Channels
    output1Size = output1Height*output1Width*output1Channels
    output2Size = output2Height*output2Width*output2Channels

    inputShape = (1,inputHeight,inputWidth,inputChannels)
    print("[INFO] inputShape=",inputShape)
    output0Shape = (1,output0Height,output0Width,output0Channels)
    print("[INFO] output0Shape=",output0Shape)
    output1Shape = (1,output1Height,output1Width,output1Channels)
    print("[INFO] output1Shape=",output1Shape)
    output2Shape = (1,output2Height,output2Width,output2Channels)
    print("[INFO] output2Shape=",output2Shape)

    self.inputTensors = inputTensors
    self.outputTensors = outputTensors
    self.inputChannels = inputChannels
    self.inputHeight = inputHeight
    self.inputWidth = inputWidth
    self.inputShape = inputShape
    self.output0Channels = output0Channels
    self.output0Height = output0Height
    self.output0Width = output0Width
    self.output0Size = output0Size
    self.output0Shape = output0Shape
    self.output1Channels = output1Channels
    self.output1Height = output1Height
    self.output1Width = output1Width
    self.output1Size = output1Size
    self.output1Shape = output1Shape
    self.output2Channels = output2Channels
    self.output2Height = output2Height
    self.output2Width = output2Width
    self.output2Size = output2Size
    self.output2Shape = output2Shape

  def config(self, detThreshold, nmsThreshold):
    self.detThreshold = detThreshold
    self.nmsThreshold = nmsThreshold
    print("[INFO] facedetect config : detThreshold = ",self.detThreshold," nmsThreshold = ",self.nmsThreshold)

  def process(self,img):
    #print("[INFO] facedetect process")

    dpu = self.dpu
    #print("[INFO] facedetect runner=",dpu)

    inputChannels = self.inputChannels
    inputHeight = self.inputHeight
    inputWidth = self.inputWidth
    inputShape = self.inputShape
    output0Channels = self.output0Channels
    output0Height = self.output0Height
    output0Width = self.output0Width
    output0Size = self.output0Size
    output0Shape = self.output0Shape
    output1Channels = self.output1Channels
    output1Height = self.output1Height
    output1Width = self.output1Width
    output1Size = self.output1Size
    output1Shape = self.output1Shape
    output2Channels = self.output2Channels
    output2Height = self.output2Height
    output2Width = self.output2Width
    output2Size = self.output2Size
    output2Shape = self.output2Shape

    imgHeight = img.shape[0]
    imgWidth  = img.shape[1]
    scale_h = imgHeight / inputHeight
    scale_w = imgWidth / inputWidth
    
    """ Image pre-processing """
    #print("[INFO] process - pre-processing - normalize ")
    # normalize
    #img = img - 128.0
    #print("[INFO] process - pre-processing - resize ")
    # resize
    img = cv2.resize(img, (inputWidth,inputHeight))

    """ Prepare input/output buffers """
    #print("[INFO] process - prep input buffer ")
    inputData = []
    inputData.append(np.empty((inputShape),dtype=np.float32,order='C'))
    inputImage = inputData[0]
    inputImage[0,...] = img
    inputImage /= 255.

    #print("[INFO] process - prep output buffer ")
    outputData = []
    outputData.append(np.empty((output0Shape),dtype=np.float32,order='C'))
    outputData.append(np.empty((output1Shape),dtype=np.float32,order='C'))
    outputData.append(np.empty((output2Shape),dtype=np.float32,order='C'))

    """ Execute model on DPU """
    #print("[INFO] process - execute ")
    job_id = dpu.execute_async( inputData, outputData )
    dpu.wait(job_id)

    """ Retrieve output results """    
    #print("[INFO] process - get outputs ")
    #OutputData0 = np.reshape(outputData[0], output0Shape)
    #OutputData1 = np.reshape(outputData[1], output1Shape)
    #OutputData2 = np.reshape(outputData[2], output2Shape)
    #yolo_outputs = [OutputData2, OutputData1, OutputData0]
    yolo_outputs = outputData[::-1]
    yolo_image_shape = (imgHeight, imgWidth, )
    yolo_input_shape = (inputWidth,inputHeight)
    
    # We can call the evaluate() function defined previously now.
    # Depending on how many objects can be identified in the picture, the function returns a
    # list of bounding box coordinates, a list of probability scores, and a list of class indexes.
    boxes, scores, classes = tf_yolov3_helper.eval(
        yolo_outputs, yolo_image_shape, yolo_input_shape,
        self.class_names, self.anchors, self.detThreshold)
    return (boxes, scores, classes)

  def stop(self):
    #"""Destroy Runner"""
    del self.dpu
	
    self.dpu = []
    self.inputTensors = []
    self.outputTensors = []
    self.tensorFormat = []
    self.input0Channels = []
    self.inputHeight = []
    self.inputWidth = []
    self.inputShape = []
    self.output0Channels = []
    self.output0Height = []
    self.output0Width = []
    self.output0Size = []
    self.output1Channels = []
    self.output1Height = []
    self.output1Width = []
    self.output1Size = []

