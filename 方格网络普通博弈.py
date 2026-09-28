import csv

import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import scipy.signal
import 模型 as model

rs = np.linspace(0.1, 0.9, 9, endpoint=True)  # 生成0.05到1，包含20个元素的等差数列
rs = list(rs)  # 将numpy数组转换成列表

fs = np.zeros(9)
step = 5000
time = 5

for t in range(time):
    print("time:", t)
    # 创建网络（方格网络）
    G = nx.watts_strogatz_graph(1296, 4, 0.5)

    for r in rs:
        r = round(r, 2)
        print("r:", r)
        cf = model.normal_simulation(G, step, r)
        print(cf)

        plt.plot(cf)
        plt.title("times:{:d}\nr: {:.2f}".format(t, r))
        plt.show()
        a = int(r * 10 - 1)
        fs[a] += cf[-1]

# a_distribute_array = np.zeros((36, 36))
# c_distribute_array = np.zeros((36, 36))

# G = nx.grid_2d_graph(36, 36, periodic=True)
# for node in G.nodes():
#    a_distribute_array[node[0]][node[1]] = a_distribute[node]
#    c_distribute_array[node[0]][node[1]] = cooperation[node][0][0]

for i in range(9):
    fs[i] /= time

print(fs)

np.savetxt("D:\实验结果\my_data_two_param.csv", fs, delimiter=",", fmt="%.2f")
