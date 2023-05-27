#!/bin/bash

mkdir coco
cd coco
mkdir images
cd images

wget -c http://images.cocodataset.org/zips/train2017.zip \
    http://images.cocodataset.org/zips/val2017.zip\
    http://images.cocodataset.org/zips/test2017.zip\
    http://images.cocodataset.org/zips/unlabeled2017.zip\

unzip train2017.zip \
    val2017.zip \
    test2017.zip \
    unlabeled2017.zip 

rm train2017.zip \
    val2017.zip \
    test2017.zip \
    unlabeled2017.zip 


cd ../
mkdir annotations
cd annotations

wget -c  http://images.cocodataset.org/annotations/annotations_trainval2017.zip \
    http://images.cocodataset.org/annotations/stuff_annotations_trainval2017.zip \
    http://images.cocodataset.org/annotations/image_info_test2017.zip \
    http://images.cocodataset.org/annotations/image_info_unlabeled2017.zip 

unzip annotations_trainval2017.zip \
    stuff_annotations_trainval2017.zip \
    image_info_test2017.zip \
    image_info_unlabeled2017.zip 

rm annotations_trainval2017.zip \
    stuff_annotations_trainval2017.zip \
    image_info_test2017.zip \ 
    image_info_unlabeled2017.zip