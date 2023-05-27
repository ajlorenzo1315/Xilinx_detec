# COCO

[coco](https://cocodataset.org/#detection-eval)

# Download

<pre>

bash download_dataset.sh

</pre>

*** Metricas ***

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