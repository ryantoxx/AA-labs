import time
import numpy as np 

from dfs import dfs
from bfs import bfs
from graphs import balanced_tree, unbalanced_tree

import matplotlib.pyplot as plt
from prettytable import PrettyTable

def compare_algorithms(tree, nodes):
    dfs_time = []
    bfs_time = []

    for node in nodes:
        start_time = time.perf_counter()
        dfs(tree, 1, node)
        dfs_time.append(round(time.perf_counter() - start_time, 7))
        start_time = time.perf_counter()
        bfs(tree, 1, node)
        bfs_time.append(round(time.perf_counter() - start_time, 7))

    if len(nodes) == 5 and set(nodes) == set([4, 8, 15, 18, 24]): 
        print('\nBalanced Tree')
        table = PrettyTable(['Name/Node', '4', '8', '15', '18', '24'])
    elif len(nodes) == 5 and set(nodes) == set([4, 11, 17, 22, 25]): 
        print('\nUnbalanced Tree')
        table = PrettyTable(['Name/Node', '4', '11', '17', '22', '25'])
    else:
        print('\nInvalid nodes list')
        return

    table.add_row(['DFS', dfs_time[0], dfs_time[1], dfs_time[2], dfs_time[3], dfs_time[4]])
    table.add_row(['BFS', bfs_time[0], bfs_time[1], bfs_time[2], bfs_time[3], bfs_time[4]])
    print(table)

    x_axis = np.arange(len(nodes))
    plt.bar(x_axis - 0.2, dfs_time, 0.4, label='DFS')
    plt.bar(x_axis + 0.2, bfs_time, 0.4, label='BFS')
    plt.xticks(x_axis, nodes)
    plt.xlabel('Node')
    plt.ylabel('Time, s')
    if set(nodes) == set([4, 8, 15, 18, 24]): plt.title('Balanced Tree')
    elif set(nodes) == set([4, 11, 17, 22, 25]): plt.title('Unbalanced Tree')
    plt.legend()
    plt.show()

bal_tree_nodes = [4, 8, 15, 18, 24]
unbal_tree_nodes = [4, 11, 17, 22, 25]
compare_algorithms(balanced_tree(), bal_tree_nodes)
compare_algorithms(unbalanced_tree(), unbal_tree_nodes)
