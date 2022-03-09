from tkinter.tix import Tree
import cv2
import os
import numpy as np
import torch
import torch.nn as nn
import torchvision
from pytorch_grad_cam import AblationCAM, EigenCAM, GradCAMPlusPlus, ScoreCAM
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
from pytorch_grad_cam.ablation_layer import AblationLayerFasterRCNN
from pytorch_grad_cam.utils.model_targets import FasterRCNNBoxScoreTarget
from pytorch_grad_cam.utils.reshape_transforms import fasterrcnn_reshape_transform
from pytorch_grad_cam.utils.image import show_cam_on_image, scale_accross_batch_and_channels, scale_cam_image

def img_list(input,only_name=False, recursive=True):
    match_files = []
    for root, dirnames, filenames in os.walk(input):
        for fn in filenames:
            if fn.split('.')[-1] in ['jpg']:
                if only_name:
                    p = fn
                else:
                    p = os.path.join(root, fn)
                match_files.append(p)
        if not recursive:
            break
    return match_files

def renormalize_cam_in_bounding_boxes(boxes, image_float_np, grayscale_cam):
    """Normalize the CAM to be in the range [0, 1] 
    inside every bounding boxes, and zero outside of the bounding boxes. """
    renormalized_cam = np.zeros(grayscale_cam.shape, dtype=np.float32)
    for x1, y1, x2, y2 in boxes:
        renormalized_cam[y1:y2, x1:x2] = scale_cam_image(grayscale_cam[y1:y2, x1:x2].copy())    
    renormalized_cam = scale_cam_image(renormalized_cam)
    eigencam_image_renormalized = show_cam_on_image(image_float_np, renormalized_cam, use_rgb=True)
    image_with_bounding_boxes = draw_boxes(boxes, labels, classes, eigencam_image_renormalized)
    return image_with_bounding_boxes

def predict(input_tensor, model, device, detection_threshold):
    outputs = model(input_tensor)
    # print(outputs)
    pred_classes = [coco_names[i] for i in outputs[0]['labels'].cpu().numpy()]
    # print(pred_classes)
    pred_labels = outputs[0]['labels'].cpu().numpy()
    pred_scores = outputs[0]['scores'].detach().cpu().numpy()
    # print(pred_scores)
    pred_bboxes = outputs[0]['boxes'].detach().cpu().numpy()
    
    boxes, classes, labels, indices = [], [], [], []
    for index in range(len(pred_scores)):
        if pred_scores[index] >= detection_threshold:
            # print(index)
            boxes.append(pred_bboxes[index].astype(np.int32))
            classes.append(pred_classes[index])
            labels.append(pred_labels[index])
            indices.append(index)
    boxes = np.int32(boxes)
    # print(classes)
    return boxes, classes, labels, indices

def draw_boxes(boxes, labels, classes, image):
    for i, box in enumerate(boxes):
        color = COLORS[labels[i]]
        cv2.rectangle(
            image,
            (int(box[0]), int(box[1])),
            (int(box[2]), int(box[3])),
            color, 2
        )
        cv2.putText(image, classes[i], (int(box[0]), int(box[1] - 5)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2,
                    lineType=cv2.LINE_AA)
    return image
# coco_names = ['__background__','plug', 'bolt', 'nut', 'fastner']
coco_names = ['plug', 'bolt', 'nut', 'fastner']

# coco_names = ['__background__', 'person', 'bicycle', 'car', 'motorcycle', 'airplane', \
#               'bus', 'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'N/A', 
#               'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 
#               'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'N/A', 'backpack', 'umbrella',
#               'N/A', 'N/A', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard',
#               'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard',
#               'surfboard', 'tennis racket', 'bottle', 'N/A', 'wine glass', 'cup', 'fork',
#               'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange',
#               'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch',
#               'potted plant', 'bed', 'N/A', 'dining table', 'N/A', 'N/A', 'toilet',
#               'N/A', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'microwave',
#               'oven', 'toaster', 'sink', 'refrigerator', 'N/A', 'book', 'clock', 'vase',
#               'scissors', 'teddy bear', 'hair drier', 'toothbrush']


# This will help us create a different color for each class
COLORS = np.random.uniform(0, 255, size=(len(coco_names), 3))

import requests
import torchvision
from PIL import Image
# image_url = "https://raw.githubusercontent.com/jacobgil/pytorch-grad-cam/master/examples/both.png"
# image = np.array(Image.open(requests.get(image_url, stream=True).raw))
# image =cv2.imread('/home/user/Project/mmdetection/datasets/hyundai_xai/test/JPEGImages/5_item10(0010)_KA4.jpg')
# image_float_np = np.float32(image) / 255
# define the torchvision image transforms
transform = torchvision.transforms.Compose([
    torchvision.transforms.ToTensor(),
])

# input_tensor = transform(image)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(device)
# input_tensor = input_tensor.to(device)
# # Add a batch dimension:
# input_tensor = input_tensor.unsqueeze(0)
print('check')
torch.cuda.empty_cache()
num_classes = 4
model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=False)
in_features = model.roi_heads.box_predictor.cls_score.in_features
model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)

