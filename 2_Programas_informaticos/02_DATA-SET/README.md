# Dataset

## Estructura

### TRAIN  Basada en DARNET

1. Create file `obj.names` in the directory `build\darknet\x64\data\`, with objects names - each in new line
2. Create file `obj.data` in the directory `build\darknet\x64\data\`, containing (where **classes = number of objects**):

  ```ini
  classes = 2
  train  = data/train.txt
  valid  = data/test.txt
  names = data/obj.names
  backup = backup/
  ```

3. Put image-files (.jpg) of your objects in the directory `build\darknet\x64\data\obj\`
4. You should label each object on images from your dataset. Use this visual GUI-software for marking bounded boxes of objects and generating annotation files for Yolo v2 & v3: https://github.com/AlexeyAB/Yolo_mark

It will create `.txt`-file for each `.jpg`-image-file - in the same directory and with the same name, but with `.txt`-extension, and put to file: object number and object coordinates on this image, for each object in new line:

`<object-class> <x_center> <y_center> <width> <height>`

  Where:

- `<object-class>` - integer object number from `0` to `(classes-1)`
- `<x_center> <y_center> <width> <height>` - float values **relative** to width and height of image, it can be equal from `(0.0 to 1.0]`
- for example: `<x> = <absolute_x> / <image_width>` or `<height> = <absolute_height> / <image_height>`
- attention: `<x_center> <y_center>` - are center of rectangle (are not top-left corner)

  For example for `img1.jpg` you will be created `img1.txt` containing:

  ```csv
  1 0.716797 0.395833 0.216406 0.147222
  0 0.687109 0.379167 0.255469 0.158333
  1 0.420312 0.395833 0.140625 0.166667
  ```

5. Create file `train.txt` in directory `build\darknet\x64\data\`, with filenames of your images, each filename in new line, with path relative to `darknet.exe`, for example containing:

  ```csv
  data/obj/img1.jpg
  data/obj/img2.jpg
  data/obj/img3.jpg
  ```

### EVAL  Basada en Keras yolov3


1. Create file `eval.txt` in data `file path file` `<x_min> <y_min> <x_max> <y_max>` -: 

  ```csv
./data/000000000001.jpg 916,1931,1359,2391,0 1774,1461,2135,1842,1 2462,1158,2765,1471,2
./data/000000000002.jpg 650,1617,1154,2100,0 1856,1461,2241,1890,0 2962,1374,3354,1789,2
./data/000000000003.jpg 623,2302,1239,2915,0 1559,1556,1957,1968,1 2189,1073,2526,1410,2
  ```

En el script de que estan numerados por orden para utilizar nuestro propio dataset anotarlo en formato COCO y seguir algo similar que con el dataset de COCO


la  version de 03_convert_data_to_eva_in_Kerasl ejecutarla dentro de la carpeta de keras-YOLOv3-model-set 