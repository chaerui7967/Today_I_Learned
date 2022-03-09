from cgi import test
import os
import numpy as np
import matplotlib.patches as patches
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from PIL import Image
import torchvision
from torchvision import transforms, datasets, models
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
import time
import torch

# from mAP_cal import predict,mean_average_precision

from torch.utils.tensorboard import SummaryWriter
writer = SummaryWriter()
criterion = torch.nn.MSELoss()


# import torch.nn.functional as F
from tqdm import tqdm
from engine import evaluate

# import utils_ObjectDetection as utils

if torch.cuda.is_available():    
    device = torch.device("cuda")
    print('There are %d GPU(s) available.' % torch.cuda.device_count())
    print('We will use the GPU:', torch.cuda.get_device_name(0))

else:
    print('No GPU available, using the CPU instead.')
    device = torch.device("cpu")



def generate_box(obj):
    
    xmin = float(obj.find('xmin').text)
    ymin = float(obj.find('ymin').text)
    xmax = float(obj.find('xmax').text)
    ymax = float(obj.find('ymax').text)
    
    return [xmin, ymin, xmax, ymax]

adjust_label = 1

def generate_label(obj):

    if obj.find('name').text == "plug":

        return 0

    elif obj.find('name').text == "bolt":

        return 1
    
    elif obj.find('name').text == "nut":

        return 2

    elif obj.find('name').text == "fastner":

        return 3

    # return 0

def generate_target(file):
    # print(file)
    with open(file) as f:
        data = f.read()
        soup = BeautifulSoup(data, "html.parser")
        objects = soup.find_all("object")
        # print(objects)
        num_objs = len(objects)

        boxes = []
        labels = []
        for i in objects:
            boxes.append(generate_box(i))
            labels.append(generate_label(i))
        # print(labels)

        boxes = torch.as_tensor(boxes, dtype=torch.float32) 
        labels = torch.as_tensor(labels, dtype=torch.int64) 
        
        target = {}
        target["boxes"] = boxes
        target["labels"] = labels
        
        return target

class MaskDataset(object):
    def __init__(self, transforms, path):
        '''
        path: path to train folder or test folder
        '''
        # transform module과 img path 경로를 정의
        self.transforms = transforms
        self.path = path
        self.imgs = list(sorted(os.listdir(self.path)))


    def __getitem__(self, idx): #special method
        # load images ad masks
        file_image = self.imgs[idx]
        file_label = self.imgs[idx][:-3] + 'xml'
        img_path = os.path.join(self.path, file_image)
        
        if 'test' in self.path:
            label_path = os.path.join("test_annotations/", file_label)
        else:
            label_path = os.path.join("annotations/", file_label)

        img = Image.open(img_path).convert("RGB")
        #Generate Label
        target = generate_target(label_path)
        
        if self.transforms is not None:
            img = self.transforms(img)

        return img, target

    def __len__(self): 
        return len(self.imgs)

data_transform = transforms.Compose([  # transforms.Compose : list 내의 작업을 연달아 할 수 있게 호출하는 클래스
        transforms.ToTensor() # ToTensor : numpy 이미지에서 torch 이미지로 변경
    ])

def collate_fn(batch):
    return tuple(zip(*batch))

dataset = MaskDataset(data_transform, 'images/')
test_dataset = MaskDataset(data_transform, 'test_images/')

data_loader = torch.utils.data.DataLoader(dataset, batch_size=4, collate_fn=collate_fn)
test_data_loader = torch.utils.data.DataLoader(test_dataset, batch_size=2, collate_fn=collate_fn)

def get_model_instance_segmentation(num_classes):
    model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=False)
    in_features = model.roi_heads.box_predictor.cls_score.in_features
    model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)

    return model

model = get_model_instance_segmentation(4)

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu') 
model.to(device)

num_epochs = 1000
params = [p for p in model.parameters() if p.requires_grad]
optimizer = torch.optim.SGD(params, lr=0.005,
                                momentum=0.9, weight_decay=0.0005)

print('----------------------train start--------------------------')
num = 1
for epoch in range(num_epochs):
    start = time.time()
    model.train()
    i = 0    
    epoch_loss = 0
    for imgs, annotations in data_loader:
        
        # print(imgs)
        # print(annotations)

        i += 1
        imgs = list(img.to(device) for img in imgs)
        annotations = [{k: v.to(device) for k, v in t.items()} for t in annotations]
        # print(annotations)
        loss_dict = model(imgs, annotations)
        
        # print('@'*100)
        # print(loss_dict)
        # print('@'*100)

        losses = sum(loss for loss in loss_dict.values())

        writer.add_scalar("Loss/train", losses, epoch)

        optimizer.zero_grad()
        losses.backward()
        optimizer.step() 
        epoch_loss += losses

    with open('log.txt', 'a') as f:
        f.write(f'epoch : {epoch+1}, Loss : {epoch_loss}, time : {time.time() - start}')
        
    print(f'epoch : {epoch+1}, Loss : {epoch_loss}, time : {time.time() - start}')
    torch.save(model.state_dict(),f'hyundai_xai/model_{num}.pt')    
    num += 1


     # # map 계산
    # img_num=1
    # model.eval()
    # # evaluate(model, test_data_loader, device=device)
    # # print(model(imgs))
    

    #     pred_boxes, classes, labels, indices = predict(im, model, device, 0.5)
    #     pred_boxes = [img_num] + classes + pred_boxes
    #     print(pred_boxes)
    #     anno = [{a: b.to(device) for a, b in an.items()} for an in anno]
    #     true_boxes = [img_num] + anno[0]['labels'] + anno[0]['boxes']
    #     print(mean_average_precision(pred_boxes, true_boxes))
    #     img_num+=1
