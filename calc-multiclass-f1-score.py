import pandas as pd
from sklearn.metrics import f1_score

# 我需要你帮我写一段程序，计算4分类任务的F1分数，具体要求如下：
# 1. 从‘./ori.csv’中读取原始数据。数据存储格式为两列，第一列是label，第二列是predict值。均存储为字符串‘tensor(num’，需要字符串中的数字num提取出来。
# 2. 对4个类别分别计算F1-score

# 从'./ori.csv'中读取原始数据
data = pd.read_csv('./ori.csv', header=None, names=['label', 'predict'], dtype=str)

# 定义函数用于从字符串中提取数字
def extract_num(string):
    return int(string.split('(')[1])

# 将字符串中的数字提取出来
data['label'] = data['label'].apply(extract_num)
data['predict'] = data['predict'].apply(extract_num)


# 计算每个类别的F1分数
classes = sorted(data['label'].unique())  # 获取所有类别的列表，排序后保证顺序一致

print(classes)

for cls in classes:
    true_positive = ((data['label'] == cls) & (data['predict'] == cls)).sum()
    true_negative = ((data['label'] != cls) & (data['predict'] != cls)).sum()
    false_positive = ((data['label'] != cls) & (data['predict'] == cls)).sum()
    false_negative = ((data['label'] == cls) & (data['predict'] != cls)).sum()

    print("TP:{}\tFP:{}\nFN:{}\tTN:{}".format(true_positive, false_positive, false_negative, true_negative))

    precision = true_positive / (true_positive + false_positive)
    recall = true_positive / (true_positive + false_negative)
    if (precision + recall) > 0:
        f1 = 2 * (precision * recall) / (precision + recall) 
    else:
        f1 = 0
    print("F1-score for class {}: {}".format(cls, f1))
    print("\n")
