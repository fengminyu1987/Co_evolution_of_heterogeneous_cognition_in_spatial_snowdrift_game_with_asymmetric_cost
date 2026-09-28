import csv
import math

import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import scipy.signal
import 模型 as model

# A = np.random.rand(10, 10)
#
# # 使用matshow函数来绘制矩阵
# plt.matshow(A, interpolation='bilinear')
# plt.show()


# 需要二维参数图的数据
r_num = 2
epsilon_num = 2

rs = np.linspace(0.5, 0.6, r_num, endpoint=True)  # 生成0.05到1，包含20个元素的等差数列
rs = list(rs)  # 将numpy数组转换成列表

epsilons = np.linspace(0.08, 0.09, epsilon_num, endpoint=True)  # 生成0.05到1，包含20个元素的等差数列
epsilons = list(epsilons)  # 将numpy数组转换成列表
fs = np.zeros((9,9))

step = 5000
time = 5

for t in range(time):
    print("time:", t)

    G = nx.watts_strogatz_graph(1296, 4, 0.5)  # WS
    # G = nx.triangular_lattice_graph(36, 36, periodic=True)  # 三角网络
    # G = nx.grid_2d_graph(36, 36, periodic=True)  # 方格网络
    # for i in range(35):
    #     for j in range(35):
    #         G.add_edge((i, j), (i + 1, j + 1))  # 右下对角线
    #         G.add_edge((i, j + 1), (i + 1, j))  # 左下对角线
            
    # for j in range(1, 35):
    #     G.add_edge((35, j), (0, j + 1))
    #     G.add_edge((35, j), (0, j - 1))
    
    # for i in range(1, 35):
    #     G.add_edge((i, 35), (i + 1, 0))
    #     G.add_edge((i, 35), (i - 1, 0))
    # G.add_edge((0, 0), (35, 35))
    # G.add_edge((0, 34), (35, 35))
    # G.add_edge((34, 0), (35, 35))
    # G.add_edge((0, 1), (35, 0))
    # G.add_edge((34, 35), (35, 0))
    # G.add_edge((0, 35), (1, 0))
    # G.add_edge((0, 35), (35, 0))


    for r in rs:
        r = round(r, 2)
        for epsilon in epsilons:
            epsilon = round(epsilon, 2)
            print("r:", r, "   e:", epsilon)
            if t == 5 and r == 0.7 and epsilon == 0.1:
                cf, a_distribute = model.simulation(G, step, r, epsilon)
                cooperation = nx.get_node_attributes(G, 'strategy')
            else:
                cf = model.simulation(G, step, r, epsilon)
            print(cf)
            
            plt.plot(cf)
            plt.title("times:{:d}\nr: {:.2f}\ne: {:.2f}".format(t,r,epsilon))
            plt.show()
            
            a = int(r * 10 - 1)
            b = int(8 - (epsilon * 100 - 1))
            fs[b][a] += cf[-1]

#a_distribute_array = np.zeros((36, 36))
#c_distribute_array = np.zeros((36, 36))

#G = nx.grid_2d_graph(36, 36, periodic=True)
#for node in G.nodes():
#    a_distribute_array[node[0]][node[1]] = a_distribute[node]
#    c_distribute_array[node[0]][node[1]] = cooperation[node][0][0]

for i in range(9):
    for j in range(9):
        fs[i][j] /= time

print(fs)

np.savetxt(".\实验结果\实验1_WS\WS.csv", fs, delimiter=",", fmt="%.2f")
# np.savetxt(".\实验结果\实验1_triangular\\triangular.csv", fs, delimiter=",", fmt="%.2f")
# np.savetxt(".\实验结果\实验1_grid\grid.csv", fs, delimiter=",", fmt="%.2f")
