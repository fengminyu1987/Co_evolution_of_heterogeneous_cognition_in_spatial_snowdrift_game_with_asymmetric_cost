import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import csv
from scipy.stats import skew
import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import scipy.signal
import 模型 as model

from scipy.stats import normaltest

with open(".\\实验结果\实验4结果\\a_0.8,0.01_4.csv") as f:  # 打开文件
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
data_skewness = skew(array)
print(f"The skewness of the data is: {data_skewness}")

with open(".\\实验结果\实验4结果\\a_0.8,0.03_4.csv") as f:  # 打开文件
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
data_skewness = skew(array1)
print(f"The skewness of the data is: {data_skewness}")

with open(".\\实验结果\实验4结果\\a_0.7,0.01_4.csv") as f:  # 打开文件
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
data_skewness = skew(array2)
print(f"The skewness of the data is: {data_skewness}")

with open(".\\实验结果\实验4结果\\a_0.7,0.03_4.csv") as f:  # 打开文件
    reader = csv.reader(f)  # 创建一个csv阅读器对象
    data = list(reader)  # 将文件内容转换为列表
    data = np.array(data, dtype=float)  # 将列表转换为numpy数组，并指定数据类型为浮点数

# 将矩阵转换为一维数组，并按照降序排序
array3 = data.flatten()
array3 = np.array(array3)
array3.sort()
array3 = abs(np.sort(-array3))
print(array3)
statistic, p_value = normaltest(array3)
data_skewness = skew(array3)
print(f"The skewness of the data is: {data_skewness}")

# with open(".\\实验结果\实验3_grid\\WS_5000.csv") as f:  # 打开文件
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
# data_skewness = skew(array4)
# print(f"The skewness of the data is: {data_skewness}")
import seaborn as sns

# # sns.kdeplot(array, fill=False, label='0', linewidth=2.0)
# # sns.kdeplot(array1, fill=False, label='T=1000', linewidth=2.0, bw_adjust=2)
plt.figure(figsize=(5,2),dpi=300)

# sns.kdeplot(array, fill=False, label='T=1000', linewidth=3.0, bw_adjust=4)
# sns.kdeplot(array1, fill=False, label='T=2000', linewidth=3.0, bw_adjust=4)
# sns.kdeplot(array2, fill=False, label='T=3000', linewidth=3.0, bw_adjust=4)
# sns.kdeplot(array3, fill=False, label='T=4000', linewidth=3.0, bw_adjust=4)
# sns.kdeplot(array4, fill=False, label='T=5000', linewidth=3.0, bw_adjust=4)

sns.kdeplot(array2, fill=False, label='r=0.7,ε=0.01', linewidth=3, bw_adjust=3, c='r', alpha=0.7)
sns.kdeplot(array3, fill=False, linestyle='--', label='r=0.7,ε=0.03', linewidth=3, bw_adjust=3, c='r')
sns.kdeplot(array,  fill=False, label='r=0.8,ε=0.01', linewidth=3, bw_adjust=3, c='blue', alpha=0.7)
sns.kdeplot(array1, fill=False, linestyle='--', label='r=0.8,ε=0.03', linewidth=3, bw_adjust=3, c='blue')
#
plt.ylabel("Frequency",fontsize=12)
plt.xlabel('favor value', fontsize=12)
#
# plt.legend()
# plt.xlim(0,)
plt.ylim(0,0.006)
plt.xlim(10,35)
#
plt.show()


#
# # 创建画板和轴
# fig, ax = plt.subplots()
#
# # 绘制五个独立的箱线图
# ax.boxplot([array, array1, array2, array3, array4], patch_artist=True)
#
# # 添加标题和标签
# ax.set_title("Five Independent Boxplots")
# ax.set_xticklabels(["Data 1", "Data 2", "Data 3", "Data 4", "Data 5"])
# ax.set_ylabel("Values")
# plt.ylim(0,)
# # 显示图形
# plt.show()




