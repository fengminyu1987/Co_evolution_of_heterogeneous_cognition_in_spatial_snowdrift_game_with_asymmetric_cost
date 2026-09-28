import math

import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import scipy.signal

'''
结点应该具有的属性：
    “恩惠值”['a']：初始都为1
    “策略”['strategy']：五五开,0:C,1:D
    “收益”

图:
    方格网络为36*36
    其他网络大小
'''


# p=0.5  #合作者初始比例
# 节点初始化
def nodes(G, p):
    C = np.array([[1, 0]])
    D = np.array([[0, 1]])
    for node in G:
        G.add_node(node, strategy=C)
        G.add_node(node, a=1)
        G.add_node(node, payoff=0.0)
    for node in random.sample(G.nodes, k=int(len(G) * p)):
        G.nodes[node]['strategy'] = D
    return G


# 费米规则，输入参数节点与其随机一个邻居适应度
def _fermi_updating_rule(fi, fj, k):
    """
    Returns the probability of individual i adopting individual j strategy
    Parameters
    ----------
    fi : float
        Payoff of individual i
    fj : float
        Payoff of individual j
    k: float
        Parameter that models the importance of a payoff difference
    Returns
    -------
    pij : float
        Probability of individual i adopting individual j strategy
    """
    return 1 / (1 + math.e ** ((fi - fj) / k))


# 合作密度
def cooperator_density(strategies, G):
    cooperator = 0
    m = len(strategies)
    # 如果不是方格网络
    for node in G:
        if strategies[node][0][0] == 1:
            cooperator += 1
    return cooperator / m


# 一轮模拟，每个结点随机抽取一个邻居进行比较,进行同步策略更新
def strategy_update_once(G, strategies):
    """
    :param G: graph
    :param strategies: 记录改变前策略的字典
    :return: 得到新的策略字典
    """
    for i in G:
        j = random.sample(list(G.neighbors(i)), 1)[0]
        fi, fj = G.nodes[i]['payoff'] * G.nodes[i]['a'], G.nodes[j]['payoff'] * G.nodes[j]['a']
        pij = _fermi_updating_rule(fi, fj, k=0.15)
        if np.random.random() < pij:
            G.nodes[i]['strategy'] = strategies[j]
    return nx.get_node_attributes(G, 'strategy')


# 常规策略更新
def normal_strategy_update_once(G, strategies):
    for i in G:
        j = random.sample(list(G.neighbors(i)), 1)[0]
        fi, fj = G.nodes[i]['payoff'], G.nodes[j]['payoff']
        pij = _fermi_updating_rule(fi, fj, k=0.15)
        if np.random.random() < pij:
            G.nodes[i]['strategy'] = strategies[j]
    return nx.get_node_attributes(G, 'strategy')


# 计算node的非对称博弈payoff
def payoff(G, node, matrix_a, r):
    """
    :param G: graph
    :param node: 当前点
    :param matrix_a: 恩惠矩阵
    :param r: SDG参数r
    :return: 当前node博弈所得
    """
    p = 0.0
    for neighbor in G.neighbors(node):
        if matrix_a[node][neighbor] == 0 and matrix_a[neighbor][node] == 0:
            Lambda = 1 / 2
        else:
            Lambda = matrix_a[neighbor][node] / (matrix_a[node][neighbor] + matrix_a[neighbor][node])
        SDG = np.array([[1 - r * Lambda, 1 - r], [1, 0]])
        p += (G.nodes[node]['strategy'] @ SDG @ G.nodes[neighbor]['strategy'].T)[0][0]
    return p


# 计算node的非对称博弈payoff（方格网络）
def payoff_grid(G, node, matrix_a, r):
    """
    :param G: graph
    :param node: 当前点
    :param matrix_a: 恩惠矩阵
    :param r: SDG参数r
    :return: 当前node博弈所得
    """
    p = 0.0
    for neighbor in G.neighbors(node):
        if matrix_a[node[0] * int(math.sqrt(len(G))) + node[1]][
            neighbor[0] * int(math.sqrt(len(G))) + neighbor[1]] + \
                matrix_a[neighbor[0] * int(math.sqrt(len(G))) + neighbor[1]][
                    node[0] * int(math.sqrt(len(G))) + node[1]] == 0:
            Lambda = 1 / 2
        else:
            Lambda = matrix_a[neighbor[0] * int(math.sqrt(len(G))) + neighbor[1]][
                         node[0] * int(math.sqrt(len(G))) + node[1]] / \
                     (matrix_a[node[0] * int(math.sqrt(len(G))) + node[1]][
                          neighbor[0] * int(math.sqrt(len(G))) + neighbor[1]] +
                      matrix_a[neighbor[0] * int(math.sqrt(len(G))) + neighbor[1]][
                          node[0] * int(math.sqrt(len(G))) + node[1]])
        SDG = np.array([[1 - r * Lambda, 1 - r], [1, 0]])
        p += (G.nodes[node]['strategy'] @ SDG @ G.nodes[neighbor]['strategy'].T)[0][0]
    return p


