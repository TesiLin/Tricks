#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   torch_model_unzip.py
@Time    :   2022/11/07 14:00:15
@Author  :   Lin Tesi 
@Version :   1.0
@Contact :   tesilin@zju.edu.cn
'''

'''
脚本内容：解压缩pth文件

pytorch>=1.6时，保存模型会进行压缩，pth文件实际上是个zip
为了在低版本torch中载入模型，需要进行转存
'''

InputFilePath = "./CBST_2Urban.pth"
OutputFilePath = InputFilePath

import torch

print(torch.cuda.is_available())
state_dict = torch.load(InputFilePath, map_location='cpu')	#xxx.pth或者xxx.pt就是你想改掉的权重文件
torch.save(state_dict, OutputFilePath, _use_new_zipfile_serialization=False)
