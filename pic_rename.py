#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   pic_rename.py
@Time    :   2022/04/12 14:29:21
@Author  :   Lin Tesi 
@Version :   1.0
@Contact :   tesilin@zju.edu.cn
'''

import os


class BatchRename():
    """
    批量重命名文件夹中的图片文件
    """

    def __init__(self):
        self.path = r'E:\AA-LEARN\3rd year\3S\dataset\google_earth_buildings\ground_truth'  # 表示需要命名处理的文件夹

    def rename(self):
        filelist = os.listdir(self.path)  # 获取文件路径
        total_num = len(filelist)  # 获取文件长度（个数）
        i = 852  # 表示文件的命名是从1开始的
        for item in filelist:
            if item.endswith('.png'):  # 转换格式就可以调整为自己需要的格式即可
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path), str(i) + '.png')
                # dst = os.path.join(os.path.abspath(self.path), '0000' + format(str(i), '0>3s') + '.jpg')
                # 这种情况下的命名格式为0000000.jpg形式，可以自定义格式
                try:
                    os.rename(src, dst)
                    print('converting %s to %s ...' % (src, dst))
                    i = i + 1
                except:
                    continue
        print('total %d to rename & converted %d jpgs' % (total_num, i))


if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()