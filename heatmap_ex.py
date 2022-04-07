#%%
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

# cv2 --> bgr 순서로 저장, matplot --> rgb 순서로 저장

heat = np.array([[1., 1., 1., 1., 1., 1., 1., 0., 0., 0.],
    [1., 1., 1., 1., 1., 1., 1., 0., 0., 0.],
    [1., 1., 1., 1., 1., 1., 1., 0., 0., 0.],
    [1., 1., 1., 1., 1., 1., 1., 0., 0., 0.],
    [1., 1., 1., 1., 1., 1., 1., 0., 0., 0.],
    [1., 1., 1., 1., 1., 1., 1., 0., 0., 0.],
    [1., 1., 1., 1., 1., 1., 1., 0., 0., 0.],
    [1., 1., 1., 1., 1., 1., 1., 0., 0., 0.],
    [1., 1., 1., 1., 1., 1., 1., 0., 0., 0.],
    [1., 1., 1., 1., 1., 1., 1., 0., 0., 0.]])

# plt.matshow(heat)
# plt.show()

img = cv2.imread('red70.jpg', 1)[:,:,::-1] 
# : : -1 역순으로 --> bgr -> rgb로 바꿈, 1(그냥),0(흑백),-1(alpha채널까지 --> 투명도)

heat = np.array(heat)
heat = cv2.resize(heat, (img.shape[1],img.shape[0])) # cam 결과 --> mask
print(heat[0])
# 색확인
for i in range(heat.shape[0]):
    # heat[i][-29] = 0 --> 경계선 그리기
    heat[i][-30] = 0.4 # 변경
경

# ---- cam 내부 계산 결과 ---
ratio = np.where(heat > 0.4, 1, 0)
ratio = np.sum(ratio) / (ratio.shape[0] * ratio.shape[1])
print(ratio)

img_ratio = np.where(heat > 0.5, heat, 0)
img_ratio = cv2.applyColorMap(np.uint8(255*img_ratio), cv2.COLORMAP_JET)
# cv2.imshow('ratio',img_ratio)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# cvtcolor = cv2.applyColorMap(np.uint8(255*heat), cv2.COLORMAP_HSV)  --> heatmap을 hsv로 먼저 바꾸면 이상해짐
# print('------------cvt _ heat 2 hsv -------------')
# print(cvtcolor[0][0])
# print(cvtcolor[0][-30])
# print(cvtcolor[0][-1])

heat = cv2.applyColorMap(np.uint8(255*heat), cv2.COLORMAP_JET)
## 기준점 찾기 bgr [31,255,226] hsv [172,88,100] cv2에서 hsv 범위는 [0-180,0-255,0-255]이므로 실제 hsv와 혼란 x

print('*'*100)
print(heat[0][0]) # 빨강 heatmap 기준 1. --> bgr (0,0,128)
# heatmap 0.5 (노랑) -->  130 255 126
print(heat[0][-30]) 
print(heat[0][-1]) # heatmap 0 (파랑) --> 128 0 0
hsv = cv2.cvtColor(heat, cv2.COLOR_BGR2HSV)
print('@'*100)
print(hsv[0][0]) # hsv로 바꿈 빨강 --> 0 255 128
print(hsv[0][-30]) # 노랑 --> 61 129 255
print(hsv[0][-1]) # 파랑 --> 120 255 128
print('-'*100)

cv2.imshow('heat', heat)
cv2.waitKey(0)
cv2.destroyAllWindows()