# Tricks

Short codes which facilitate my work



### copy_batch.py

批量拷贝文件

应用场景：一堆文件里只用拷贝部分。数个文件夹里样本命名相同，都需要拷贝。

方式：给出需要拷贝的文件列表txt



### pic_rename.py

批量重命名png文件

应用场景：数字编号



### torch_model_unzip.py

解压高版本pytorch(>=1.6)保存的模型，以便低版本环境可以载入



### batchRenameForSuffix.py

批量更改后缀

应用场景：把所有.tif后缀改成.png



### divide_dataset.py

用途：手动分割训练集和验证集，平衡数据分布

本文件用于统计建筑类（1类）在图像中的像素数，划分thershold，并进行文件移动



### calc-multiclass-f1-score.py

用途：计算多分类任务的f1-score

方法：对每个类分别计算二分类f1-score，参考：多分类问题的f1-macro怎么算? - 白杨的回答 - 知乎 https://www.zhihu.com/question/447276753/answer/2386014468
