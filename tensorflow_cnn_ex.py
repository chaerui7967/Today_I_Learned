
#%%
# preprocessing
import tensorflow as tf
from tensorflow.keras.preprocessing import image_dataset_from_directory
import matplotlib.pyplot as plt
import cv2

# print(cv2.imread('/Users/chaegilho/Desktop/fashion_data/Fancy_Pop/moschino-048-1366.jpg').shape)

b_size = 32 # 임의로 조정
img_h, img_w = 180, 180  # 50,90,180
data_dir = '/Users/chaegilho/Desktop/fashion_data'
# data_dir = '/Users/chaegilho/Desktop/test' 

train_ds = image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset='training',
    seed=123,
    image_size=(img_h, img_w),
    batch_size = b_size
)

class_names = train_ds.class_names
# print(train_ds.class_names)

val_ds = image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset='validation',
    seed=123,
    image_size=(img_h,img_w),
    batch_size=b_size
)

# # print image
# plt.figure(figsize=(100,100))
# for images, labels in train_ds.take(1):
#     for i in range(9):
#         ax = plt.subplot(3,3, i+1)
#         plt.imshow(images[i].numpy().astype('uint8'))
#         plt.title(train_ds.class_names[labels[i]])
#         plt.axis('off')

# for img_batch, label_batch in train_ds:
#     print(img_batch.shape)
#     print(label_batch.shape)
#     break

# normalization
# normalization_layer = tf.keras.layers.experimental.preprocessing.Rescaling(1./255) # -1~1 경우 1./127.5, offset=-1
# normalized_ds = train_ds.map(labda x, y : (normalization_layer(x), y))

autotune = tf.data.AUTOTUNE

train_ds = train_ds.cache().prefetch(buffer_size=autotune)
val_ds = val_ds.cache().prefetch(buffer_size=autotune)

# 훈련
from tensorflow.keras import models, layers
num_classes = len(class_names)

model = models.Sequential()
model.add(layers.experimental.preprocessing.Rescaling(1./255))
model.add(layers.Conv2D(32, 3, activation='relu'))
model.add(layers.MaxPooling2D())
model.add(layers.Conv2D(32, 3, activation='relu'))
model.add(layers.MaxPooling2D())
model.add(layers.Conv2D(32, 3, activation='relu'))
model.add(layers.MaxPooling2D())

model.add(layers.Flatten())
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(num_classes))

model.compile(
    optimizer='adam',
    loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=['accuracy']
)

model.fit(
    train_ds,
    validation_data = val_ds,
    epochs=3
)










