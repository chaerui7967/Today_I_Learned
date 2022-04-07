import numpy as np
from PIL import Image
from pathlib import Path
import base64
import cv2
import os
import json
import io

# 빈 labelme 파일 생성 --> 위험물 데이터에서 background 데이터 생성을 위해

def img_arr_to_b64(img_arr):
    img_pil = Image.fromarray(img_arr)
    # img_pil = Image.open(img_arr)
    f = io.BytesIO()
    img_pil.save(f,format='PNG')
    # f.seek(0)
    # f.read
    # img_pil.save(f, format='JPEG')
    img_bin = f.getvalue()
    # return img_bin

    if hasattr(base64, 'encodebytes'):
        img_b64 = base64.encodebytes(img_bin)
    else:
        img_b64 = base64.encodestring(img_bin)
    return img_b64

def main(input_dir):
    annos=[]
    img_dir=[]

    for root, _, files in os.walk(input_dir):
        for input in files:
            if not (input.endswith('.png') or input.endswith('.jpg')):
                continue
            img = os.path.join(root,input)
            img_dir.append(img)

            # anno = os.path.join(root, input)
            # annos.append(anno)
            
    for i in img_dir:
        img = cv2.imread(i)
        img = img.convert('RGB')
        cv2.imwrite(i,img)
        # anno_data = {
        #     'version' : '4.5.13',
        #     'flags' : {},
        #     "shapes" : []
        # }
        # anno_data['imagePath'] = os.path.basename(i)

        # path = Path(i).parent
        # im_name = os.path.basename(i)
        # anno_name = '.'.join(im_name.split('.')[:-1]) + '.txt'
        # with open(f'{os.path.join(path,anno_name)}', 'w') as a:
        #     a.write(' ')
        # # img = cv2.imread(i)
        # # # anno_data['imageData'] = 
        # # anno_data['imageData'] = img_arr_to_b64(img).decode('utf8')
        # # # print(anno_data['imageData'])
        # # with open(f'{os.path.join(path,anno_name)}', 'w') as a:
        # #     json.dump(anno_data,a)
        # # # print(os.path.join(path,anno_name))
    

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Extract categories.')
    parser.add_argument('-i', '--image_dir', required=True, help='Image directory')
    args = parser.parse_args()

    main(args.image_dir)