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

# grid
G = nx.grid_2d_graph(36, 36, periodic=True)  # 方格网络
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

for t in range(4):
    if t == 0:
        cf, a_4 = model.simulation(G, 4001, 0.7, 0.01)
        a_distribute_4 = np.zeros(1296)
        for node in G.nodes():
            a_distribute_4[node] = a_4[node]
        np.savetxt(".\\实验结果\摩尔方格a分布\\a_0.7,0.01_4.csv", a_distribute_4, delimiter=",", fmt="%.2f")
    if t == 1:
        cf, a_4 = model.simulation(G, 4001, 0.7, 0.03)
        a_distribute_4 = np.zeros(1296)
        for node in G.nodes():
            a_distribute_4[node] = a_4[node]
        np.savetxt(".\\实验结果\摩尔方格a分布\\a_0.7,0.03_4.csv", a_distribute_4, delimiter=",", fmt="%.2f")
    if t == 2:
        cf, a_4 = model.simulation(G, 4001, 0.8, 0.01)
        a_distribute_4 = np.zeros(1296)
        for node in G.nodes():
            a_distribute_4[node] = a_4[node]
        np.savetxt(".\\实验结果\摩尔方格a分布\\a_0.8,0.01_4.csv", a_distribute_4, delimiter=",", fmt="%.2f")
    if t == 3:
        cf, a_4 = model.simulation(G, 4001, 0.8, 0.03)
        a_distribute_4 = np.zeros(1296)
        for node in G.nodes():
            a_distribute_4[node] = a_4[node]
        np.savetxt(".\\实验结果\摩尔方格a分布\\a_0.8,0.03_4.csv", a_distribute_4, delimiter=",", fmt="%.2f")




