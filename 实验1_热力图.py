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


def plot_rows_as_curves(matrix, output_path):
    # 获取矩阵的行数和列数
    num_rows, num_cols = matrix.shape

    # 绘制每行曲线
    for row in range(num_rows):
        plt.plot(range(num_cols), matrix[row, :], label=f"{(9 - row) / 100}")
        plt.scatter(range(num_cols), matrix[row, :])

    # 添加图例
    plt.legend()
    plt.xlabel('r')
    plt.ylabel('Cooperator frequency')
    # 显示图形
    plt.savefig(output_path, dpi=300)
    plt.show()


# 依次读取 WS、triangular 和 grid 的 CSV 数据。
data_files = [
    ("实验1_WS", "WS.csv"),
    ("实验1_triangular", "triangular.csv"),
    ("实验1_grid", "GRID.csv"),
]

for subdirectory, filename in data_files:
    with open(f".\\实验结果\\{subdirectory}\\{filename}") as f:  # 打开文件
        reader = csv.reader(f)  # 创建一个csv阅读器对象
        data = list(reader)  # 将文件内容转换为列表
        data = np.array(data, dtype=float)  # 将列表转换为numpy数组，并指定数据类型为浮点数

    # 绘制矩阵图像，并添加颜色条和标题
    # plt.matshow(data, cmap=plt.cm.jet, interpolation="gaussian")  # 使用matshow函数绘制矩阵，并指定颜色为蓝色
    plt.imshow(data, cmap=plt.cm.jet, extent=(0, 1, 0, 0.09), vmin=0, vmax=1, interpolation="gaussian", aspect=(100/9))

    plt.colorbar()  # 添加颜色条
    # x_labels =[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # y_labels = ['0.09', '0.08', '0.07', '0.06', '0.05', '0.04', '0.03', '0.02', '0.01', '0.00']
    # plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], x_labels)
    # plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], y_labels)
    ax = plt.gca()

    # 将 x 轴刻度显示在下方
    ax.xaxis.set_ticks_position('bottom')
    plt.xlabel('r')
    plt.ylabel('ε')
    plt.savefig(os.path.join('.\\实验结果', subdirectory, f'{os.path.splitext(filename)[0]}_heatmap.png'), dpi=300)
    plt.show()  # 显示图像

    # 调用函数绘制曲线
    plot_rows_as_curves(data, os.path.join('.\\实验结果', subdirectory, f'{os.path.splitext(filename)[0]}_curves.png'))
    plt.close('all')