# 对称博弈
def normal_payoff(G, node, r):
    p = 0.0
    for neighbor in G.neighbors(node):
        SDG = np.array([[1 - r * 1 / 2, 1 - r], [1, 0]])
        p += (G.nodes[node]['strategy'] @ SDG @ G.nodes[neighbor]['strategy'].T)[0][0]
    return p


# 模拟一轮博弈结果（非对称）
def payoff_once(G, matrix_a, r):
    if type(list(G.nodes())[1]) == int:  # 如果不是方格网络
        for i in G:
            G.nodes[i]['payoff'] = payoff(G, i, matrix_a, r)
    else:
        for i in G:
            G.nodes[i]['payoff'] = payoff_grid(G, i, matrix_a, r)
    return G


# 模拟一轮对称博弈结果
def normal_payoff_once(G, r):
    for i in G:
        G.nodes[i]['payoff'] = normal_payoff(G, i, r)
    return G


# 费米规则，随机选择一个邻居判断是否给予恩惠
def _fermi_updating_rule_2(p, a_p, k):
    return 1 / (1 + math.e ** ((p - a_p) / k))


# 恩惠的给予
def give_a(G, i, j, update_matrix, epsilon):
    G.nodes[i]['a'] -= epsilon
    G.nodes[j]['a'] += epsilon
    update_matrix[i][j] += epsilon
    return update_matrix


# 恩惠的给予（方格图）
def give_a_grid(G, i, j, update_matrix, epsilon):
    G.nodes[i]['a'] -= epsilon
    G.nodes[j]['a'] += epsilon
    update_matrix[i[0] * int(math.sqrt(len(G))) + i[1]][j[0] * int(math.sqrt(len(G))) + j[1]] += epsilon
    return update_matrix


# 每个点，每个step随机选择一个邻居，判断是否需要继续给予恩惠
def give_a_process(G, r, matrix_a, strategies, epsilon):
    """
    :param epsilon: 给予的恩惠值
    :param G: graph
    :param r: SDG参数r
    :param matrix_a: 恩惠矩阵
    :param strategies: 记录的是未改变的策略。
                       在总程序中，每一轮的话应该是先博弈，然后根据恩惠值来改变策略，之后观察是否需要继续给予恩惠
                       但此时策略已经改变，只能用还未改变的策略
                       上面改变策略最后返回的是一个新的策略列表，需要一个中间变量承载一下
    :return: 得到一个新的恩惠值矩阵
    """
    update_matrix = np.zeros((len(G), len(G)))
    if type(list(G.nodes())[1]) == int:  # 如果不是方格网络
        for i in G:
            if G.nodes[i]['a'] > 0.1:
                j = random.sample(list(G.neighbors(i)), 1)[0]
                if matrix_a[i][j] + matrix_a[j][i] == 0:
                    Lambda = 1 / 2
                else:
                    Lambda = matrix_a[j][i] / (matrix_a[i][j] + matrix_a[j][i])
                SDG = np.array([[1 - r * Lambda, 1 - r], [1, 0]])
                p = (strategies[i] @ SDG @ strategies[j].T)[0][0]
                SDG = np.array([[1 - r * 1 / 2, 1 - r], [1, 0]])
                assumed_p = (strategies[i] @ SDG @ strategies[j].T)[0][0]
                p_no_action = _fermi_updating_rule_2(assumed_p, p, k=0.15)
                if np.random.random() < p_no_action:

                    if G.nodes[i]['a'] <= epsilon:
                        update_matrix = give_a(G, i, j, update_matrix, G.nodes[i]['a'] - 0.1)
                    else:
                        update_matrix = give_a(G, i, j, update_matrix, epsilon)
        for i in range(len(G)):
            for j in range(len(G)):
                matrix_a[i][j] += update_matrix[i][j]
    else:  # 如果是方格网络
        for i in G:
            if G.nodes[i]['a'] > 0.1:
                j = random.sample(list(G.neighbors(i)), 1)[0]
                if matrix_a[i[0] * int(math.sqrt(len(G))) + i[1]][
                    j[0] * int(math.sqrt(len(G))) + j[1]] + matrix_a[j[0] * int(math.sqrt(len(G))) + j[1]][
                    i[0] * int(math.sqrt(len(G))) + i[1]] == 0:
                    Lambda = 1 / 2
                else:
                    Lambda = matrix_a[j[0] * int(math.sqrt(len(G))) + j[1]][
                                 i[0] * int(math.sqrt(len(G))) + i[1]] / \
                             (matrix_a[i[0] * int(math.sqrt(len(G))) + i[1]][
                                  j[0] * int(math.sqrt(len(G))) + j[1]] +
                              matrix_a[j[0] * int(math.sqrt(len(G))) + j[1]][
                                  i[0] * int(math.sqrt(len(G))) + i[1]])
                SDG = np.array([[1 - r * Lambda, 1 - r], [1, 0]])
                p = (strategies[i] @ SDG @ strategies[j].T)[0][0]
                SDG = np.array([[1 - r * 1 / 2, 1 - r], [1, 0]])
                assumed_p = (strategies[i] @ SDG @ strategies[j].T)[0][0]
                p_no_action = _fermi_updating_rule_2(assumed_p, p, k=0.15)
                if np.random.random() < p_no_action:
                    if G.nodes[i]['a'] <= epsilon:
                        update_matrix = give_a_grid(G, i, j, update_matrix, G.nodes[i]['a'] - 0.1)
                    else:
                        update_matrix = give_a_grid(G, i, j, update_matrix, epsilon)
        for i in range(len(G)):
            for j in range(len(G)):
                matrix_a[i][j] += update_matrix[i][j]
    return matrix_a


