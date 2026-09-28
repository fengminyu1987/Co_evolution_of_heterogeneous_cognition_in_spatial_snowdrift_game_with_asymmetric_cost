import csv

import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import scipy.signal
import 实验3模型 as model


G = nx.watts_strogatz_graph(1296, 4, 0.5)

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
np.savetxt(".\实验结果\实验3_WS\\WS_1000.csv", a_distribute1000, delimiter=",", fmt="%.2f")
np.savetxt(".\实验结果\实验3_WS\\a_distribute_0.8,0.01_1000.csv", a_distribute2000, delimiter=",", fmt="%.2f")
np.savetxt(".\实验结果\实验3_WS\\a_distribute_0.8,0.01_2000.csv", a_distribute3000, delimiter=",", fmt="%.2f")
np.savetxt(".\实验结果\实验3_WS\\a_distribute_0.8,0.01_3000.csv", a_distribute4000, delimiter=",", fmt="%.2f")
np.savetxt(".\实验结果\实验3_WS\\a_distribute_0.8,0.01_4000.csv", a_distribute5000, delimiter=",", fmt="%.2f")
