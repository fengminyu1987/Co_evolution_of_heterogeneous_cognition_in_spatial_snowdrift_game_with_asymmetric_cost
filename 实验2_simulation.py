import csv
import math

import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import scipy.signal
import 实验2模型 as model


step = 5000
r = 0.5
epsilon = 0.01

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


(cf, a_distribute_2000, a_distribute_4000, a_distribute_5000,
 cooperation_0, cooperation_2000, cooperation_4000, cooperation_5000) = model.simulation(G, step, r, epsilon)

cooperation = nx.get_node_attributes(G, 'strategy')

a_distribute_array_2000 = np.zeros((36, 36))
a_distribute_array_4000 = np.zeros((36, 36))
a_distribute_array_5000 = np.zeros((36, 36))

c_distribute_array_0 = np.zeros((36, 36))
c_distribute_array_2000 = np.zeros((36, 36))
c_distribute_array_4000 = np.zeros((36, 36))
c_distribute_array_5000 = np.zeros((36, 36))

G = nx.grid_2d_graph(36, 36, periodic=True)
for node in G.nodes():
   a_distribute_array_2000[node[0]][node[1]] = a_distribute_2000[node]
   a_distribute_array_4000[node[0]][node[1]] = a_distribute_4000[node]
   a_distribute_array_5000[node[0]][node[1]] = a_distribute_5000[node]
   c_distribute_array_0[node[0]][node[1]] = cooperation_0[node][0][0]
   c_distribute_array_2000[node[0]][node[1]] = cooperation_2000[node][0][0]
   c_distribute_array_4000[node[0]][node[1]] = cooperation_4000[node][0][0]
   c_distribute_array_5000[node[0]][node[1]] = cooperation_5000[node][0][0]


np.savetxt(rf".\实验结果\实验2结果\a_{r},{epsilon}_2.csv", a_distribute_array_2000, delimiter=",", fmt="%.2f")
np.savetxt(rf".\实验结果\实验2结果\a_{r},{epsilon}_4.csv", a_distribute_array_4000, delimiter=",", fmt="%.2f")
np.savetxt(rf".\实验结果\实验2结果\a_{r},{epsilon}_5.csv", a_distribute_array_5000, delimiter=",", fmt="%.2f")

np.savetxt(rf".\实验结果\实验2结果\c_{r},{epsilon}_0.csv", c_distribute_array_0, delimiter=",", fmt="%.2f")
np.savetxt(rf".\实验结果\实验2结果\c_{r},{epsilon}_2.csv", c_distribute_array_2000, delimiter=",", fmt="%.2f")
np.savetxt(rf".\实验结果\实验2结果\c_{r},{epsilon}_4.csv", c_distribute_array_4000, delimiter=",", fmt="%.2f")
np.savetxt(rf".\实验结果\实验2结果\c_{r},{epsilon}_5.csv", c_distribute_array_5000, delimiter=",", fmt="%.2f")