# 基于模型设定的模拟
def simulation(G, step, r, epsilon):
    nodes(G, p=0.5)
    strategies = nx.get_node_attributes(G, 'strategy')
    f = [cooperator_density(strategies, G), ]
    matrix_a = np.zeros((len(G), len(G)))
    for i in range(step):
        print(i)
        if i == 0:
            cooperation_0 = nx.get_node_attributes(G, 'strategy')
        if i == 2000:
            a_distribute_2000 = nx.get_node_attributes(G, 'a')
            cooperation_2000 = nx.get_node_attributes(G, 'strategy')
        if i == 4000:
            a_distribute_4000 = nx.get_node_attributes(G, 'a')
            cooperation_4000 = nx.get_node_attributes(G, 'strategy')
        if i == 5000:
            a_distribute_5000 = nx.get_node_attributes(G, 'a')
            cooperation_5000 = nx.get_node_attributes(G, 'strategy')
        payoff_once(G, matrix_a, r)
        new_strategies = strategy_update_once(G, strategies)
        matrix_a = give_a_process(G, r, matrix_a, strategies, epsilon)
        strategies = new_strategies
        f.append(cooperator_density(strategies, G))
        print(f[i])
    return (f, a_distribute_2000, a_distribute_4000, a_distribute_5000, cooperation_0,
            cooperation_2000, cooperation_4000, cooperation_5000)


# 常规模拟
def normal_simulation(G, step, r):
    nodes(G, p=0.5)
    strategies = nx.get_node_attributes(G, 'strategy')
    f = [cooperator_density(strategies, G), ]
    for i in range(step):
        print(i)
        normal_payoff_once(G, r)
        new_strategies = normal_strategy_update_once(G, strategies)
        strategies = new_strategies
        f.append(cooperator_density(strategies, G))
        print(f[i])
    return f


def Cooperation_frequency_iteration_number_equal(G, step, r, epsilon):
    """
    :param G: graph
    :param step: 迭代步数
    :param r:
    :param epsilon:
    :return:
        iteration：对应data_dict.values()的索引
        cooperation： 合作迭代数据,最后的值即为稳定的合作密度即: cooperation[-1]
        list(a_distribute.values())： a的分布
    """
    iteration = list(range(0, step, 1))

    cooperation, a_distribute = simulation(G, step, r, epsilon)
    # cooperation = normal_simulation(G, num, r)

    return iteration, cooperation, list(a_distribute.values())
