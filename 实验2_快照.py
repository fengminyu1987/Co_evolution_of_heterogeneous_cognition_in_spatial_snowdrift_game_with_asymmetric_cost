import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import numpy as np
import matplotlib.pyplot as plt

# 从CSV文件加载数据到NumPy数组
plt.figure(figsize=(5,5))
data = np.genfromtxt('.\\实验结果\实验2结果\\c_0.6,0.03_0.csv', delimiter=',')
plt.axis('off')

# 绘制矩阵
plt.imshow(data, cmap='bwr_r')  # cmap是颜色映射，可以根据需要更改

plt.show()





