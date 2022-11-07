#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   copy_batch.py
@Time    :   2022/11/07 14:27:32
@Author  :   Lin Tesi 
@Version :   1.0
@Contact :   tesilin@zju.edu.cn
'''

import shutil
import numpy as np

def copyimgs(sourcePath,targetPath,imglist):

    for objName in np.loadtxt(imglist,dtype=np.str_,encoding='utf-8'):
        shutil.copy(sourcePath + '/' + objName + '.png', targetPath + '/' + objName + '.png')
 
if __name__ == '__main__':
    # 读取一个图像名列表
    imgList = r'C:\Users\lenovo\Desktop\copylist.txt'
    # 复制影像的文件夹
    sourcePath = r'C:\Users\lenovo\Desktop\process\split\85007'
    # 目标文件夹
    targetPath = r'C:\Users\lenovo\Desktop\process\house_detect\85007'
    copyimgs(sourcePath,targetPath,imgList)
