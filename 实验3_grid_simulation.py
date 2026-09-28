import csv

import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import scipy.signal
import 实验3模型 as model

G = nx.Graph()  # 创建一个空的无向图

# G.add_node(1)
# G.add_node(2,role = 1)
# G.add_node(1,role = 1)
#
# print(G)
#
# for node in G:
#     print(G.nodes[node]['role'])

# C = np.array([[1, 0]])
# D = np.array([[0, 1]])
#
# SDG = np.array([[0.8, 0.6], [1, 0]])
#
# print((C @ SDG @ D.T)[0][0])


# G = nx.erdos_renyi_graph(1000, 0.6)
#
# _, y = model.Cooperation_frequency_iteration_number_equal(G, 0.4, 0.05)
#
# plt.plot(y)
# plt.show()

# G = nx.grid_2d_graph(4, 4, periodic=True)
#
# for node in G:
#     G.add_node(node, a=1)
#     print(node)
#
# a_distribute = nx.get_node_attributes(G, 'a')
# a_distribute_array = np.zeros((4, 4))
#
# for node in G.nodes():
#     a_distribute_array[node[0]][node[1]] = a_distribute[node]
#
# print(a_distribute_array)


'''G = nx.grid_2d_graph(4, 4, periodic=True)
for i in range(3):
    for j in range(3):
        G.add_edge((i, j), (i + 1, j + 1))  # 右下对角线
        G.add_edge((i, j + 1), (i + 1, j))  # 左下对角线

for j in range(1, 3):
    G.add_edge((3, j), (0, j + 1))
    G.add_edge((3, j), (0, j - 1))

for i in range(1, 3):
    G.add_edge((i, 3), (i + 1, 0))
    G.add_edge((i, 3), (i - 1, 0))

G.add_edge((0, 2), (3, 3))
G.add_edge((2, 0), (3, 3))

G.add_edge((0, 1), (3, 0))
G.add_edge((2, 3), (3, 0))

G.add_edge((0, 3), (1, 0))

G.add_edge((0, 0), (3, 3))
G.add_edge((0, 3), (3, 0))

for node in G:
    print('\t', node)
    print(len(G[node]))
    for neighbor in G.neighbors(node):
        print(neighbor)
    print("")'''

"""
由此开始
"""
# 方格图
G = nx.grid_2d_graph(36, 36, periodic=True)
for i in range(35):
    for j in range(35):
        G.add_edge((i, j), (i + 1, j + 1))  # 右下对角线
        G.add_edge((i, j + 1), (i + 1, j))  # 左下对角线
        
for j in range(1, 35):
    G.add_edge((35, j), (0, j + 1))
    G.add_edge((35, j), (0, j - 1))

for i in range(1, 35):
    G.add_edge((i, 35), (i + 1, 0))
    G.add_edge((i, 35), (i - 1, 0))
G.add_edge((0, 0), (35, 35))
G.add_edge((0, 34), (35, 35))
G.add_edge((34, 0), (35, 35))
G.add_edge((0, 1), (35, 0))
G.add_edge((34, 35), (35, 0))
G.add_edge((0, 35), (1, 0))
G.add_edge((0, 35), (35, 0))

for node in G:
    if len(list(G.neighbors(node))) != 8:
        print(node)

cf, a1000, a2000, a3000, a4000, a5000 = model.simulation(G, 5001, 0.8, 0.01)


a_distribute1000 = np.zeros((36, 36))
a_distribute2000 = np.zeros((36, 36))
a_distribute3000 = np.zeros((36, 36))
a_distribute4000 = np.zeros((36, 36))
a_distribute5000 = np.zeros((36, 36))

for node in G.nodes():
    a_distribute1000[node[0]][node[1]] = a1000[node]
    a_distribute2000[node[0]][node[1]] = a2000[node]
    a_distribute3000[node[0]][node[1]] = a3000[node]
    a_distribute4000[node[0]][node[1]] = a4000[node]
    a_distribute5000[node[0]][node[1]] = a5000[node]
    
    
#np.savetxt("D:\实验结果\my_data_a_distribute_0.6,0.03.csv", a_distribute, delimiter=",", fmt="%.2f")
np.savetxt(".\实验结果\摩尔方格a分布\\a_distribute_0.8,0.01_1000.csv", a_distribute1000, delimiter=",", fmt="%.2f")
np.savetxt(".\实验结果\摩尔方格a分布\\a_distribute_0.8,0.01_2000.csv", a_distribute2000, delimiter=",", fmt="%.2f")
np.savetxt(".\实验结果\摩尔方格a分布\\a_distribute_0.8,0.01_3000.csv", a_distribute3000, delimiter=",", fmt="%.2f")
np.savetxt(".\实验结果\摩尔方格a分布\\a_distribute_0.8,0.01_4000.csv", a_distribute4000, delimiter=",", fmt="%.2f")
np.savetxt(".\实验结果\摩尔方格a分布\\a_distribute_0.8,0.01_5000.csv", a_distribute5000, delimiter=",", fmt="%.2f")
