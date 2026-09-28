import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import csv

import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import scipy.signal
import 模型 as model

from scipy.stats import normaltest

with open(".\\实验结果\实验2结果\\a_0.5,0.01_2.csv") as f:  # 打开文件
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

with open(".\\实验结果\实验2结果\\a_0.5,0.01_4.csv") as f:  # 打开文件
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

with open(".\\实验结果\实验2结果\\a_0.5,0.01_5.csv") as f:  # 打开文件
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
#
# with open(".\\实验结果\实验3结果\\WS_4000.csv") as f:  # 打开文件
#     reader = csv.reader(f)  # 创建一个csv阅读器对象
#     data = list(reader)  # 将文件内容转换为列表
#     data = np.array(data, dtype=float)  # 将列表转换为numpy数组，并指定数据类型为浮点数
#
# # 将矩阵转换为一维数组，并按照降序排序
# array3 = data.flatten()
# array3 = np.array(array3)
# array3.sort()
# array3 = abs(np.sort(-array3))
# print(array3)
# statistic, p_value = normaltest(array3)
#
# with open(".\\实验结果\实验3结果\\WS_5000.csv") as f:  # 打开文件
#     reader = csv.reader(f)  # 创建一个csv阅读器对象
#     data = list(reader)  # 将文件内容转换为列表
#     data = np.array(data, dtype=float)  # 将列表转换为numpy数组，并指定数据类型为浮点数
#
# # 将矩阵转换为一维数组，并按照降序排序
# array4 = data.flatten()
# array4 = np.array(array4)
# array4.sort()
# array4 = abs(np.sort(-array4))
# print(array4)
# statistic, p_value = normaltest(array4)
#
import seaborn as sns
plt.figure(dpi=200)
# sns.kdeplot(array, fill=False, label='0', linewidth=2.0)
# sns.kdeplot(array1, fill=False, label='T=1000', linewidth=2.0, bw_adjust=2)

sns.kdeplot(array, fill=False, label='T=2000', linewidth=3,bw_adjust=2)
sns.kdeplot(array1, fill=False, label='T=4000', linewidth=3,bw_adjust=3)
sns.kdeplot(array2, fill=False, label='T=5000', linewidth=3.0,bw_adjust=4)
# sns.kdeplot(array3, fill=False, label='T=4000', linewidth=3.0, bw_adjust=2)
# sns.kdeplot(array4, fill=False, label='T=5000', linewidth=3.0, bw_adjust=2)

# sns.kdeplot(array1, fill=False, linestyle='--', label='r=0.8,ε=0.03', linewidth=3.0, bw_adjust=2, c='blue')
# sns.kdeplot(array2, fill=False, label='r=0.7,ε=0.01', linewidth=3.0, bw_adjust=2, c='r', alpha=0.7)
# sns.kdeplot(array4, fill=False, linestyle='--', label='r=0.7,ε=0.03', linewidth=3.0, bw_adjust=2,c='r')

plt.ylabel("Frequency")
plt.xlabel('favor value')

plt.legend()

# plt.ylim(0,0.02)
# plt.xlim(0, )

plt.show()




