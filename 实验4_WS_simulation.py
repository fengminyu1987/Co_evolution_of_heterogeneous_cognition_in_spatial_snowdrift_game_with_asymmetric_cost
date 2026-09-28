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

# WS
G = nx.watts_strogatz_graph(1296, 4, 0.5)

for t in range(4):
    if t == 0:
        cf, a_4 = model.simulation(G, 4001, 0.7, 0.01)
        a_distribute_4 = np.zeros(1296)
        for node in G.nodes():
            a_distribute_4[node] = a_4[node]
        np.savetxt(".\\实验结果\实验4结果\\a_0.7,0.01_4.csv", a_distribute_4, delimiter=",", fmt="%.2f")
    if t == 1:
        cf, a_4 = model.simulation(G, 4001, 0.7, 0.03)
        a_distribute_4 = np.zeros(1296)
        for node in G.nodes():
            a_distribute_4[node] = a_4[node]
        np.savetxt(".\\实验结果\实验4结果\\a_0.7,0.03_4.csv", a_distribute_4, delimiter=",", fmt="%.2f")
    if t == 2:
        cf, a_4 = model.simulation(G, 4001, 0.8, 0.01)
        a_distribute_4 = np.zeros(1296)
        for node in G.nodes():
            a_distribute_4[node] = a_4[node]
        np.savetxt(".\\实验结果\实验4结果\\a_0.8,0.01_4.csv", a_distribute_4, delimiter=",", fmt="%.2f")
    if t == 3:
        cf, a_4 = model.simulation(G, 4001, 0.8, 0.03)
        a_distribute_4 = np.zeros(1296)
        for node in G.nodes():
            a_distribute_4[node] = a_4[node]
        np.savetxt(".\\实验结果\实验4结果\\a_0.8,0.03_4.csv", a_distribute_4, delimiter=",", fmt="%.2f")




