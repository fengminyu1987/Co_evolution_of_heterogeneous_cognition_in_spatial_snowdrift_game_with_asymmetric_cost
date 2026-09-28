import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import csv

import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import scipy.signal
import seaborn as sns
from scipy.stats import normaltest

import 模型 as model

with open(".\\实验结果\\实验3_WS\WS_5000.csv") as f:  # 打开文件
    reader = csv.reader(f)  # 创建一个csv阅读器对象
    data = list(reader)  # 将文件内容转换为列表
    data = np.array(data, dtype=float)  # 将列表转换为numpy数组，并指定数据类型为浮点数

# 将矩阵转换为一维数组，并按照降序排序
array = data.flatten()
array = np.array(array)
array.sort()
array = abs(np.sort(-array))
print(array)
statistic, p_value = normaltest(array)

with open(".\\实验结果\\实验3_WS\WS_2000.csv") as f:  # 打开文件
    reader = csv.reader(f)  # 创建一个csv阅读器对象
    data = list(reader)  # 将文件内容转换为列表
    data = np.array(data, dtype=float)  # 将列表转换为numpy数组，并指定数据类型为浮点数

# 将矩阵转换为一维数组，并按照降序排序
array1 = data.flatten()
array1 = np.array(array1)
array1.sort()
array1 = abs(np.sort(-array1))
print(array1)
statistic, p_value = normaltest(array1)

with open(".\\实验结果\\实验3_WS\WS_1000.csv") as f:  # 打开文件
    reader = csv.reader(f)  # 创建一个csv阅读器对象
    data = list(reader)  # 将文件内容转换为列表
    data = np.array(data, dtype=float)  # 将列表转换为numpy数组，并指定数据类型为浮点数

# 将矩阵转换为一维数组，并按照降序排序
array2 = data.flatten()
array2 = np.array(array2)
array2.sort()
array2 = abs(np.sort(-array2))
print(array2)
statistic, p_value = normaltest(array2)
sns.kdeplot(array, fill=False, label='r=0.6,ε=0.03,5000', linewidth=3.0,bw_adjust=2)
sns.kdeplot(array1, fill=False, label='r=0.6,ε=0.03,2000', linewidth=3.0,bw_adjust=2)
sns.kdeplot(array2, fill=False, label='r=0.6,ε=0.03,1000', linewidth=3.0,bw_adjust=2)



# sns.kdeplot(array2, fill=False, label='r=0.6,ε=0.01', linewidth=2.0, bw_adjust=2)
# sns.kdeplot(array8, fill=False, label='r=0.7,ε=0.01', linewidth=2.0, bw_adjust=3)


# sns.kdeplot(array5, fill=False, label='r=0.6,ε=0.02', linewidth=2.0, bw_adjust=2)
# sns.kdeplot(array6, fill=False, label='r=0.6,ε=0.05', linewidth=2.0, bw_adjust=2)

plt.ylabel("Frequency")
plt.legend()
plt.xlim(0,)
plt.show()

# for i in range(len(hist)):
#     plt.scatter(bins[i] + (bins[i + 1] - bins[i]) / 2, hist[i]/1296, color='r', marker="s")
# # plt.ylim(0, 0.25)
# # plt.yticks([0, 0.05, 0.10, 0.15, 0.20, 0.25])
# plt.show()


plt.bar(range(len(array)), array)
plt.show()