target_layers = [model.backbone]

model.load_state_dict(torch.load('hyundai_xai/model_14.pt'))


with torch.no_grad():
    model.eval().to(device)
# torch.no_grad()

im_list = img_list('test_images')

for img in im_list:
    new_img = os.path.basename(img)
    new_img = new_img.split('.')[0]

    image =cv2.imread(img)
    image_float_np = np.float32(image) / 255
    input_tensor = transform(image)
    input_tensor = input_tensor.to(device)
    # Add a batch dimension:
    input_tensor = input_tensor.unsqueeze(0)

    # Run the model and display the detections
    boxes, classes, labels, indices = predict(input_tensor, model, device, 0.9)
    # print(classes)
    # print('@@@@@@@')
    # print(labels)
    # print(classes)
    # print(boxes)
    # print('@@@@@@')
    
    image = draw_boxes(boxes, labels, classes, image)

    cv2.imwrite(f'output/re/{new_img}_ori.jpg',image)

    # target_layers = [model.backbone]
    
    # print('@@@@@@@')
    # print(labels)
    # print(classes)
    # print(boxes)
    # print('@@@@@@')
    
    targets = [FasterRCNNBoxScoreTarget(labels=labels, bounding_boxes=boxes)]

    # model = nn.DataParallel(model)
    # model.eval().to(device)
    # cam = EigenCAM(model,
    #             target_layers, 
    #             use_cuda=torch.cuda.is_available(),
    #             reshape_transform=fasterrcnn_reshape_transform)

    # grayscale_cam = cam(input_tensor, targets=targets)
    # grayscale_cam = grayscale_cam[0, :]

    # cam = GradCAMPlusPlus(model,
    #             target_layers, 
    #             use_cuda=torch.cuda.is_available(),
    #             reshape_transform=fasterrcnn_reshape_transform)

    # cam = ScoreCAM(model=model,
    #             target_layers=target_layers, 
    #             use_cuda=torch.cuda.is_available(),
    #             reshape_transform=fasterrcnn_reshape_transform)
    # torch.cuda.empty_cache()
    # print('camsssss')
    # cam.batch_size = 1
    cam = AblationCAM(model,
               target_layers, 
               use_cuda=torch.cuda.is_available(), 
               reshape_transform=fasterrcnn_reshape_transform,
               ablation_layer=AblationLayerFasterRCNN())
    # Take the first image in the batch:
    # with torch.no_grad():
    grayscale_cam = cam(input_tensor, targets=targets, eigen_smooth=True)[0, :]
   
    cam_image = show_cam_on_image(image_float_np, grayscale_cam, use_rgb=False)
    # cam_image = show_cam_on_image(image_float_np, grayscale_cam, use_rgb=True)

    # And lets draw the boxes again:
    image_with_bounding_boxes = draw_boxes(boxes, labels, classes, cam_image)
    Image.fromarray(image_with_bounding_boxes)

    cv2.imwrite(f'output/re/{new_img}_out.jpg',image_with_bounding_boxes)
    cv2.imwrite(f'output/re/{new_img}_out2.jpg',renormalize_cam_in_bounding_boxes(boxes, image_float_np, grayscale_cam))