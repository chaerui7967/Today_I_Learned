import numpy as np
from PIL import Image
import base64
import cv2
import os
import json
import io

# def img_b64_to_arr(img_b64):
#     f = io.BytesIO()
#     f.write(base64.b64decode(img_b64))
#     img_arr = np.array(Image.open(f))
#     print(img_arr)
#     return img_arr

def img_arr_to_b64(img_arr):
    img_pil = Image.fromarray(img_arr)
    f = io.BytesIO()
    img_pil.save(f, format='PNG')
    img_bin = f.getvalue()
    if hasattr(base64, 'encodebytes'):
        img_b64 = base64.encodebytes(img_bin)
    else:
        img_b64 = base64.encodestring(img_bin)
    return img_b64

def main(input_dir, out_dir):
    annos=[]
    # imgs=[]
    
    for root, _, files in os.walk(input_dir):
        for input in files:
            if not input.endswith('.json'):
                continue
                # img = os.path.join(root,input)
                # imgs.append(img)

                # anno_file = input.split('.')[0] + '.json'

            anno = os.path.join(root, input)
            annos.append(anno)
            
    # for i,j in zip(annos,imgs):
        # print(i, j)
    for i in annos:
        with open(i, 'r') as a:
            anno_data = json.load(a)
        
        for an in anno_data['shapes']:
            if an['label'] not in ['indicator']:
                continue
            x1 = int(an['points'][0][0])
            y1 = int(an['points'][0][1])
            x2 = int(an['points'][1][0])
            y2 = int(an['points'][1][1])
            anno_data['imageHeight'] = y2 - y1
            anno_data['imageWidth'] = x2 - x1
            anno_data['shapes'].remove(an)
            break
        
        for change in anno_data['shapes']:
            if change['label'] in ['indicator']:
                continue
            change['points'][0][0] -= x1
            change['points'][0][1] -= y1
            change['points'][1][0] -= x1
            change['points'][1][1] -= y1
            # print(change)
        img_name = anno_data['imagePath']
        im_name = img_name.split('.')[0]
        print(im_name)
        # print(img)
        img_path = os.path.join(os.path.dirname(i),img_name)
        # print(img_path)
        img = cv2.imread(img_path)
        crop_img = img[y1:y2, x1:x2]
        
        im_name2 = im_name+'.jpg'
        crop_name = os.path.join(out_dir, im_name2)
        cv2.imwrite(crop_name, crop_img)
        # cv2.imshow('img',crop_img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        # img_data = base64.b64decode(img)
        # print(img_data)
        # img_arr = img_b64_to_arr(img_data)
        crop_data = img_arr_to_b64(crop_img).decode('utf8')
        # print(crop_data)

        # print(anno_data['imageData'] == crop_data)
        # print(type(crop_data))

        anno_data['imageData'] = crop_data

        anno_name = im_name + '.json'
        outpath = os.path.join(out_dir, anno_name)
        with open(outpath, 'w') as wri:
            json.dump(anno_data, wri, indent="\t")



    #         return

    # return



if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Extract categories.')
    parser.add_argument('-i', '--image_dir', required=True, help='Image directory')
    # parser.add_argument('-j', '--annotation_dir', required=True, help='json file')
    parser.add_argument('-o', '--output_dir', required=True, help='Output')
    args = parser.parse_args()

    main(args.image_dir, args.output_dir)