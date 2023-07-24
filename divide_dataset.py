# 用途：手动分割训练集和验证集，平衡数据分布
# 本文件用于统计建筑类（1类）在图像中的像素数，划分thershold，并进行文件移动

import os
import collections
import cv2
import numpy as np
import shutil
import random
ori_img_path = './Dataset/xbd_1024/socal/images/'
ori_mask_path = './Dataset/xbd_1024/socal/masks/'
save_train_img_path = './Dataset/xbd_1024/base_socal/train/images/'
save_train_mask_path = './Dataset/xbd_1024/base_socal/train/masks/'
save_val_img_path='./Dataset/xbd_1024/base_socal/val/images/'
save_val_mask_path = './Dataset/xbd_1024/base_socal/val/masks/'

os.makedirs(save_train_img_path, exist_ok=True)
os.makedirs(save_train_mask_path, exist_ok=True)
os.makedirs(save_val_img_path, exist_ok=True)
os.makedirs(save_val_mask_path, exist_ok=True)
have_build_more=[]
have_build_less=[]
no_build=[]
thershold=0.03
val_portion=0.2
mask_list = os.listdir(ori_mask_path)
# 统计各个分区文件
for file in mask_list:
    mask_file_path = os.path.join(ori_mask_path, file)
    img = cv2.imread(mask_file_path, cv2.IMREAD_UNCHANGED)

    all_pixels = len(img)*len(img[0])
    img = (img > 127) * 1
    build_pixels = np.sum(img)
    if build_pixels==0:
        no_build.append(file)
    elif build_pixels*1.0/all_pixels < thershold:
        have_build_less.append(file)
    else:
        have_build_more.append(file)

# shuffle
random.shuffle(no_build)
random.shuffle(have_build_less)
random.shuffle(have_build_more)

# val portion indexes
no_build_val = val_portion*len(no_build)
have_build_less_val = val_portion*len(have_build_less)
have_build_more_val = val_portion*len(have_build_more)

for i in range(len(no_build)):
    image_path = os.path.join(ori_img_path, no_build[i])
    mask_path = os.path.join(ori_mask_path, no_build[i])
    if i < no_build_val: # val part
        shutil.copy(image_path, save_val_img_path)
        shutil.copy(mask_path, save_val_mask_path)
    else:               # train part
        shutil.copy(image_path, save_train_img_path)
        shutil.copy(mask_path, save_train_mask_path)

for i in range(len(have_build_less)):
    image_path = os.path.join(ori_img_path, have_build_less[i])
    mask_path = os.path.join(ori_mask_path, have_build_less[i])
    if i < have_build_less_val: # val part
        shutil.copy(image_path, save_val_img_path)
        shutil.copy(mask_path, save_val_mask_path)
    else:               # train part
        shutil.copy(image_path, save_train_img_path)
        shutil.copy(mask_path, save_train_mask_path)

for i in range(len(have_build_more)):
    image_path = os.path.join(ori_img_path, have_build_more[i])
    mask_path = os.path.join(ori_mask_path, have_build_more[i])
    if i < have_build_more_val: # val part
        shutil.copy(image_path, save_val_img_path)
        shutil.copy(mask_path, save_val_mask_path)
    else:               # train part
        shutil.copy(image_path, save_train_img_path)
        shutil.copy(mask_path, save_train_mask_path)

print("total image num: "+str(len(mask_list)))
print("len(no_build) = {:d}, len(no_build_val) = {:f}".format(len(no_build), no_build_val))
print("len(have_build_less) = {:d}, len(have_build_less_val) = {:f}".format(len(have_build_less), have_build_less_val))
print("len(have_build_more) = {:d}, len(have_build_more_val) = {:f}".format(len(have_build_more), have_build_more_val))
train_files_num=len(os.listdir(save_train_img_path))
val_files_num=len(os.listdir(save_val_img_path))
print(train_files_num)
print(val_files_num)
if val_files_num+train_files_num==len(mask_list):
    print("success")
else:
    print("Error")


"""
total image num: 823
len(no_build) = 415, len(no_build_val) = 83.000000
len(have_build_less) = 285, len(have_build_less_val) = 57.000000
len(have_build_more) = 123, len(have_build_more_val) = 24.600000
658
165
success
"""